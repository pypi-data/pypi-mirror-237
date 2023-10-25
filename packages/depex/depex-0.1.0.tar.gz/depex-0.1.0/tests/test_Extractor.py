from pathlib import Path

from depex import Extractor


def test_init(tmp_path: Path):
    fp = tmp_path.joinpath("test.toml")
    fp.touch()
    e = Extractor(fp)
    assert e.path
    assert not e.data


def test_load_toml(test_pyproject_file: Path):
    fp = test_pyproject_file
    assert fp.exists()
    e = Extractor(fp)
    assert e.path
    assert e.data


def test_example_base_dependencies_output(
    test_extractor_object: Extractor, base_dependencies_str: str
):
    assert test_extractor_object.base_dependencies == base_dependencies_str


def test_example_optional_dependencies_output(
    test_extractor_object: Extractor, optional_dependencies_str: str
):
    assert test_extractor_object.optional_dependencies == optional_dependencies_str


def test_example_all_dependencies_output(
    test_extractor_object: Extractor,
    base_dependencies_str: str,
    optional_dependencies_str: str,
):
    assert (
        test_extractor_object.all_dependencies
        == base_dependencies_str + "\n\n" + optional_dependencies_str
    )
