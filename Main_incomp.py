"""
:title: Python Code for Incomplete Two Balls with Non-negatively Curved Centre for Quartic Graphs
:authors:

"""

import ast
import copy
import CurvatureCalculator as curvature
from itertools import chain
from itertools import izip
from itertools import permutations
import numpy as np
from operator import itemgetter
import os


all_graphs = [[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 4], [2, 4], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 2, 4], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [1], [2], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [2, 4], [3, 4], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4], [1], [2]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1], [1], [2], [2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1], [2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1], [2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], []]],
[[[1, 1, 0, 0, 1, 0], [[1, 2, 3, 4], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 2, 3], [3], [4], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [2], [3], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[3, 4], [1], [2], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 2], [3, 4], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [2, 3], [4], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [2, 4], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [3, 4], [2], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [2, 3], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [3, 4], [2], [3]], []], [[1, 1, 0, 0, 1, 0], [[3, 4], [3, 4], [1], [2]], []], [[1, 1, 0, 0, 1, 0], [[1, 2, 3], [3, 4], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2, 3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2, 4], [3]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [3, 4], [2]], []], [[1, 1, 0, 0, 1, 0], [[1, 2, 3, 4], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 2], [3, 4], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [2, 4], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [2, 3], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2, 3, 4]], []]],
[[[1, 1, 1, 0, 0, 0], [[2, 3, 4], [2], [3], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2], [3], [4], [4]], []], [[1, 1, 1, 0, 0, 0], [[2], [2], [3], [3], [4], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2, 3], [4], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2, 4], [3], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3, 4], [2, 3], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2, 4], [3, 4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3, 4], [2, 3, 4]], []]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1], [2], [3], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2, 3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [3, 4], [3, 4], [1], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [3, 4], [1], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3], [2, 4], [3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [3]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 2], [2, 3], [3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 3], [2, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2, 4], [3]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [3, 4], [1]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [2, 3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [2, 3, 4]], []]],
[[[1, 1, 1, 1, 1, 0], [[3, 4]], []], [[1, 1, 1, 1, 1, 0], [[3], [4]], []]],
[[[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2], [3], [4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [2], [3], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 4], [3], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [3, 4], [2], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 4], [1], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 3], [4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [2, 4], [3], [3]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [3, 4], [2], [3]], []], [[1, 1, 0, 0, 0, 0], [[2, 3], [2, 4], [3, 4], [1], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 4], [2, 4], [3, 4], [1], [3]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 3, 4], [1], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3], [2, 4], [3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3], [3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 4], [3, 4], [3]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [3, 4], [3, 4], [2]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 2], [3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2, 3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2, 4], [3]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 4], [3, 4], [1]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 3, 4], [1, 4]], []]],
[[[1, 1, 1, 1, 0, 0], [[2, 3, 4], [4]], []], [[1, 1, 1, 1, 0, 0], [[2, 3], [4], [4]], []], [[1, 1, 1, 1, 0, 0], [[2, 4], [3], [4]], []], [[1, 1, 1, 1, 0, 0], [[2], [3], [4], [4]], []], [[1, 1, 1, 1, 0, 0], [[2, 4], [3, 4]], []]],
[[[1, 1, 0, 0, 1, 1], [[1, 2, 3, 4]], []], [[1, 1, 0, 0, 1, 1], [[1, 2, 3], [4]], []], [[1, 1, 0, 0, 1, 1], [[1, 2], [3], [4]], []], [[1, 1, 0, 0, 1, 1], [[1, 4], [2], [3]], []], [[1, 1, 0, 0, 1, 1], [[1], [2], [3], [4]], []], [[1, 1, 0, 0, 1, 1], [[1, 2], [3, 4]], []], [[1, 1, 0, 0, 1, 1], [[1, 4], [2, 3]], []]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3], [2], [4], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 2, 3], [4], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3], [2, 4], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [2, 4], [3]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2, 3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2], [3, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3, 4], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2, 3, 4]], []]],
[[[1, 1, 0, 1, 0, 0], [[1, 2, 3, 4], [4], [4]], []], [[1, 1, 0, 1, 0, 0], [[1, 4], [2, 4], [3], [4]], []], [[1, 1, 0, 1, 0, 0], [[1, 2, 4], [3, 4], [4]], []], [[1, 1, 0, 1, 0, 0], [[1, 4], [2, 4], [3, 4]], []]],
[[[1, 1, 1, 1, 1, 1], [], []]]]

def menu():
    run = True
    while run:
        try:
            print "\n\nMenu\n1. Generate latex document of all the graphs\n2. Give properties of a two ball\n3. Isomorphism checker\n4. Exit"
            input = raw_input("Select: ")
            # Generate latex document
            if input == "1":
                all_graphs = generate_incomp_twoballs()
                write_to_file(all_graphs)
                print "\n Successfully created latex file: /latex/classification.tex"
            # Give properties of a two ball
            elif input == "2":
                graph_in = raw_input("\nInput a two ball: ")
                graph = standardise(ast.literal_eval(graph_in))
                adjmatrix = adjmat(graph)
                curv = curvature.curv_calc(adjmatrix, 0)
                outdegree = outdeg(graph)
                s1out = s1_outreg(outdegree)
                curve_sharp = curv_sharp(curv, outdegree)
                print "\nCurvature: %11.3f\nS1 out-reg: %10s\nCurvature-sharp: %s" % (curv, s1out, curve_sharp)
            # Isomorphism Checker
            elif input == "3":
                input1 = raw_input("\nInput first two ball: ")
                graph1 = ast.literal_eval(input1)
                input2 = raw_input("Input second two ball: ")
                graph2 = ast.literal_eval(input2)
                print ""
                print iso(standardise(graph1), standardise(graph2))
            elif input == "4":
                print "Exiting"
                run = False
            else:
                print "\nInvalid input"
        except:
            print 'Error'
    return


# GET FUNCTIONS #
def get_oneballs(oneball=None):
    """ Get a one ball in standard form or, if no arguments are specified, a list of standard one balls.
    :param oneball: a single one ball (default [])
    :return: A one ball in standard form or a list of all standard one balls
    """
    # Dictionary of all the standard one balls and their equivalent representations
    oneball_dict = {(0, 0, 0, 0, 0, 0): [],
                    (1, 0, 0, 0, 0, 0): [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
                                         [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]],
                    (1, 0, 0, 0, 0, 1): [[0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0]],
                    (1, 1, 0, 0, 0, 0): [[1, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0],
                                         [0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1],
                                         [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1]],
                    (1, 1, 1, 0, 0, 0): [[1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 1]],
                    (1, 1, 0, 1, 0, 0): [[1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1]],
                    (1, 1, 0, 0, 1, 0): [[1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1],
                                         [0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 1],
                                         [0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]],
                    (1, 1, 0, 0, 1, 1): [[1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0]],
                    (1, 1, 1, 1, 0, 0): [[1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0],
                                         [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1],
                                         [1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1]],
                    (1, 1, 1, 1, 1, 0): [[1, 1, 1, 1, 0, 1], [1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1],
                                         [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]],
                    (1, 1, 1, 1, 1, 1): []}
    # If function was called without specifying any arguments, return list of all standard one balls
    if oneball is None:
        return map(list, oneball_dict.keys())
    # If one ball parameter is in standard form, return it
    if tuple(oneball) in oneball_dict.keys():
        return oneball
    # Otherwise, return the equivalent one ball in standard form
    for key in oneball_dict:
        if oneball in oneball_dict[key]:
            return list(key)


# SINGLE GRAPH FUNCTIONS #
def standardise(g):
    """ Standardises a graph by standardising the one ball, adding the leaves and sorting the two ball.
    :param g: graph
    :return: standardised graph
    """
    # STANDARDISE ONE BALL #
    g_new = standardise_oneball(g)

    # SORT TWO BALL #
    for vertex in g_new[1]:
        vertex.sort()
    # Create a data structure of a list of lists containing the two ball vertex and its connections
    two_ball_struct = []
    for i in range(len(g_new[1])):
        two_ball_struct.append([i + 5, g_new[1][i]])
    two_ball_struct.sort(key=lambda x: x[1][:])
    two_ball_struct.sort(key=lambda x: len(x[1]), reverse=True)
    # Create list of sorted two ball vertices
    two_ball_struct = list(izip(*two_ball_struct))
    g_new[1] = list(two_ball_struct[1])

    # ADD LEAVES #
    # Calculate number of existing connections
    out_degree = outdeg(g_new)
    radial_edges = chain.from_iterable(g_new[1])
    freq = [0, 0, 0, 0]  # Frequency of radial edges from each one ball vertex
    for edge in radial_edges:
        freq[edge - 1] += 1
    leaf_freq = np.subtract(out_degree, freq)
    for i in range(4):
        for j in range(leaf_freq[i]):
            g_new[1].append([i + 1])
    return g_new


def standardise_oneball(g):
    """ Standardises the one ball.
    :param g: graph
    :return: graph with standardised one ball
    """
    oneball_orig = g[0]
    oneball_std = get_oneballs(oneball_orig)
    # If orignial one ball is already a standard one ball, return graph
    if oneball_orig == oneball_std:
        return g

    # RELABEL VERTICES #
    # Create data structure, oneball_struct, containing original one ball and its connections
    oneball_sph_edges = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    oneball_struct = list(izip(oneball_sph_edges, oneball_orig))
    for i in range(6):
        oneball_struct[i] = list(oneball_struct[i])
    # Find permutation that maps the original one ball to the standard one ball
    perms = permutations([1, 2, 3, 4])
    for perm in perms:
        oneball_perm_struct = copy.deepcopy(oneball_struct)
        for i in range(6):
            for j in range(2):
                oneball_perm_struct[i][0][j] = perm[oneball_struct[i][0][j] - 1]
            oneball_perm_struct[i][0].sort()
        oneball_perm_struct.sort(key=lambda x: x[0][:])
        oneball_perm = []
        for i in range(6):
            oneball_perm.append(oneball_perm_struct[i][1])
        # If the permuted one ball is the same as the standardised one ball, relabel two ball vertices and return graph
        if oneball_perm == oneball_std:
            g[0] = oneball_std
            for vertex in g[1]:
                for i in range(len(vertex)):
                    vertex[i] = perm[vertex[i] - 1]
            for two_ball_vertex in g[1]:
                two_ball_vertex.sort()
            return g


def adjmat_oneball(oneball):
    """ Create adjacency submatrix for the one ball.
    :param oneball: the one ball
    :return: submatrix for the one ball
    """
    oneball_matrix = np.zeros((4, 4), dtype=int)
    i = (1, 1, 1, 2, 2, 3)
    j = (2, 3, 4, 3, 4, 4)
    for n in range(6):
        if oneball[n] == 1:
            oneball_matrix[i[n] - 1, j[n] - 1] = 1
            oneball_matrix[j[n] - 1, i[n] - 1] = 1
    return oneball_matrix


def adjmat(g):
    """ Creates the adjacency matrix for a graph.
    :param g: graph
    :return: adjacency matrix
    """
    g_new = g[0:2]
    num_vertices = 5 + len(g_new[1])
    adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
    # Edges from the center
    adj_matrix[0, 1:5] = 1
    adj_matrix[1:5, 0] = 1
    # Fill in one ball
    adj_matrix[1:5, 1:5] = adjmat_oneball(g_new[0])
    # Two ball radial edges
    for i in range(num_vertices - 5):
        vertex = g_new[1][i]
        for j in range(len(vertex)):
            adj_matrix[i + 5, vertex[j]] = 1
            adj_matrix[vertex[j], i + 5] = 1
    return adj_matrix


def outdeg(g):
    """ Creates a list of the out degrees for the one sphere.
    :param g: graph
    :return: list of the out degrees for the one sphere
    """
    j = (1, 1, 1, 2, 2, 3)
    k = (2, 3, 4, 3, 4, 4)
    out_degrees = [0, 0, 0, 0]
    for i in range(6):
        if g[0][i] == 0:
            out_degrees[j[i] - 1] += 1
            out_degrees[k[i] - 1] += 1
    return out_degrees


def curv_sharp(curv, out_degrees):
    """ Determines whether a graph is infinity curvature sharp using its curvature and out degrees.
    :param curv: curvature of the central vertex
    :param out_degrees: list of the out degrees for the one sphere
    :return: True if the graph is infinity curvature sharp
    """
    k = (7 - 0.25 * sum(out_degrees)) * 0.5  # Curvature bound
    if abs(curv - k) <= 1e-6:
        return True
    else:
        return False


def s1_outreg(out_degrees):
    """ Determines whether a graph is s1 out regular by checking if the one sphere out degrees are constant.
    :param out_degrees: list of the out degrees for the one sphere
    :return: True if the graph is s1 out regular
    """
    for i in range(1, 4):
        if out_degrees[i] != out_degrees[0]:
            return False
    return True


# ISOMORPHIC FUNCTIONS #
def get_oneball_perms(oneball):
    """ Returns a list of the permutations for a one ball that preserve its structure.
    :param oneball: one ball
    :return: permutations
    """
    all_oneball_perms = {(0, 0, 0, 0, 0, 0): [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2),
                                              (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3),
                                              (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1),
                                              (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1),
                                              (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2),
                                              (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)],
                         (1, 0, 0, 0, 0, 0): [(1, 2, 3, 4), (2, 1, 3, 4), (1, 2, 4, 3), (2, 1, 4, 3)],
                         (1, 0, 0, 0, 0, 1): [(1, 2, 3, 4), (2, 1, 3, 4), (1, 2, 4, 3), (2, 1, 4, 3),
                                              (3, 4, 1, 2), (4, 3, 1, 2), (3, 4, 2, 1), (4, 3, 2, 1)],
                         (1, 1, 0, 0, 0, 0): [(1, 2, 3, 4), (1, 3, 2, 4)],
                         (1, 1, 1, 0, 0, 0): [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4),
                                              (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2)],
                         (1, 1, 0, 1, 0, 0): [(1, 2, 3, 4), (1, 3, 2, 4), (2, 1, 3, 4),
                                              (2, 3, 1, 4), (3, 1, 2, 4), (3, 2, 1, 4)],
                         (1, 1, 0, 0, 1, 0): [(1, 2, 3, 4), (2, 1, 4, 3)],
                         (1, 1, 0, 0, 1, 1): [(1, 2, 3, 4), (2, 4, 1, 3), (4, 3, 2, 1), (3, 1, 4, 2)],
                         (1, 1, 1, 1, 0, 0): [(1, 2, 3, 4), (1, 3, 2, 4)],
                         (1, 1, 1, 1, 1, 0): [(1, 2, 3, 4), (1, 2, 4, 3), (2, 1, 3, 4), (2, 1, 4, 3)]}
    return all_oneball_perms[tuple(oneball)]


def iso(g1, g2):
    """ Determines whether two graphs are isomorphic.
    :param g1: graph one
    :param g2: graph two
    :param fix_center: True if the centers are fixed (default False)
    :return: True if the graphs are isomorphic
    """
    # If graphs are identical, return True
    if g1 == g2:
        return True
    # If number of vertices differ, return False
    num_vertices = 5 + len(g1[1])
    if num_vertices != 5 + len(g2[1]):
        return False

    # PRELIMINARY CHECKS #
    # If one balls are the same, continue checks
    if g1[0] == g2[0]:
        oneball_perms = get_oneball_perms(g2[0])
        for perm in oneball_perms:
            g2_new = copy.deepcopy(g2)
            for twoball_vertex in g2_new[1]:
                for i in range(len(twoball_vertex)):
                    twoball_vertex[i] = perm[twoball_vertex[i] - 1]
                twoball_vertex.sort()
            g2_new[1].sort(key=lambda x: x[:])
            g2_new[1].sort(key=len, reverse=True)
            if g2_new[2]:
                # Create a data structure of a list of lists containing the two ball vertex and its connections
                two_ball_struct = []
                for i in range(len(g2_new[1])):
                    two_ball_struct.append([i + 5, g2_new[1][i]])
                two_ball_struct.sort(key=lambda x: x[1][:])
                two_ball_struct.sort(key=lambda x: len(x[1]), reverse=True)
                # Create list of sorted two ball vertices
                two_ball_struct = list(izip(*two_ball_struct))
                g2_new[1] = list(two_ball_struct[1])
            if g1 == g2_new:
                return True
    return False


# GRAPH GENERATING FUNCTIONS #
def partition(n, num_unsat_vert, avail_outdeg_max):
    """ Returns a list of partitions of an integer that satisfies the conditions.
    :param n: integer to be partitioned
    :param num_unsat_vert: number of unsaturated vertices in the one sphere
    :param avail_outdeg_max: maximum available out degree
    :return: list of partitions of integer n
    """
    m = [[n]]
    for x in range(1, n):
        for y in partition(n - x, num_unsat_vert, avail_outdeg_max):
            s = sorted([x] + y, reverse=True)
            if s not in m:
                m.append(s)
    return m


def generate_twoball(avail_outdeg, part, twoball, all_twoballs, vertices):
    """ Recursively generates all two balls for a specific one ball.
    :param avail_outdeg: available outdegrees
    :param part: current partition
    :param twoball: current two ball
    :param all_twoballs: list of all the two balls for the specific one ball
    :param vertices: list of available vertices with multiplicity
    :return: None
    """
    # Tail of recursion is reached when part is empty, therefore current two sphere is complete
    if not part:
        if twoball not in all_twoballs:
            twoball.append([])
            all_twoballs.append(twoball)
        return
    # Tail of recursion is also reached when there are only leaves left
    if part[0] == 1:
        twoball_new = copy.deepcopy(twoball)
        for i in range(4):
            for j in range(avail_outdeg[i]):
                if len(twoball_new) == 1:
                    twoball_new.append([[i + 1]])
                else:
                    twoball_new[1].append([i + 1])
        if twoball_new not in all_twoballs:
            twoball_new.append([])
            all_twoballs.append(twoball_new)
        return
    # Generating a radial edge
    p = part[0]
    part_new = part[1:]
    for a in vertices[p - 2]:
        valid = True
        avail_outdeg_new = copy.deepcopy(avail_outdeg)
        for i in a:
            if avail_outdeg[i - 1] == 0:
                valid = False
            avail_outdeg_new[i - 1] -= 1
        # If radial edge is valid, add it to the current two ball and repeat to generate the next edge
        if valid:
            twoball_new = copy.deepcopy(twoball)
            if len(twoball_new) == 1:
                twoball_new.append([a])
            else:
                twoball_new[1] = twoball_new[1] + [a]
            generate_twoball(avail_outdeg_new, part_new, twoball_new, all_twoballs, vertices)
    return


def generate_incomp_twoballs():
    """ Generates all incomplete two balls with non-negative curvature grouped by one ball
    :return: list of lists of two balls
    """
    oneballs = get_oneballs()
    vertices = [[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
                [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]],
                [[1, 2, 3, 4]]]
    twoballs_incomp = []
    for oneball in oneballs[:-1]:
        avail_outdeg = outdeg([oneball, [], []])
        # Calculate number of unsaturated vertices
        num_unsat_vert = 0
        for i in range(4):
            if avail_outdeg[i] != 0:
                num_unsat_vert += 1
        # Get list of valid partitions
        n = sum(avail_outdeg)
        parts = partition(n, num_unsat_vert, max(avail_outdeg))
        # Create list of valid partitions
        parts_new = []
        avail_outdeg_max = max(avail_outdeg)
        for part in parts:
            part_len = len(part)
            part_max = max(part)
            if part_max <= num_unsat_vert and avail_outdeg_max <= part_len:
                parts_new.append(part)
        twoballs_incomp_oneball = []  # All incomplete two balls for a specific one ball
        # Generate two ball for each partition
        for part in parts_new:
            twoball = [oneball]
            all_twoballs = []
            generate_twoball(avail_outdeg, part, twoball, all_twoballs, vertices)
            # Set first non-negative two ball as first unique two ball
            unique_twoballs = []
            first_twoball_index = 0
            for i in range(len(all_twoballs)):
                curv = curvature.curv_calc(adjmat(all_twoballs[i]), 0)
                if curv >= 0:
                    first_twoball_index = i + 1
                    all_twoballs[i][1].sort(key=lambda x: x[:])
                    all_twoballs[i][1].sort(key=len, reverse=True)
                    unique_twoballs = [all_twoballs[i]]
                    break
            # If there are no non-negative two balls, skip to next partition
            if unique_twoballs:
                # Remove isomorphisms
                for graph1 in all_twoballs[first_twoball_index:]:
                    # If graph is non-negative check if it is unique
                    curv = curvature.curv_calc(adjmat(graph1), 0)
                    if curv >= 0:
                        isomorphic = False
                        graph1[1].sort(key=lambda x: x[:])
                        graph1[1].sort(key=len, reverse=True)
                        for graph2 in unique_twoballs:
                            if iso(graph1, graph2):
                                isomorphic = True
                                break
                        # If graph is unique add it
                        if not isomorphic:
                            unique_twoballs.append(graph1)
                for twoball in unique_twoballs:
                    twoball[1].sort(key=len, reverse=True)
                twoballs_incomp_oneball += unique_twoballs
        twoballs_incomp.append(twoballs_incomp_oneball)
    twoballs_incomp.append([[[1, 1, 1, 1, 1, 1], [], []]])
    return twoballs_incomp


def generate_curv_sharp_twoballs(all_twoballs):
    """

    :param all_twoballs: list of incomplete two balls
    :return: list of two balls that have curvature sharp centres
    """
    curv_sharp_graphs = []
    for oneball in all_twoballs:
        k = (7 - 0.25 * sum(outdeg(oneball[0]))) * 0.5
        for twoball in oneball:
            if abs(curvature.curv_calc(adjmat(twoball),0)-k) <= 1e-6:
                curv_sharp_graphs.append(twoball)
    return curv_sharp_graphs


# CREATE LATEX FILE #
def write_to_file(all_graphs):
    """ Creates the latex document, '/latex/classification.tex' summarising the incomplete two balls
    :param all_graphs: graphs to be listed in document
    :return: none
    """
    # Tikz drawings of the one balls
    oneball_images = ['\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v3) edge[red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v3) edge[red] (v4)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}',
                     '\\draw(v0) -- (v1)\n'
                     '\t(v0) -- (v2)\n'
                     '\t(v0) -- (v3)\n'
                     '\t(v0) -- (v4)\n'
                     '\t(v1) edge[red] (v2)\n'
                     '\t(v2) edge[red] (v3)\n'
                     '\t(v3) edge[red] (v4)\n'
                     '\t(v4) edge[red] (v1)\n'
                     '\t(v1) edge[bend left, red] (v3)\n'
                     '\t(v2) edge[bend left, red] (v4)[thick];\n'
                     '\\end{tikzpicture}']

    # POPULATE TABLES WITH VALUES #
    index = 1
    all_tables = []
    curvature_sharp_table = []
    for i, oneball_graphs in enumerate(all_graphs):
        table = []
        oneball = oneball_graphs[0][0]
        outdegree = outdeg([oneball])
        s1out = s1_outreg(outdegree)
        k = (7 - 0.25 * sum(outdegree)) * 0.5
        for graph in oneball_graphs:
            curv = curvature.curv_calc(adjmat(graph), 0)
            curvature_sharp = curv_sharp(curv, outdegree)
            table.append([graph[1:], curv, curvature_sharp])
            table.sort(key=itemgetter(1), reverse=True)
        for j, line in enumerate(table):
            line.insert(0, str(i+1) + "." + str(j+1))
            index += 1
            if line[3]:
                curvature_sharp_line = copy.deepcopy(line[:-1])
                curvature_sharp_line[1].insert(0, oneball)
                curvature_sharp_table.append(curvature_sharp_line)
        all_tables.append([str(oneball), s1out, k, table])

    # CREATE TEX FILE #
    if not os.path.exists('latex'):
        os.makedirs('latex')
    f = open('latex/classification.tex', 'w')
    # Front page and abstract
    f.write('\\documentclass[11pt, oneside]{article}\n'
            '\\usepackage{geometry}\n'
            '\\geometry{a4paper, margin = 1in}\n'
            '\\usepackage[parfill]{parskip}\n'
            '\\usepackage{graphicx}\n'
            '\\graphicspath{ {/latex/} }\n'
            '\\usepackage{wrapfig}\n'
            '\\usepackage{tikz}\n'
            '\\usepackage{amssymb}\n\n'
            '\\title{Incomplete Two Balls with Non-negatively Curved Centre for Quartic Graphs}\n'
            '\\author{Leyna Watson May}\n'
            '\\date{}\n'
            '\\begin{document}\n'
            '\\maketitle\n'
            '\\begin{abstract}'
            'This document contains the 204 incomplete two balls with non-negative curvature at their centres, separated by structure of the one ball. '
            'Additionally, it contains the 22 two balls with infinity curvature sharp centres. '
            'The 11 one ball structures and relevant properties are summarised below.\n\n'
            '\\end{abstract}'
            '\\vspace{1cm}\n'
            '\\begin{center}\n'
            '\\begin{tabular}{| l | l | l | p{3.1cm} | p{3.7cm} |}\n'
            '\\hline\n'
            'Index & One Ball & S1 Out-regular & Bakry-\\\'Emery Curvature Bound, \\begin{math}\\kappa _\\infty \\end{math} & Total Number of Non-negative Two Balls\\\\ \\hline\n')
    for i, oneball_table in enumerate(all_tables):
        f.write('%i & %s & %s & %.3f & %s \\\\ \\hline\n' % (i+1, oneball_table[0], oneball_table[1], oneball_table[2], len(oneball_table[3])))
    f.write('\\end{tabular}\n'
            '\\end{center}\n'
            '\\newpage\n')

    # CREATE CONTENTS #
    index = 1
    n = 0
    for oneball_table in all_tables:
        # Start a new section with drawing and make table
        f.write('\\section{%s}\n\n'
                'S1 Out-regular: %s\n\n'
                'Curvature Bound: %.3f\n\n'
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=2]\n'
                '\\tikzstyle{every node}=[draw, shape=circle, scale = 0.9, thick]\n'
                '\\path(1:0cm)\tnode(v0) [fill, text = white]{$v_0$};\n'
                '\\path(180:1cm)\tnode(v1) [fill = red, red, text =white]{$v_1$};\n'
                '\\path(90:1cm)\tnode(v2) [fill = red, red, text =white]{$v_2$};\n'
                '\\path(0:1cm)\tnode(v3) [fill = red, red, text =white]{$v_3$};\n'
                '\\path(270:1cm)\tnode(v4) [fill = red, red, text =white]{$v_4$};\n\n'
                '%s\n\n'
                '\\vspace{1cm}\n'
                '\\begin{tabular}{| l | p{8cm} | l | l |}\n'
                '\\hline\n'
                'Index & Two Sphere & Curvature & Curvature Sharp \\\\ \\hline\n'
                % (oneball_table[0], oneball_table[1], oneball_table[2], oneball_images[n]))
        n += 1
        # Write values to the table
        table_len = 1
        for table_line in oneball_table[3]:
            f.write('%s & %s & %.3f & %s \\\\ \\hline\n' % (table_line[0], str(table_line[1]), table_line[2], table_line[3]))
            if table_len % 32 == 0:
                f.write('\\end{tabular}\n'
                        '\\end{center}\n'
                        '\\newpage\n'
                        '\\begin{center}\n'
                        '\\begin{tabular}{| l | p{8cm} | l | l |}\n'
                        '\\hline\n'
                        'Index & Two Sphere & Curvature & Curvature Sharp \\\\ \\hline\n')
                table_len = 0
            table_len += 1
            index += 1
        f.write('\\end{tabular}\n'
                '\\end{center}\n'
                '\\newpage\n')
    # Create page containing the curvature sharp graphs
    f.write('\\setcounter{secnumdepth}{0}'
            '\\section{Curvature Sharp Graphs}\n\n'
            'Total: %i\n\n'
            '\\vspace{1cm}\n'
            '\\begin{center}\n'
            '\\begin{tabular}{|l|l|l|}\n'
            '\\hline\n'
            'Index & Two Ball & Curvature\\\\ \\hline\n' % len(curvature_sharp_table))
    for graph in curvature_sharp_table:
        f.write('%s & %s & %.3f\\\\ \\hline\n' % (graph[0], graph[1], graph[2]))
    f.write('\\end{tabular}\n'
            '\\end{center}\n'
            '\\end{document}')
    f.close()

menu()