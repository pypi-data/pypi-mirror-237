import tomllib  # noqa: I001
from pathlib import Path
from typing import Any


class Extractor:
    """A pyproject.toml dependency extractor."""

    def __init__(self, path: str | Path) -> None:
        """Initialize an Extractor.

        Args:
            path: Path to a project directory or pyproject.toml file.
        """
        self.path = path if isinstance(path, Path) else Path(path)
        self.data = self.load_toml(self.path)

    @property
    def all_dependencies(self) -> str:
        """Output all extracted dependencies."""
        all_dependencies = ""
        if self.base_dependencies:
            all_dependencies += self.base_dependencies
        if self.optional_dependencies:
            if all_dependencies:
                all_dependencies += "\n\n"
            all_dependencies += self.optional_dependencies
        return all_dependencies

    @property
    def base_dependencies(self) -> str:
        """Output the base project dependencies."""
        dependencies = self.data.get("project", {}).get("dependencies", [])
        if not dependencies:
            return ""
        return "\n".join(sorted(dependencies))

    @property
    def optional_dependencies(self) -> str:
        """Output the optional project dependencies."""
        optional_dependencies = ""
        for k, v in sorted(
            self.data.get("project", {}).get("optional-dependencies", {}).items()
        ):
            if optional_dependencies:
                optional_dependencies += "\n\n"
            sorted_dependencies = "\n".join(sorted(v))
            optional_dependencies += f"# [{k}]\n{sorted_dependencies}"
        return optional_dependencies

    @staticmethod
    def load_toml(path: str | Path) -> dict[str, Any]:
        """Load data from a TOML file.

        Args:
            path: Path to a TOML file.

        Returns:
            TOML data.
        """
        with open(path, "rb") as f:
            data = tomllib.load(f)
        return data
