import subprocess  # noqa: I001
from importlib.metadata import version
from pathlib import Path

import pytest

from depex import cli


def test_help():
    result = subprocess.run("depex --help", shell=True)
    assert result.returncode == 0


def test_version():
    result = subprocess.check_output("depex --version", shell=True, text=True)
    version_string = f"depex {version('depex')}\n"
    assert result == version_string


def test_no_arg():
    result = subprocess.run("depex", shell=True)
    assert result.returncode == 2


def test_bad_arg():
    result = subprocess.run("depex -z", shell=True)
    assert result.returncode == 2


def test_parsing_args_simple():
    args = cli.parse_args(["pyproject.toml", "--opts"])
    assert args.path
    assert isinstance(args.path, Path)
    assert args.opts


def test_parsing_args_complex():
    args = cli.parse_args([".", "--no-opts"])
    assert args.path
    assert isinstance(args.path, Path)
    assert not args.opts


def test_bad_project_path():
    return_code = cli.main(["pyproject.tomll"])
    assert return_code == 1


@pytest.mark.parametrize(
    "path,return_code",
    [
        ("pyproject.tomll", 1),
        (".", 1),
        ("test_project_directory", 0),
        ("test_pyproject_file", 0),
    ],
)
def test_path_arg(path: str, return_code: int, request: pytest.FixtureRequest):
    try:
        fp = str(request.getfixturevalue(path))
    except pytest.FixtureLookupError:
        fp = path
    return_code = cli.main([fp])
    assert return_code == return_code


def test_example_base_dependencies_output(
    test_pyproject_file: Path, base_dependencies_str: str
):
    result = subprocess.check_output(
        f"depex {str(test_pyproject_file)} --no-opts", shell=True, text=True
    )
    assert result == base_dependencies_str + "\n"


def test_example_optional_dependencies_output(
    test_pyproject_file: Path, optional_dependencies_str: str
):
    result = subprocess.check_output(
        f"depex {str(test_pyproject_file)} --opts", shell=True, text=True
    )
    assert result == optional_dependencies_str + "\n"


def test_example_all_dependencies_output(
    test_pyproject_file: Path,
    base_dependencies_str: str,
    optional_dependencies_str: str,
):
    result = subprocess.check_output(
        f"depex {str(test_pyproject_file)}", shell=True, text=True
    )
    assert result == base_dependencies_str + "\n\n" + optional_dependencies_str + "\n"
