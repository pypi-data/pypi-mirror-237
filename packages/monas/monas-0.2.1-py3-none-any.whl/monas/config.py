from __future__ import annotations

import sys
import typing
from pathlib import Path
from typing import Iterable

import click
from tomlkit.toml_file import TOMLFile

from monas.vcs import Git

if typing.TYPE_CHECKING:
    from tomlkit.toml_document import TOMLDocument

    from monas.project import PyPackage


class Config:
    """The configuration for monas tool.

    It is stored as [tool.monas] table in the `pyproject.toml` file.
    """

    _pyproject: TOMLDocument
    _tool: dict

    def __init__(self) -> None:
        self.path = self._locate_mono_project()

    def _locate_mono_project(self) -> Path:
        """Find the pyproject.toml with monas setting in the current or parent dirs"""
        path = Path.cwd().absolute()
        for parent in [path, *path.parents]:
            if not (parent / "pyproject.toml").exists():
                continue
            self._pyproject = TOMLFile(parent / "pyproject.toml").read()
            self._tool = self._pyproject.setdefault("tool", {}).setdefault("monas", {})
            if self._tool:
                return parent
        raise click.UsageError(
            "Monas repo isn't initialized, have you run `monas init`?"
        )

    def get_repo(self) -> Git:
        """Get the git repository."""
        return Git(self.path)

    @property
    def root_venv(self) -> Path:
        return self.path / ".venv"

    @property
    def homepage(self) -> str | None:
        """Get the homepage."""
        urls = self._pyproject.get("project", {}).get("urls", {})
        return urls.get("Home", urls.get("Homepage"))

    @property
    def package_paths(self) -> list[Path]:
        """The list of paths that contain packages"""
        return [self.path / p for p in self._tool.get("packages", [])]

    @property
    def version(self) -> str:
        """The version of the monorepo"""
        return self._tool.get("version", "0.0.0")

    def set_version(self, version: str) -> None:
        """Set the version of the monorepo"""
        self._tool["version"] = version
        TOMLFile(self.path / "pyproject.toml").write(self._pyproject)

    @property
    def python_version(self) -> str:
        """The selected Python version"""
        return self._tool.get(
            "python-version", ".".join(map(str, sys.version_info[:2]))
        )

    @property
    def default_package_dir(self) -> Path:
        """
        Default directory to find or add mono-repo packages.
        If no directory is specified, will fallback to project root path
        """
        if len(self.package_paths) == 0:
            return self.path
        first_pkg_path = self.package_paths[0]
        if "*" or "?" in first_pkg_path.name:
            return first_pkg_path.parent
        return first_pkg_path

    def add_package_path(self, path: Path) -> None:
        """Add a package-containing directory path to the configuration"""
        relative_path = path.relative_to(self.path) if path.is_absolute() else path
        if relative_path.name != "*":
            relative_path = relative_path / "*"
        if (self.path / relative_path) in self.package_paths:
            return
        self._tool.setdefault("packages", []).append(relative_path.as_posix())
        TOMLFile(self.path / "pyproject.toml").write(self._pyproject)

    def add_explicit_package_path(self, package_path: Path) -> None:
        relative_path = (
            package_path.relative_to(self.path)
            if package_path.is_absolute()
            else package_path
        )
        if relative_path in self.package_paths:
            return
        self._tool.setdefault("packages", []).append(relative_path.as_posix())
        TOMLFile(self.path / "pyproject.toml").write(self._pyproject)

    def iter_packages(self) -> Iterable[PyPackage]:
        """Iterate over the packages in the monorepo"""
        from monas.project import PyPackage

        for p in self.package_paths:
            child_pkgs = list(p.parent.glob(p.name))
            for package in child_pkgs:
                if package.is_dir():
                    pypackage = PyPackage(self, package)
                    if pypackage.metadata.path.is_file():
                        yield pypackage


pass_config = click.make_pass_decorator(Config, ensure=True)
