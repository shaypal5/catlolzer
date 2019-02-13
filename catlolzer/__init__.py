"""An advanced cat lolzing engine."""

from .core import (  # noqa: F401
    CatLolzer,
    cheezburger,
)
import catlolzer.doge

del core
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
