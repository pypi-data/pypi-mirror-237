from .extractor import Extractor

__all__ = ["__version__", "Extractor"]


def __getattr__(name: str) -> str:
    """Lazily get the version when needed."""

    if name == "__version__":
        from importlib.metadata import version

        return version("depex")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
