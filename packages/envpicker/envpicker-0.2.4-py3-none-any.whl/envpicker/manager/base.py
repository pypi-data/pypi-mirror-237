from __future__ import annotations
from typing import Optional, TypedDict, Generator, Tuple
import os
from abc import ABC, abstractmethod
from wrapconfig import YAMLWrapConfig
import subprocess
import hashlib
import subprocess
import yaml
import re

from ..logger import ENVPICKER_LOGGER
from ..utils import (
    split_version,
    SpecifierSet,
    matches_version,
    PackageVersionCondition,
)


class EnvironmentEntry(TypedDict):
    hash: str
    path: str
    name: str
    py_executable: str


class FullEnvironmentEntry(EnvironmentEntry):
    envdata: Optional[EnvYaml]


class EnvYaml(TypedDict):
    name: str
    dependencies: list[str]


class EnvExistsError(Exception):
    pass


def path_hash(path: str) -> str:
    """
    Return the hash of the path as md5
    """
    return hashlib.md5(path.encode()).hexdigest()


def is_package_entry(entry: str) -> bool:
    """
    Return True if the entry is a package
    """
    if not isinstance(entry, str):
        return False
    # forbid any whitespace and linebreaks via regex
    if re.search(r"\s", entry):
        return False

    # require version specifier

    vs = (
        entry.replace(">", "=")
        .replace("<", "=")
        .replace("!", "=")
        .replace("==", "=")
        .split("=", 1)
    )
    if len(vs) != 2:
        return False
    e, v = vs
    if not e or not v:
        return False

    return True


class BaseEnvManager(ABC):
    def __init__(self, path: Optional[str] = None) -> None:
        super().__init__()
        if not path:
            path = os.environ.get(
                "ENV_MANAGER_PATH",
                os.path.join(os.path.expanduser("~"), ".env_manager"),
            )
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        if not os.path.isdir(path):
            raise FileExistsError("The path specified is not a directory")
        self.path = path

        self.registry = YAMLWrapConfig(os.path.join(self.path, "registry.yml"))

    @property
    def environments(self) -> list[EnvironmentEntry]:
        envs = self.registry.get("environments")
        if not envs:
            return []
        return envs

    @environments.setter
    def environments(self, envs: list[EnvironmentEntry]):
        # validate envs
        envs = list(envs)
        for env in envs:
            self.validate_env(env)

        self.registry.set("environments", envs)

    def env_to_full_env(self, env: EnvironmentEntry) -> FullEnvironmentEntry:
        yaml_path = os.path.join(self.path, f"{env['hash']}.yaml")
        if not os.path.isfile(yaml_path):
            self.create_env_yaml(env)
        with open(yaml_path, "r") as f:
            envdata = yaml.safe_load(f)
        return FullEnvironmentEntry(**env, envdata=envdata)

    @classmethod
    def validate_env(cls, env: EnvironmentEntry):
        if not os.path.isdir(env["path"]):
            raise FileNotFoundError("The path does not exist")
        if not os.path.isfile(env["py_executable"]):
            raise FileNotFoundError("The python executable does not exist")
        if not env["name"]:
            raise ValueError("The environment name cannot be empty")
        if not env["hash"]:
            raise ValueError("The environment hash cannot be empty")

    def get_env_by_path(self, path: str) -> Optional[FullEnvironmentEntry]:
        envs = self.environments
        path = os.path.normpath(os.path.abspath(path))
        for env in envs:
            if env["path"] == path:
                # get the yaml file
                return self.env_to_full_env(env)
        return None

    @classmethod
    @abstractmethod
    def is_available(cls) -> bool:
        """Return True if the manager is available."""

    @classmethod
    @abstractmethod
    def register_all(cls) -> None:
        """Register all available environments."""

    def register_environment(
        self,
        path: str,
        py_executable: Optional[str] = None,
        name: Optional[str] = None,
        force: bool = False,
    ) -> FullEnvironmentEntry:
        ENVPICKER_LOGGER.info("Registering environment %s", path)
        if not os.path.isdir(path):
            raise FileNotFoundError("The path does not exist")

        path = os.path.normpath(os.path.abspath(path))
        if py_executable is None:
            # if windows
            if os.name == "nt":
                py_executable = os.path.join(path, "python.exe")
            elif os.name == "posix":
                py_executable = os.path.join(path, "bin", "python")
            else:
                raise OSError("Unsupported OS")

        # try to call the python executable
        try:
            subprocess.check_output([py_executable, "--version"])
        except Exception as exc:
            raise ValueError("The python executable is not valid") from exc

        return self.add_env(
            path=path, py_executable=py_executable, name=name, force=force
        )

    def add_env(
        self,
        path: str,
        py_executable: str,
        name: Optional[str] = None,
        force: bool = False,
    ) -> FullEnvironmentEntry:
        """
        Register an environment in the .env_manager folder
        """
        ENVPICKER_LOGGER.info("Adding environment %s", path)
        path = os.path.normpath(os.path.abspath(path))

        new_env = EnvironmentEntry(
            path=path, hash=path_hash(path=path), name=name, py_executable=py_executable
        )
        env = None
        env = self.get_env_by_path(path=path)
        print(env, new_env)
        if env is not None and not force:
            raise EnvExistsError("The environment is already registered")

        envs = self.environments
        if env:
            env = [e for e in envs if e["path"] == path][0]
            env.update(new_env)
        else:
            env = new_env
            envs.append(new_env)

        self.environments = envs

        self.create_env_yaml(env)
        return self.get_env_by_path(path=path)

    def create_env_yaml(self, env: EnvironmentEntry):
        ENVPICKER_LOGGER.debug("Creating yaml for %s", env["name"])
        yaml_path = os.path.join(self.path, f"{env['hash']}.yaml")

        # get all methods of self, that start with create_env_yaml_

        dependencies = self.get_dependencies(env)

        data = EnvYaml(
            name=env["name"],
            dependencies=dependencies,
        )

        with open(yaml_path, "w") as f:
            yaml.dump(data, f)

        # export the environment to yaml
        # if windows

    @abstractmethod
    def get_dependencies(self, env: EnvironmentEntry) -> list[str]:
        """Return the dependencies of the environment"""

    def find_matching(
        self, required_dependencies: list[str]
    ) -> Generator[str, None, None]:
        split_deps: list[PackageVersionCondition] = [
            split_version(dep) for dep in required_dependencies
        ]
        envs = self.environments

        for env in envs:
            matches = True
            full_env = self.env_to_full_env(env)
            packages = full_env["envdata"]["dependencies"]
            packages = [split_version(dep) for dep in packages]
            packages = {dep["pkg"].lower(): dep for dep in packages}
            for required_dep in split_deps:
                if required_dep["pkg"].lower() not in packages:
                    matches = False
                    break
                if not matches_version(
                    required_dep["vstring"],
                    packages[required_dep["pkg"].lower()]["vstring"],
                ):
                    matches = False
                    break

            if matches:
                yield env

    @staticmethod
    def stream_process(
        proc: subprocess.Popen,
    ) -> Generator[Tuple[bytes, bytes], None, None]:
        # Stream the output continuously
        while True:
            output_stdout = proc.stdout.read1()
            output_stderr = proc.stderr.read1()
            if output_stdout or output_stderr:
                yield output_stdout or b"", output_stderr or b""
            if proc.poll() is not None:
                break
        yield b"\n", b"\n"
        _, errors = proc.communicate()

        if errors:
            raise RuntimeError(errors.decode())

    @staticmethod
    def run_py_in_env(
        env: dict, command: str
    ) -> Generator[Tuple[bytes, bytes], None, None]:
        """
        Calls the Python executable from the specified envirbonment and executes the given command.
        Yields the output line by line.
        """
        py_executable_path = env["py_executable"]
        # Start the command with the specified Python executable
        with subprocess.Popen(
            [py_executable_path, "-u", "-c", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as proc:
            yield from BaseEnvManager.stream_process(proc)

    def run_py_in_matching(
        self, required_dependencies: list[str], command: str
    ) -> Generator[bytes, None, None]:
        """
        Runs the given command in the first matching environment.
        """
        env = next(self.find_matching(required_dependencies))
        yield from self.run_py_in_env(env, command)

    @staticmethod
    def run_pyfile_in_env(
        env: dict, path: str
    ) -> Generator[Tuple[bytes, bytes], None, None]:
        """
        Calls the Python executable from the specified envirbonment and executes the given command.
        Yields the output line by line.
        """
        py_executable_path = env["py_executable"]
        path = os.path.abspath(path)
        # Start the command with the specified Python executable
        with subprocess.Popen(
            [py_executable_path, "-u", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as proc:
            yield from BaseEnvManager.stream_process(proc)

    def run_pyfile_in_matching(
        self, required_dependencies: list[str], path: str
    ) -> Generator[Tuple[bytes, bytes], None, None]:
        """
        Runs the given command in the first matching environment.
        """
        env = next(self.find_matching(required_dependencies))
        yield from self.run_pyfile_in_env(env, path)
