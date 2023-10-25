"""qmatch
A collection of some astronomical match algorithms
By Dr Jie Zheng & Dr Lin-qiao Jiang
v0.11 2023-09-14
"""


from ._match_fast_ import findneighbor, match
from ._match_simple_ import match2d, offset1d
from ._match_triang_ import make_tri, match_triangle
from ._mean_offset_ import mean_xy, mean_offset1d, simu_mean
