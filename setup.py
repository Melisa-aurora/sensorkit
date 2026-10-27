"""Cythonization config for sensorkit.

The package is plain Python. This file declares how it is compiled:
each module below is cythonized (Cython pure-Python mode, .py -> .c) and
built as a native extension. The pure-Python __init__.py is shipped unchanged.

Build:
    pip install "Cython>=3.0" setuptools wheel
    python setup.py build_ext --inplace
"""

from Cython.Build import cythonize
from setuptools import Extension, setup

# Modules to cythonize.
CYTHON_MODULES = [
    "sensorkit.filters",
    "sensorkit.checksum",
    "sensorkit.control",
]

# Cython compiler directives applied to every module.
CYTHON_DIRECTIVES = {
    "language_level": "3",
    "boundscheck": False,
    "wraparound": False,
    "cdivision": True,
    "infer_types": True,
}

extensions = [
    Extension(
        name,
        sources=["src/" + name.replace(".", "/") + ".py"],
    )
    for name in CYTHON_MODULES
]

setup(
    ext_modules=cythonize(extensions, compiler_directives=CYTHON_DIRECTIVES),
)
