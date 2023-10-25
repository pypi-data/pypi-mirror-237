from pathlib import Path
from typing import Generator

import pytest

from depex import Extractor


@pytest.fixture
def base_dependencies() -> list[str]:
    return ["dep-a", "dep-c>=1.5.0", "dep-d==3.2.1"]


@pytest.fixture
def base_dependencies_str(base_dependencies) -> str:
    return "\n".join(sorted(base_dependencies))


@pytest.fixture
def optional_dependencies() -> dict[str, list[str]]:
    return {"opts1": ["opts1-a"], "opts2": ["opts2-a==1.5.0", "opts2-b>=2.0.0"]}


@pytest.fixture
def optional_dependencies_str(optional_dependencies) -> str:
    optional_dependencies_str = ""
    for k, v in optional_dependencies.items():
        if optional_dependencies_str:
            optional_dependencies_str += "\n\n"
        sorted_dependencies = "\n".join(v)
        optional_dependencies_str += f"# [{k}]\n{sorted_dependencies}"
    return optional_dependencies_str


@pytest.fixture
def example_pyproject_toml_string(
    base_dependencies: list[str], optional_dependencies: dict[str, list[str]]
) -> str:
    optional_dependencies_str = ""
    for k, v in optional_dependencies.items():
        optional_dependencies_str += f"{k} = {v}\n"
    return f"""[project]
name = "example-project"
version = "0.1.0"
description = "Example pyproject.toml file."
dependencies = {base_dependencies}

[project.optional-dependencies]
{optional_dependencies_str}
"""


@pytest.fixture
def test_project_directory(
    tmp_path: Generator[Path, None, None]
) -> Generator[Path, None, None]:
    return tmp_path


@pytest.fixture
def test_pyproject_file(
    test_project_directory: Path, example_pyproject_toml_string: str
) -> Path:
    fp = test_project_directory.joinpath("pyproject.toml")
    with open(fp, "w") as f:
        f.write(example_pyproject_toml_string)
    return fp


@pytest.fixture
def test_extractor_object(test_pyproject_file: Path) -> Extractor:
    return Extractor(test_pyproject_file)
