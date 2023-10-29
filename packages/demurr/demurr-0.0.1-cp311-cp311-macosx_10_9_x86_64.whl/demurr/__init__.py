"A parser/demangler for decorated Visual C++ names using LLVM"

__version__ = '0.0.1'

try:
    from .msvc import *
except ImportError:
    pass
