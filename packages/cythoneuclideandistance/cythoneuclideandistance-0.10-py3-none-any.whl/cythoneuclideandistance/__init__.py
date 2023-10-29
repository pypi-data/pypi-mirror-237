import os
import subprocess
import sys

import numexpr
import numpy as np


def _dummyimport():
    import Cython


try:
    from . import euclcython
except Exception as e:
    cstring = r"""# distutils: extra_compile_args=/openmp
# distutils: extra_link_args=/openmp
# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
# cython: binding=False
# cython: boundscheck=False
# cython: wraparound=False
# cython: initializedcheck=False
# cython: nonecheck=False
# cython: overflowcheck=False
# cython: overflowcheck.fold=False
# cython: embedsignature=False
# cython: embedsignature.format=c
# cython: cdivision=True
# cython: cdivision_warnings=False
# cython: cpow=True
# cython: c_api_binop_methods=True
# cython: profile=False
# cython: linetrace=False
# cython: infer_types=False
# cython: language_level=3
# cython: c_string_type=bytes
# cython: c_string_encoding=default
# cython: type_version_tag=True
# cython: unraisable_tracebacks=False
# cython: iterable_coroutine=True
# cython: annotation_typing=True
# cython: emit_code_comments=False
# cython: cpp_locals=True


cimport cython
import numpy as np
cimport numpy as np
import cython
from cython.parallel import prange

def cdistecl(np.int32_t[:] coords, np.int32_t[:] seq, np.float32_t[:] a, int num_coords, int num_seq, int width ):
    cdef int x0, y0, x1, y1
    cdef float di,aa,bb
    cdef int coord, element, h
    for coord in prange(0, num_coords-1, 1,nogil=True):
        x0 = coords[coord]
        y0 = coords[coord + 1]
        for element in range(0, num_seq, 1):
            if element % 2 !=0:
                continue
            x1 = seq[element]
            y1 = seq[element+1]
            aa=(x0 - x1)
            bb=(y0 - y1)
            di = ((aa*aa) + (bb*bb))
            h=(coord*width) + element
            h=h//2
            a[h] = di
    return 0"""
    pyxfile = f"euclcython.pyx"
    pyxfilesetup = f"euclcython_setup.py"

    dirname = os.path.abspath(os.path.dirname(__file__))
    pyxfile_complete_path = os.path.join(dirname, pyxfile)
    pyxfile_setup_complete_path = os.path.join(dirname, pyxfilesetup)

    if os.path.exists(pyxfile_complete_path):
        os.remove(pyxfile_complete_path)
    if os.path.exists(pyxfile_setup_complete_path):
        os.remove(pyxfile_setup_complete_path)
    with open(pyxfile_complete_path, mode="w", encoding="utf-8") as f:
        f.write(cstring)
    numpyincludefolder = np.get_include()
    compilefile = (
        """
	from setuptools import Extension, setup
	from Cython.Build import cythonize
	ext_modules = Extension(**{'py_limited_api': False, 'name': 'euclcython', 'sources': ['euclcython.pyx'], 'include_dirs': [\'"""
        + numpyincludefolder
        + """\'], 'define_macros': [], 'undef_macros': [], 'library_dirs': [], 'libraries': [], 'runtime_library_dirs': [], 'extra_objects': [], 'extra_compile_args': [], 'extra_link_args': [], 'export_symbols': [], 'swig_opts': [], 'depends': [], 'language': None, 'optional': None})

	setup(
		name='euclcython',
		ext_modules=cythonize(ext_modules),
	)
			"""
    )
    with open(pyxfile_setup_complete_path, mode="w", encoding="utf-8") as f:
        f.write(
            "\n".join(
                [x.lstrip().replace(os.sep, "/") for x in compilefile.splitlines()]
            )
        )
    subprocess.run(
        [sys.executable, pyxfile_setup_complete_path, "build_ext", "--inplace"],
        cwd=dirname,
        shell=True,
        env=os.environ.copy(),
    )
    from . import euclcython


def calculate_euc_distance(coords1, coords2):
    """
    Calculate Euclidean distances between two sets of coordinates.

    This function computes the Euclidean distance matrix between two sets of coordinates.

    Args:
        coords1 (numpy.ndarray): An array of shape (n, 2) containing the first set of coordinates.
        coords2 (numpy.ndarray): An array of shape (m, 2) containing the second set of coordinates.

    Returns:
        numpy.ndarray: A 2D array of shape (n, m) containing the Euclidean distances between all pairs of coordinates.

    Example:
        import random
        import cythoneuclideandistance
        import numpy as np

        coords1 = np.array(
            [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(23000)],
            dtype=np.int32,
        )
        coords2 = np.array(
            [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(22150)],
            dtype=np.int32,
        )

        distance_matrix = cythoneuclideandistance.calculate_euc_distance(coords1, coords2)
        print(distance_matrix)
    """
    if len(coords2) > len(coords1):
        coords1, coords2 = coords2, coords1
    min_array_len = min(len(coords1), len(coords2))
    len_coords1 = len(coords1)
    len_coords2 = len(coords2)
    array_coords1_flat = coords1.ravel()
    array_coords2_flat = coords2.ravel()

    len_array_coords2_flat = len(array_coords2_flat)
    len_array_coords1_flat = len(array_coords1_flat)
    a = np.zeros((len_coords1 * len_coords2), dtype=np.float32)
    euclcython.cdistecl(
        array_coords1_flat,
        array_coords2_flat,
        a,
        len_array_coords1_flat,
        len_array_coords2_flat,
        min_array_len,
    )
    numexpr.evaluate("sqrt(a)", out=a, global_dict={}, local_dict={"a": a})
    return a.reshape((len_coords1, len_coords2))
