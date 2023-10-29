import os
import typing

try:
    if not typing.TYPE_CHECKING:
        from ._msvc_module_d import *
        from ._msvc_module_d import __version__
    else:
        from ._msvc_module import *
        from ._msvc_module import __version__
except ModuleNotFoundError:
    pass