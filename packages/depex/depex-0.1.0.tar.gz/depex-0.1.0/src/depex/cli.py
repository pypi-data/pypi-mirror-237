import sys
from argparse import ArgumentParser, BooleanOptionalAction, Namespace
from collections.abc import Sequence
from importlib.metadata import version
from pathlib import Path

from depex import Extractor


def parse_args(argv: Sequence[str] | None = None) -> Namespace:
    """Parse command line (cli) arguments.

    Args:
        argv: Command line arguments. Defaults to None.

    Returns:
        Parsed arguments.
    """
    parser = ArgumentParser(
        description="Extract Python project requirements from a `pyproject.toml` file.",
        epilog="Copyright 2023 Josh Duncan (joshbduncan.com)",
    )
    parser.add_argument(
        "path",
        type=Path,
        help="path to a project directory or pyproject.toml file",
    )
    parser.add_argument(
        "--opts",
        action=BooleanOptionalAction,
        help="include all dependencies",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('depex')}",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """Process command line (cli) arguments and output extracted dependencies.

    Args:
        argv: Command line arguments. Defaults to None.

    Returns:
        Exit code.
    """
    args = parse_args(argv)

    path: Path = (
        args.path.joinpath("pyproject.toml") if args.path.is_dir() else args.path
    )
    if not path.exists():
        print("Error: pyproject.toml file not found", file=sys.stderr)
        return 1
    extractor = Extractor(path)

    match args.opts:
        case True:
            print(extractor.optional_dependencies)
        case False:
            print(extractor.base_dependencies)
        case _:
            print(extractor.all_dependencies)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
