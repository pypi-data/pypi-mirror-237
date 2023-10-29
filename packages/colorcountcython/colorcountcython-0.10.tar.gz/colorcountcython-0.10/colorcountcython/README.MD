# This module provides functionality to count unique colors in an image represented as a NumPy array and, optionally, group their coordinates.

## Tested against Windows / Python 3.11 / Anaconda

## pip install colorcountcython

```python

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


```