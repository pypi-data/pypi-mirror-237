import os
import subprocess
import sys
import numpy as np


def _dummyimport():
    import Cython


try:
    from . import allcolorcountcython
except Exception as e:
    cstring = r"""# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
# cython: binding=False
# cython: boundscheck=False
# cython: wraparound=False
# cython: initializedcheck=False
# cython: nonecheck=False
# cython: overflowcheck=True
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
from collections import defaultdict

cpdef searchallcolors(unsigned char[:] pic, int totallengthpic, int width, int withcoords, int withcount):
	cdef my_dict = defaultdict(int)
	cdef my_dict1 = defaultdict(list)
	cdef my_dict12={}
	cdef int x,y
	cdef int i
	cdef unsigned char r,g,b
	for i in range(0, totallengthpic, 3):
		b = pic[i]
		g = pic[i + 1]
		r = pic[i + 2]
		if withcount:
			my_dict[(r,g,b)]+=1
		if withcoords:
			x=((i % width)//3)
			y=(i // width)
			my_dict1[(r,g,b)].append((x,y))
	if withcount:
		my_dict12['color_count']=my_dict
	if withcoords:
		my_dict12['color_coords']=my_dict1
		#for keys in my_dict1.keys():
			#my_dict12['color_coords'][keys] = np.array(my_dict12['color_coords'][keys],dtype=np.int32)
	return my_dict12"""
    pyxfile = f"allcolorcountcython.pyx"
    pyxfilesetup = f"locatepixelcolorcompiled_setup.py"

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
	ext_modules = Extension(**{'py_limited_api': False, 'name': 'allcolorcountcython', 'sources': ['allcolorcountcython.pyx'], 'include_dirs': [\'"""
        + numpyincludefolder
        + """\'], 'define_macros': [], 'undef_macros': [], 'library_dirs': [], 'libraries': [], 'runtime_library_dirs': [], 'extra_objects': [], 'extra_compile_args': [], 'extra_link_args': [], 'export_symbols': [], 'swig_opts': [], 'depends': [], 'language': None, 'optional': None})

	setup(
		name='allcolorcountcython',
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
    from . import allcolorcountcython


def colorcount(pic, coords=True, count=True):
    """

    This module provides functionality to count unique colors in an image represented as a NumPy array and, optionally, group their coordinates. It includes a Cython-based implementation for improved performance.

    Functions:
    - colorcount(pic, coords=True, count=True):
      Count the unique colors in an image represented as a NumPy array. If `coords` is set to True, it also groups the coordinates of each color.

    Internal Functions:
    - _dummyimport():
      Internal function to check the availability of Cython.
    - searchallcolors(pic, totallengthpic, width, withcoords, withcount):
      Cython function to count colors in an image and, if specified, group their coordinates.

    Parameters:
    - pic (ndarray): The input image represented as a NumPy array.
    - coords (bool): If True, the function will return the coordinates of each unique color.
    - count (bool): If True, the function will return the count of each unique color.

    Returns:
    A dictionary containing unique color information. If `coords` is True, it includes the coordinates of each color. If `count` is True, it includes the count of each color.

    Note:
    The `colorcount` function takes an image as input and returns a dictionary containing color counts and, if specified, color coordinates. The Cython-based implementation in this module enhances the performance of color counting.

    Example:
        from a_cv_imwrite_imread_plus import open_image_in_cv
        from colorcountcython import colorcount
        b=open_image_in_cv('c:\\tetetete.png')
        d=colorcount(pic=b,coords=True, count=True)
        print(d)

    """

    width = pic.shape[1] * 3
    if pic.dtype != np.uint8:
        pic = pic.astype(np.uint8)
    if pic.shape[-1] > 3:
        pic = pic[:, :, :3]
    fl = pic.flatten()
    return allcolorcountcython.searchallcolors(
        fl, len(fl), width, int(coords), int(count)
    )
