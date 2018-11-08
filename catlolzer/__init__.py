"""An advanced cat lolzing engine."""

from .core import CatLolzer  # noqa: F401

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
