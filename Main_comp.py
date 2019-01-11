"""
:title: Python Code for Incomplete Two Balls with Non-negatively Curved Centre for Quartic Graphs
:authors: Francis Gurr and Leyna Watson May

"""

import ast
import copy
import CurvatureCalculator as curvature
from itertools import chain
from itertools import combinations
from itertools import izip
from itertools import permutations
from itertools import repeat
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
            print "\nOops! Something went wrong"
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
    # Relabel and sort the two sphere spherical edges
    for edge in g_new[2]:
        for i in range(2):
            edge[i] = two_ball_struct[0].index(edge[i]) + 5
        edge.sort()
    g_new[2].sort(key=lambda x: x[1])
    g_new[2].sort(key=lambda x: x[0])

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

    # SORT TWO SPHERE SPHERICAL EDGES #
    g_new[2].sort(key=lambda x: x[:])
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
    # If there are spherical edges add them to the matrix
    if g[2]:
        for sph_edge in g[2]:
            adj_matrix[sph_edge[0], sph_edge[1]] = 1
            adj_matrix[sph_edge[1], sph_edge[0]] = 1
    return adj_matrix


def curvatures(g):
    """ Creates a list of lists of vertex and corresponding curvature.
    :param g: graph
    :return: list of lists of vertex and corresponding curvature
    """
    adj_matrix = adjmat(g)
    curvatures = []
    for i in range(5 + len(g[1])):
        curv = round(curvature.curv_calc(adj_matrix, i), 3)
        curvatures.append([i, curv])
    return curvatures


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


def diam_less_than_two(g):
    """ Determines whether a graph has a diameter of less than two.
    :param g: graph
    :return: True if the graph has a diameter of less than two
    """
    adj_matrix = adjmat(g)
    matrix = adj_matrix + np.matmul(adj_matrix, adj_matrix)
    length = len(adj_matrix)
    for i in range(length):
        for j in range(length):
            if matrix[i][j] <= 0:
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


def recenter(g, x):
    """ Recenter the graph about a vertex.
    :param g: graph
    :param x: new central vertex
    :return: recentered graph
    """
    adj_matrix = adjmat(g)
    # If original center is given, return graph
    if x == 0:
        return g
    # Otherwise get the new one ball, two sphere and two ball vertices
    oneball_vertices = [x] + curvature.one_sphere(adj_matrix, x)  # List of new one ball vertices
    twosphere_vertices = curvature.two_sphere(adj_matrix, x)  # List of new two sphere vertices
    twoball_vertices = oneball_vertices + twosphere_vertices  # List of vertices contained in the new two ball
    # If the new two ball does not contain all of the original vertices, i.e has a diameter > 2, raise an exception
    if len(twoball_vertices) != len(adj_matrix):
        return None

    # ONE BALL NOTATION #
    g_new = [[0, 0, 0, 0, 0, 0], [], []]
    vertices_a = (1, 1, 1, 2, 2, 3)
    vertices_b = (2, 3, 4, 3, 4, 4)
    for n in range(6):
        vertex_a = oneball_vertices[vertices_a[n]]
        vertex_b = oneball_vertices[vertices_b[n]]
        if adj_matrix[vertex_a, vertex_b] == 1:
            g_new[0][n] = 1

    # TWO BALL NOTATION #
    for i in range(len(twosphere_vertices)):
        radial_edges = []
        for j in range(1, len(oneball_vertices)):
            if adj_matrix[twosphere_vertices[i], oneball_vertices[j]] == 1:
                radial_edges.append(j)
        g_new[1].append(radial_edges)

    # SPHERICAL EDGE NOTATION #
    for i in range(5, len(twoball_vertices)):
        for j in range(i + 1, len(twoball_vertices)):
            if adj_matrix[twoball_vertices[i], twoball_vertices[j]] == 1:
                g_new[2].append([i, j])

    # STANDARDISE #
    g_new = standardise_oneball(g_new)
    return g_new


def iso(g1, g2, fix_center=False):
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

    if not fix_center:
        curv1 = curvature.curv_calc(adjmat(g1), 0)
        curvs2 = curvatures(g2)

    g2_center = num_vertices
    original_g2 = g2
    exit_flag = True
    while exit_flag:

        # PRELIMINARY CHECKS #
        # If one balls are the same, continue checks
        if g1[0] == g2[0]:
            # If number of spherical edges are the same, continue
            if len(g1[2]) == len(g2[2]):
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
                        # Relabel and sort the two sphere spherical edges
                        for edge in g2_new[2]:
                            for i in range(2):
                                edge[i] = two_ball_struct[0].index(edge[i]) + 5
                            edge.sort()
                        g2_new[2].sort(key=lambda x: x[:])
                    if g1 == g2_new:
                        return True

        # RECENTERING #
        # Recenter unless only comparing graphs with fixed centers
        exit_flag = False
        if not fix_center:
            for i in range(g2_center - 1, 0, -1):
                # If the curvatures are the same recenter around the new vertex
                if curv1 == curvs2[i][1]:
                    g2 = recenter(original_g2, i)
                    if g2 is not None:
                        g2_center = i
                        exit_flag = True
                        break
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
                            if iso(graph1, graph2, True):
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
    curv_sharp_graphs = []
    for oneball in all_twoballs:
        k = (7 - 0.25 * sum(outdeg(oneball[0]))) * 0.5
        for twoball in oneball:
            if abs(curvature.curv_calc(adjmat(twoball),0)-k) <= 1e-6:
                curv_sharp_graphs.append(twoball)
    return curv_sharp_graphs


def complete_twoball(g):
    """ Generates completions of a two ball by adding spherical edges.
    :param g: incomplete two ball
    :return: list of completed graphs
    """
    # If there is no two sphere, return g
    if not g[1]:
        return g
    else:
        g_new = copy.deepcopy(g)
        twoball_vertices = len(g_new[1])
        degrees = []
        unsat_vertices = []  # Unsaturated vertices in the two sphere
        # Create list of degrees and unsaturated vertices
        for j in range(twoball_vertices):
            deg = 4 - len(g_new[1][j])
            degrees.append(deg)
            if deg != 0:
                unsat_vertices.append(5 + j)
        degrees.sort(reverse=True)
        unsat_vertices.sort(reverse=True)
        # Generate spherical edges
        complete_graphs = []
        generate_sph_edges(degrees, unsat_vertices, complete_graphs, g_new)
        # Sort graphs
        sorted_graphs = []
        for graph in complete_graphs:
            graph[2].sort(key=lambda x: x[:])
            sorted_graphs.append(graph)
        # Set first non-negative two ball as first unique two ball
        unique_twoballs = []
        first_twoball_index = 0
        for i in range(len(complete_graphs)):
            curv = curvatures(complete_graphs[i])
            only_curvatures = list(izip(*curv))[1]
            if min(only_curvatures) >= 0:
                first_twoball_index = i + 1
                complete_graphs[i][2].sort(key=lambda x: x[:])
                unique_twoballs = [complete_graphs[i]]
                break
        # Remove isomorphisms
        for graph1 in complete_graphs[first_twoball_index:]:
            # If graph is non-negative check if it is unique
            curv = curvatures(graph1)
            only_curvatures = list(izip(*curv))[1]
            if min(only_curvatures) >= 0:
                graph1[2].sort(key=lambda x: x[:])
                isomorphic = False
                for graph2 in unique_twoballs:
                    if iso(graph1, graph2, True):
                        isomorphic = True
                        break
                # If graph is unique add it
                if not isomorphic:
                    unique_twoballs.append(graph1)
        return unique_twoballs


def generate_sph_edges(degrees, unsat_vertices, complete_graphs, g):
    """ Recursively generates the spherical edges one vertex at a time.
    :param degrees: list of the degrees of two sphere vertices
    :param unsat_vertices: unsaturated vertices in the two sphere
    :param complete_graphs: list of completions of the graph
    :param g: incomplete two ball
    :return: None
    """
    # Tail of recursion is reached when all vertices are saturated
    if not unsat_vertices:
        complete_graphs.append(g)
        return
    # Find possible vertex saturations for first unsaturated vertex
    subsets = list(combinations(unsat_vertices[1:], degrees[0]))
    vertex_saturation = []
    for comb in subsets:
        vertex_saturation.append(list(comb))
    # Adding spherical edges and repeat with updated values
    if vertex_saturation != [[]]:
        for choice in vertex_saturation:
            deg_new = degrees[1:]
            vert_new = unsat_vertices[1:]
            g_new = copy.deepcopy(g)
            for i in choice:
                g_new[2].append([i, unsat_vertices[0]])
                deg_new[-(i - 4)] -= 1
                if deg_new[-(i - 4)] == 0:
                    vert_new.remove(i)
            generate_sph_edges(deg_new, vert_new, complete_graphs, g_new)
    return


def generate_non_neg_twoballs():
    """ Generates all non-negatively curved four regular two balls and a list of their curvatures.
    :return: list of non-negative two balls and corresponding curvatures
    """
    # Generate incomplete two balls
    twoballs_incomp = generate_incomp_twoballs()
    # Generate completions for each non-negative two ball
    twoballs_comp = []
    for oneball in twoballs_incomp:
        for twoball in oneball:
            twoballs_comp.extend(complete_twoball(twoball))
    # Remove isomorphisms
    unique_graphs = [twoballs_comp[0]]
    for graph1 in twoballs_comp[1:]:
        isomorphic = False
        for graph2 in unique_graphs:
            if iso(graph1[0], graph2[0], True):
                isomorphic = True
        if not isomorphic:
            unique_graphs.append(graph1)
    return unique_graphs


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


# print generate_curv_sharp_twoballs(all_graphs)


########################################################################################################################


def complete_twoball_noiso(g):
    """ Generates completions of a two ball by adding spherical edges.
    :param g: incomplete two ball
    :return: list of completed graphs
    """
    # If there is no two sphere, return g
    if not g[1]:
        return g
    else:
        g_new = copy.deepcopy(g)
        twoball_vertices = len(g_new[1])
        degrees = []
        unsat_vertices = []  # Unsaturated vertices in the two sphere
        # Create list of degrees and unsaturated vertices
        for j in range(twoball_vertices):
            deg = 4 - len(g_new[1][j])
            degrees.append(deg)
            if deg != 0:
                unsat_vertices.append(5 + j)
        degrees.sort(reverse=True)
        unsat_vertices.sort(reverse=True)
        # Generate spherical edges
        complete_graphs = []
        generate_sph_edges(degrees, unsat_vertices, complete_graphs, g_new)
        # Sort graphs
        sorted_graphs = []
        for graph in complete_graphs:
            graph[2].sort(key=lambda x: x[:])
            sorted_graphs.append(graph)
        # Remove graphs of negative curvature
        graphs_non_neg = []
        for graph in sorted_graphs:
            curv = curvatures(graph)
            only_curvatures = list(izip(*curv))[1]
            if min(only_curvatures) >= 0:
                graphs_non_neg.append([graph, curv])  # list of lists containing graph and its curvatures
        return graphs_non_neg


def generate_non_neg_twoballs_noiso():
    """ Generates all non-negatively curved four regular two balls and a list of their curvatures.
    :return: list of non-negative two balls and corresponding curvatures
    """
    # Generate incomplete two balls
    twoballs_incomp = [[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1], [1], [2], [2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1], [2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1], [2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [1], [2], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4], [1], [2]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [2, 4], [3, 4], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 4], [2, 4], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 2, 4], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], []]],
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
    # Generate completions for each non-negative two ball
    twoballs_comp = []
    for oneball in twoballs_incomp:
        for twoball in oneball:
            twoballs_comp.extend(complete_twoball_noiso(twoball))
    return twoballs_comp

# n=0
# graphs = generate_non_neg_twoballs_noiso()
# # graphs = generate_incomp_twoballs()
# for graph in graphs:
#     print graph
#     n += len(graph)
# print n

incompgraphshopefullyrightthistime=[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1], [1], [2], [2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1], [2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1], [2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [1], [2], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2], [3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4], [1], [2]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 3], [4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [2, 4], [3, 4], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 4], [2, 4], [3]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 2, 4], [3, 4], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3], [4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], []], [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], []]]
[[[1, 1, 0, 0, 1, 0], [[1, 2, 3, 4], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 2, 3], [3], [4], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [2], [3], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[3, 4], [1], [2], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 2], [3, 4], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [2, 3], [4], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [2, 4], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [3, 4], [2], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [2, 3], [3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [3, 4], [2], [3]], []], [[1, 1, 0, 0, 1, 0], [[3, 4], [3, 4], [1], [2]], []], [[1, 1, 0, 0, 1, 0], [[1, 2, 3], [3, 4], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2, 3], [4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2, 4], [3]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [3, 4], [2]], []], [[1, 1, 0, 0, 1, 0], [[1, 2, 3, 4], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 2], [3, 4], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3], [2, 4], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 4], [2, 3], [3, 4]], []], [[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2, 3, 4]], []]]
[[[1, 1, 1, 0, 0, 0], [[2, 3, 4], [2], [3], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2], [3], [4], [4]], []], [[1, 1, 1, 0, 0, 0], [[2], [2], [3], [3], [4], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2, 3], [4], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2, 4], [3], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3, 4], [2, 3], [4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3], [2, 4], [3, 4]], []], [[1, 1, 1, 0, 0, 0], [[2, 3, 4], [2, 3, 4]], []]]
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1], [2], [3], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2, 3], [4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [3, 4], [3, 4], [1], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [3, 4], [1], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3], [2, 4], [3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [3]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 2], [2, 3], [3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 3], [2, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2, 4], [3]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [3, 4], [1]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [2, 3], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 3, 4], [4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3, 4], [2]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [2, 3, 4]], []]]
[[[1, 1, 1, 1, 1, 0], [[3, 4]], []], [[1, 1, 1, 1, 1, 0], [[3], [4]], []]]
[[[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2], [3], [4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [2], [3], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 4], [3], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [3, 4], [2], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 4], [1], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 3], [4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [2, 4], [3], [3]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [3, 4], [2], [3]], []], [[1, 1, 0, 0, 0, 0], [[2, 3], [2, 4], [3, 4], [1], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 4], [2, 4], [3, 4], [1], [3]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3, 4], [3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 3, 4], [1], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3], [2, 4], [3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3], [3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 4], [3, 4], [3]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [3, 4], [3, 4], [2]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 2], [3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2, 3], [4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2, 4], [3]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 4], [3, 4], [1]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 3, 4], [4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 3, 4], [2, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3, 4], [3, 4]], []], [[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 3, 4], [1, 4]], []]]
[[[1, 1, 1, 1, 0, 0], [[2, 3, 4], [4]], []], [[1, 1, 1, 1, 0, 0], [[2, 3], [4], [4]], []], [[1, 1, 1, 1, 0, 0], [[2, 4], [3], [4]], []], [[1, 1, 1, 1, 0, 0], [[2], [3], [4], [4]], []], [[1, 1, 1, 1, 0, 0], [[2, 4], [3, 4]], []]]
[[[1, 1, 0, 0, 1, 1], [[1, 2, 3, 4]], []], [[1, 1, 0, 0, 1, 1], [[1, 2, 3], [4]], []], [[1, 1, 0, 0, 1, 1], [[1, 2], [3], [4]], []], [[1, 1, 0, 0, 1, 1], [[1, 4], [2], [3]], []], [[1, 1, 0, 0, 1, 1], [[1], [2], [3], [4]], []], [[1, 1, 0, 0, 1, 1], [[1, 2], [3, 4]], []], [[1, 1, 0, 0, 1, 1], [[1, 4], [2, 3]], []]]
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3], [2], [4], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 2, 3], [4], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 2, 4], [3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3, 4], [2], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3], [2, 4], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [2, 4], [3]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [3, 4], [2]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2, 3], [4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2], [3, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 2, 4], [3, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3, 4], [2, 4]], []], [[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2, 3, 4]], []]]
[[[1, 1, 0, 1, 0, 0], [[1, 2, 3, 4], [4], [4]], []], [[1, 1, 0, 1, 0, 0], [[1, 4], [2, 4], [3], [4]], []], [[1, 1, 0, 1, 0, 0], [[1, 2, 4], [3, 4], [4]], []], [[1, 1, 0, 1, 0, 0], [[1, 4], [2, 4], [3, 4]], []]]
[[[1, 1, 1, 1, 1, 1], [], []]]
204

# new = [graphs[0]]
# for graph in graphs[1:]:
#     isom =False
#     for graph2 in new:
#         if iso(graph,graph2,True):
#             isom = True
#     if not isom:
#         new.append(graph)
# for graphh in new:
#     print graphh
# print len(new)


twoballs_comp = [[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 9], [6, 11], [7, 8], [7, 11], [8, 10], [9, 12], [10, 12], [11, 12]]], [[0, 0.0], [1, 0.626], [2, 0.219], [3, 0.219], [4, 0.0], [5, 0.5], [6, 0.5], [7, 0.0], [8, 0.0], [9, 0.626], [10, 0.219], [11, 0.219], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 11], [7, 10], [8, 12], [9, 10], [9, 11], [10, 12], [11, 12]]], [[0, 0.0], [1, 0.219], [2, 0.448], [3, 0.448], [4, 0.219], [5, 0.683], [6, 0.448], [7, 0.448], [8, 0.683], [9, 0.543], [10, 0.321], [11, 0.321], [12, 0.543]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 12], [8, 11], [9, 10], [9, 11], [10, 12], [11, 12]]], [[0, 0.0], [1, 0.219], [2, 0.448], [3, 0.448], [4, 0.219], [5, 0.448], [6, 0.683], [7, 0.683], [8, 0.448], [9, 0.543], [10, 0.321], [11, 0.321], [12, 0.543]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 11], [6, 7], [6, 12], [7, 9], [8, 10], [9, 10], [9, 11], [10, 12], [11, 12]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 12], [6, 7], [6, 10], [7, 11], [8, 9], [9, 10], [9, 11], [10, 12], [11, 12]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 12], [7, 8], [7, 11], [9, 10], [9, 12], [10, 11], [11, 12]]], [[0, 0.0], [1, 0.219], [2, 0.219], [3, 0.0], [4, 0.0], [5, 1.391], [6, 0.427], [7, 0.427], [8, 1.085], [9, 0.653], [10, 0.653], [11, 0.0], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 11], [6, 8], [6, 12], [7, 9], [7, 10], [8, 10], [9, 12], [10, 11], [11, 12]]], [[0, 0.0], [1, 0.219], [2, 0.427], [3, 0.0], [4, 0.0], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.427], [9, 0.427], [10, 0.219], [11, 0.0], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 10], [5, 12], [6, 9], [6, 10], [7, 8], [7, 11], [8, 9], [9, 12], [10, 11], [11, 12]]], [[0, 0.0], [1, 0.427], [2, 0.219], [3, 0.0], [4, 0.0], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.427], [9, 0.219], [10, 0.427], [11, 0.0], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 12], [7, 10], [7, 12], [8, 9], [9, 11], [10, 11], [11, 12]]], [[0, 0.0], [1, 0.219], [2, 0.626], [3, 0.0], [4, 0.219], [5, 0.5], [6, 0.0], [7, 0.5], [8, 0.0], [9, 0.219], [10, 0.626], [11, 0.0], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 11], [6, 9], [6, 10], [7, 11], [7, 12], [8, 9], [9, 12], [10, 11], [10, 12]]], [[0, 0.0], [1, 0.219], [2, 0.0], [3, 0.0], [4, 0.219], [5, 0.0], [6, 0.427], [7, 0.278], [8, 0.0], [9, 0.427], [10, 0.0], [11, 0.0], [12, 0.543]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 11], [6, 9], [6, 10], [7, 11], [7, 12], [8, 10], [9, 11], [9, 12], [10, 12]]], [[0, 0.0], [1, 0.219], [2, 0.0], [3, 0.0], [4, 0.219], [5, 0.0], [6, 0.427], [7, 0.427], [8, 0.0], [9, 0.427], [10, 0.0], [11, 0.0], [12, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 11], [6, 11], [6, 12], [7, 8], [7, 9], [8, 10], [9, 12], [10, 11], [10, 12]]], [[0, 0.0], [1, 0.427], [2, 0.0], [3, 0.219], [4, 0.0], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.427], [9, 0.219], [10, 0.0], [11, 0.427], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 11], [6, 11], [6, 12], [7, 9], [7, 10], [8, 9], [9, 12], [10, 11], [10, 12]]], [[0, 0.0], [1, 0.0], [2, 0.219], [3, 0.219], [4, 0.0], [5, 0.0], [6, 0.427], [7, 0.278], [8, 0.0], [9, 0.0], [10, 0.543], [11, 0.427], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 12], [6, 9], [6, 11], [7, 8], [8, 10], [9, 11], [9, 12], [10, 11], [10, 12]]], [[0, 0.0], [1, 0.219], [2, 0.0], [3, 0.219], [4, 0.0], [5, 0.427], [6, 1.391], [7, 1.085], [8, 0.427], [9, 0.653], [10, 0.0], [11, 0.653], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 12], [6, 9], [6, 11], [7, 9], [7, 11], [8, 10], [9, 12], [10, 11], [10, 12]]], [[0, 0.0], [1, 0.219], [2, 0.0], [3, 0.219], [4, 0.0], [5, 0.0], [6, 0.5], [7, 0.0], [8, 0.0], [9, 0.219], [10, 0.0], [11, 0.219], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 12], [6, 11], [6, 12], [7, 9], [7, 10], [8, 9], [9, 11], [10, 11], [10, 12]]], [[0, 0.0], [1, 0.0], [2, 0.219], [3, 0.219], [4, 0.0], [5, 0.0], [6, 0.427], [7, 0.427], [8, 0.0], [9, 0.0], [10, 0.427], [11, 0.427], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 10], [6, 12], [7, 9], [7, 11], [8, 11], [8, 12], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.427], [5, 1.085], [6, 0.0], [7, 0.0], [8, 1.085], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 11], [6, 11], [6, 12], [7, 9], [7, 10], [8, 10], [8, 12], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.427], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 11], [5, 12], [6, 9], [6, 10], [7, 9], [7, 10], [8, 11], [8, 12], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.219], [2, 0.219], [3, 0.219], [4, 0.219], [5, 0.0], [6, 0.219], [7, 0.219], [8, 0.5], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 10], [5, 12], [6, 9], [6, 11], [7, 9], [7, 11], [8, 10], [8, 12], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.219], [2, 0.219], [3, 0.219], [4, 0.219], [5, 0.219], [6, 0.5], [7, 0.0], [8, 0.219], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 11], [6, 10], [6, 12], [7, 10], [7, 12], [8, 9], [9, 11], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.219], [3, 0.0], [4, 0.219], [5, 0.0], [6, 0.0], [7, 0.5], [8, 0.0], [9, 0.0], [10, 0.219], [11, 0.0], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 11], [6, 10], [6, 12], [7, 10], [7, 12], [8, 9], [8, 11], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.219], [2, 0.219], [3, 0.219], [4, 0.219], [5, 0.219], [6, 0.0], [7, 0.5], [8, 0.219], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 11], [6, 12], [7, 11], [7, 12], [8, 9], [8, 10], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.219], [2, 0.219], [3, 0.219], [4, 0.219], [5, 0.5], [6, 0.219], [7, 0.219], [8, 0.0], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 12], [6, 9], [6, 10], [7, 11], [7, 12], [8, 10], [9, 11], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.219], [2, 0.0], [3, 0.0], [4, 0.219], [5, 0.0], [6, 0.278], [7, 0.427], [8, 0.0], [9, 0.543], [10, 0.0], [11, 0.0], [12, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 10], [5, 12], [6, 8], [6, 10], [7, 11], [7, 12], [8, 9], [9, 11], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.427], [3, 0.0], [4, 0.219], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.427], [9, 0.0], [10, 0.219], [11, 0.0], [12, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 10], [5, 12], [6, 9], [6, 10], [7, 11], [7, 12], [8, 9], [8, 11], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.427], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 11], [5, 12], [6, 9], [6, 11], [7, 10], [7, 12], [8, 9], [8, 10], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.427], [5, 0.0], [6, 1.085], [7, 1.085], [8, 0.0], [9, 0.219], [10, 0.219], [11, 0.219], [12, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 12], [6, 11], [6, 12], [7, 9], [7, 10], [8, 10], [9, 11], [9, 12], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.219], [3, 0.219], [4, 0.0], [5, 0.0], [6, 0.278], [7, 0.427], [8, 0.0], [9, 0.0], [10, 0.427], [11, 0.543], [12, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [6, 9], [7, 10], [7, 11], [8, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.666], [1, 1.164], [2, 1.164], [3, 0.219], [4, 0.219], [5, 1.106], [6, 1.106], [7, 1.391], [8, 0.427], [9, 0.427], [10, 0.653], [11, 0.653]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [6, 8], [7, 10], [7, 11], [8, 9], [8, 11], [9, 10], [10, 11]]], [[0, 0.666], [1, 1.164], [2, 1.164], [3, 0.219], [4, 0.219], [5, 1.106], [6, 1.106], [7, 1.391], [8, 0.427], [9, 0.427], [10, 0.653], [11, 0.653]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [1], [2], [3], [4]], [[5, 10], [6, 11], [7, 8], [7, 9], [8, 10], [8, 11], [9, 10], [9, 11]]], [[0, 0.666], [1, 0.367], [2, 0.367], [3, 0.891], [4, 0.891], [5, 1.426], [6, 1.426], [7, 0.666], [8, 0.367], [9, 0.367], [10, 1.426], [11, 1.426]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], [[5, 9], [6, 8], [6, 11], [7, 8], [7, 10], [9, 10], [9, 11], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.614], [3, 0.0], [4, 0.0], [5, 0.614], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.5], [10, 0.219], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], [[5, 11], [6, 8], [6, 10], [7, 9], [7, 10], [8, 9], [9, 11], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], [[5, 9], [6, 9], [6, 11], [7, 8], [7, 11], [8, 10], [9, 10], [10, 11]]], [[0, 0.0], [1, 0.367], [2, 0.746], [3, 0.219], [4, 0.448], [5, 1.056], [6, 0.561], [7, 0.448], [8, 0.683], [9, 0.626], [10, 0.543], [11, 0.321]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], [[5, 10], [6, 8], [6, 11], [7, 10], [7, 11], [8, 9], [9, 10], [9, 11]]], [[0, 0.0], [1, 1.0], [2, 0.078], [3, 0.543], [4, 0.543], [5, 1.426], [6, 0.078], [7, 0.427], [8, 0.0], [9, 1.0], [10, 0.427], [11, 1.426]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [2], [3], [4]], [[5, 10], [6, 10], [6, 11], [7, 8], [7, 11], [8, 9], [9, 10], [9, 11]]], [[0, 0.0], [1, 0.367], [2, 0.0], [3, 0.543], [4, 0.448], [5, 1.353], [6, 1.0], [7, 0.448], [8, 0.321], [9, 0.078], [10, 1.164], [11, 0.404]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [1], [2], [3]], [[5, 10], [6, 8], [6, 11], [7, 9], [7, 11], [8, 9], [9, 10], [10, 11]]], [[0, 1.0], [1, 0.0], [2, 0.891], [3, 0.0], [4, 2.0], [5, 1.0], [6, 0.0], [7, 1.0], [8, 0.0], [9, 0.0], [10, 1.0], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [1], [2], [3]], [[5, 9], [6, 10], [6, 11], [7, 8], [7, 11], [8, 10], [9, 10], [9, 11]]], [[0, 1.0], [1, 0.891], [2, 0.0], [3, 0.0], [4, 2.0], [5, 1.0], [6, 1.0], [7, 0.0], [8, 0.0], [9, 1.0], [10, 0.0], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2], [3], [4]], [[5, 9], [6, 8], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 1.333], [1, 1.333], [2, 1.164], [3, 1.164], [4, 1.164], [5, 1.164], [6, 1.164], [7, 1.164], [8, 0.5], [9, 0.5], [10, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2], [3], [4]], [[5, 8], [6, 10], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 1.333], [1, 1.333], [2, 1.164], [3, 1.164], [4, 1.164], [5, 1.164], [6, 1.164], [7, 1.164], [8, 0.5], [9, 0.5], [10, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2], [3], [4]], [[5, 10], [6, 9], [7, 8], [8, 9], [8, 10], [9, 10]]], [[0, 1.333], [1, 1.333], [2, 0.367], [3, 0.367], [4, 0.367], [5, 0.367], [6, 0.367], [7, 0.367], [8, 0.0], [9, 0.0], [10, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 9], [7, 11], [8, 11], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.614], [3, 0.0], [4, 0.219], [5, 0.614], [6, 0.0], [7, 0.0], [8, 0.5], [9, 0.0], [10, 0.0], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 10], [7, 9], [7, 11], [8, 11], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.614], [3, 0.0], [4, 0.219], [5, 0.0], [6, 0.614], [7, 0.0], [8, 0.5], [9, 0.0], [10, 0.0], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 11], [7, 9], [7, 11], [8, 10], [10, 11]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.891], [7, 2.0], [8, 1.0], [9, 0.0], [10, 0.0], [11, 1.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 9], [5, 10], [6, 9], [6, 11], [7, 8], [7, 11], [8, 10], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 8], [5, 11], [6, 9], [6, 10], [7, 9], [7, 11], [8, 10], [10, 11]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 0.0], [4, 0.0], [5, 0.891], [6, 0.0], [7, 2.0], [8, 1.0], [9, 0.0], [10, 0.0], [11, 1.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 9], [5, 11], [6, 9], [6, 10], [7, 8], [7, 11], [8, 10], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 9], [5, 10], [6, 9], [6, 11], [7, 10], [7, 11], [8, 10], [8, 11]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 0.219], [4, 0.219], [5, 1.0], [6, 1.0], [7, 0.427], [8, 0.427], [9, 0.0], [10, 0.427], [11, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 9], [5, 11], [6, 9], [6, 10], [7, 10], [7, 11], [8, 10], [8, 11]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 0.219], [4, 0.219], [5, 1.0], [6, 1.0], [7, 0.427], [8, 0.427], [9, 0.0], [10, 0.427], [11, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 10], [7, 10], [8, 11], [9, 11], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.448], [4, 0.427], [5, 0.5], [6, 0.448], [7, 0.427], [8, 0.321], [9, 1.085], [10, 0.321], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 9], [5, 10], [6, 7], [6, 10], [7, 8], [8, 11], [9, 11], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.219], [5, 0.219], [6, 1.085], [7, 0.219], [8, 0.0], [9, 1.085], [10, 0.219], [11, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 9], [5, 11], [6, 8], [6, 10], [7, 9], [7, 10], [8, 11], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.427], [3, 0.448], [4, 0.0], [5, 0.0], [6, 0.448], [7, 0.427], [8, 0.321], [9, 1.085], [10, 0.321], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 11], [7, 11], [8, 10], [9, 10], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.448], [4, 0.427], [5, 0.5], [6, 0.321], [7, 1.085], [8, 0.448], [9, 0.427], [10, 0.321], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 10], [6, 8], [6, 11], [7, 9], [7, 11], [9, 10], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 0.427], [3, 0.0], [4, 0.448], [5, 0.0], [6, 0.427], [7, 0.448], [8, 1.085], [9, 0.321], [10, 0.0], [11, 0.321]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 10], [6, 9], [6, 11], [7, 10], [7, 11], [8, 9], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 1.5], [3, 0.0], [4, 0.219], [5, 0.219], [6, 0.0], [7, 1.5], [8, 1.5], [9, 0.219], [10, 0.219], [11, 1.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 11], [6, 7], [6, 9], [7, 11], [8, 10], [9, 10], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.219], [4, 0.427], [5, 0.219], [6, 0.219], [7, 1.085], [8, 1.085], [9, 0.0], [10, 0.427], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 11], [6, 8], [6, 11], [7, 9], [8, 10], [9, 10], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.0], [3, 0.448], [4, 0.0], [5, 0.0], [6, 0.321], [7, 1.085], [8, 0.448], [9, 0.427], [10, 0.321], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 11], [6, 10], [6, 11], [7, 8], [8, 9], [9, 10], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.219], [4, 0.0], [5, 0.0], [6, 0.626], [7, 0.427], [8, 0.0], [9, 0.427], [10, 0.626], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 10], [5, 11], [6, 7], [6, 11], [7, 8], [8, 9], [9, 10], [10, 11]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.0], [4, 0.0], [5, 0.219], [6, 2.0], [7, 0.427], [8, 0.427], [9, 2.0], [10, 0.427], [11, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 9], [5, 11], [6, 10], [6, 11], [7, 8], [7, 10], [8, 9], [10, 11]]], [[0, 0.0], [1, 0.0], [2, 1.5], [3, 0.219], [4, 0.0], [5, 0.219], [6, 1.5], [7, 0.0], [8, 0.219], [9, 1.5], [10, 1.5], [11, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 10], [5, 11], [6, 8], [6, 10], [7, 9], [7, 11], [8, 10], [9, 11]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.638], [4, 0.638], [5, 0.0], [6, 0.638], [7, 0.638], [8, 0.638], [9, 0.638], [10, 0.638], [11, 0.638]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 10], [5, 11], [6, 9], [6, 11], [7, 8], [7, 10], [8, 11], [9, 10]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0], [11, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], [[5, 9], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.241], [1, 0.241], [2, 0.241], [3, 0.938], [4, 0.448], [5, 0.938], [6, 0.241], [7, 0.321], [8, 0.448], [9, 0.219], [10, 0.321]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], [[5, 10], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.241], [1, 0.241], [2, 0.241], [3, 0.938], [4, 0.448], [5, 0.241], [6, 0.938], [7, 0.321], [8, 0.448], [9, 0.219], [10, 0.321]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], [[5, 8], [6, 10], [7, 9], [7, 10], [8, 9], [9, 10]]], [[0, 0.241], [1, 0.241], [2, 0.938], [3, 0.241], [4, 0.321], [5, 0.938], [6, 0.241], [7, 0.448], [8, 0.219], [9, 0.321], [10, 0.448]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], [[5, 9], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.241], [1, 0.241], [2, 0.241], [3, 0.938], [4, 0.448], [5, 0.938], [6, 0.241], [7, 0.448], [8, 0.321], [9, 0.219], [10, 0.321]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], [[5, 10], [6, 8], [7, 9], [7, 10], [8, 9], [9, 10]]], [[0, 0.241], [1, 0.241], [2, 0.938], [3, 0.241], [4, 0.321], [5, 0.241], [6, 0.938], [7, 0.448], [8, 0.219], [9, 0.321], [10, 0.448]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3], [4]], [[5, 10], [6, 9], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.241], [1, 0.241], [2, 0.241], [3, 0.938], [4, 0.448], [5, 0.241], [6, 0.938], [7, 0.448], [8, 0.321], [9, 0.219], [10, 0.321]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3], [4]], [[5, 9], [6, 10], [7, 9], [7, 10], [8, 9], [8, 10]]], [[0, 0.666], [1, 2.0], [2, 2.0], [3, 1.091], [4, 1.091], [5, 0.871], [6, 0.871], [7, 0.666], [8, 0.5], [9, 1.091], [10, 1.091]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3], [4]], [[5, 8], [6, 10], [7, 9], [7, 10], [8, 9], [9, 10]]], [[0, 0.0], [1, 1.0], [2, 1.353], [3, 0.294], [4, 0.614], [5, 1.164], [6, 1.164], [7, 1.091], [8, 0.543], [9, 0.626], [10, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3], [4]], [[5, 9], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 0.615], [4, 0.615], [5, 1.164], [6, 1.164], [7, 0.078], [8, 0.078], [9, 0.278], [10, 0.278]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3], [4]], [[5, 10], [6, 9], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3], [4]], [[5, 9], [6, 10], [7, 9], [7, 10], [8, 9], [8, 10]]], [[0, 0.0], [1, 1.612], [2, 1.612], [3, 0.746], [4, 0.746], [5, 1.747], [6, 1.747], [7, 0.561], [8, 0.561], [9, 0.626], [10, 0.626]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], [[5, 9], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 0.0], [2, 1.164], [3, 1.164], [4, 1.091], [5, 1.353], [6, 0.294], [7, 0.614], [8, 0.5], [9, 0.543], [10, 0.626]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], [[5, 10], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 1.0], [2, 1.164], [3, 1.426], [4, 0.219], [5, 0.367], [6, 1.106], [7, 0.543], [8, 1.085], [9, 0.427], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], [[5, 8], [6, 10], [7, 9], [7, 10], [8, 9], [9, 10]]], [[0, 1.0], [1, 1.0], [2, 0.367], [3, 1.106], [4, 0.543], [5, 1.164], [6, 1.426], [7, 0.219], [8, 0.427], [9, 0.427], [10, 1.085]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], [[5, 9], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 1.0], [1, 1.0], [2, 1.164], [3, 1.426], [4, 0.891], [5, 1.164], [6, 1.426], [7, 0.891], [8, 1.0], [9, 0.219], [10, 1.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [3, 4], [2], [4]], [[5, 10], [6, 9], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 1.0], [1, 0.0], [2, 1.164], [3, 1.164], [4, 0.078], [5, 1.0], [6, 0.615], [7, 0.615], [8, 0.278], [9, 0.278], [10, 0.078]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4], [1], [2]], [[5, 9], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.666], [1, 1.164], [2, 1.164], [3, 0.404], [4, 0.404], [5, 1.106], [6, 1.106], [7, 0.448], [8, 0.448], [9, 0.427], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4], [1], [2]], [[5, 10], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.666], [1, 1.164], [2, 1.164], [3, 0.404], [4, 0.404], [5, 1.106], [6, 1.106], [7, 0.448], [8, 0.448], [9, 0.427], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4], [1], [2]], [[5, 9], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.666], [1, 1.164], [2, 1.164], [3, 0.404], [4, 0.404], [5, 1.106], [6, 1.106], [7, 0.448], [8, 0.448], [9, 0.427], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [3, 4], [3, 4], [1], [2]], [[5, 10], [6, 9], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.666], [1, 1.164], [2, 1.164], [3, 0.404], [4, 0.404], [5, 1.106], [6, 1.106], [7, 0.448], [8, 0.448], [9, 0.427], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], [[5, 7], [6, 8], [6, 10], [7, 10], [8, 9], [9, 10]]], [[0, 0.367], [1, 1.056], [2, 0.278], [3, 0.561], [4, 0.448], [5, 0.746], [6, 0.891], [7, 0.626], [8, 0.683], [9, 0.448], [10, 0.321]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], [[5, 8], [6, 8], [6, 10], [7, 9], [7, 10], [9, 10]]], [[0, 0.367], [1, 1.0], [2, 1.879], [3, 0.294], [4, 0.219], [5, 0.321], [6, 0.561], [7, 1.11], [8, 0.448], [9, 1.391], [10, 0.653]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], [[5, 10], [6, 8], [6, 10], [7, 8], [7, 9], [9, 10]]], [[0, 0.367], [1, 1.0], [2, 1.164], [3, 1.426], [4, 0.427], [5, 1.0], [6, 1.106], [7, 0.543], [8, 0.427], [9, 1.085], [10, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], [[5, 9], [6, 8], [6, 10], [7, 9], [7, 10], [8, 10]]], [[0, 0.367], [1, 1.0], [2, 0.294], [3, 1.879], [4, 0.219], [5, 0.321], [6, 1.11], [7, 0.561], [8, 1.391], [9, 0.448], [10, 0.653]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], [[5, 10], [6, 8], [6, 9], [7, 9], [7, 10], [8, 10]]], [[0, 0.367], [1, 1.0], [2, 1.426], [3, 1.164], [4, 0.427], [5, 1.0], [6, 0.543], [7, 1.106], [8, 1.085], [9, 0.427], [10, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4]], [[5, 10], [6, 9], [6, 10], [7, 8], [7, 10], [8, 9]]], [[0, 0.367], [1, 1.333], [2, 0.367], [3, 0.367], [4, 0.0], [5, 1.333], [6, 0.367], [7, 0.367], [8, 0.0], [9, 0.0], [10, 0.367]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [2, 4], [3, 4], [3]], [[5, 8], [6, 7], [6, 10], [7, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 0.278], [2, 1.106], [3, 0.219], [4, 0.427], [5, 0.614], [6, 0.543], [7, 0.5], [8, 0.427], [9, 1.085], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [2, 4], [3, 4], [3]], [[5, 7], [6, 8], [6, 10], [7, 10], [8, 9], [9, 10]]], [[0, 1.0], [1, 1.106], [2, 0.278], [3, 0.219], [4, 0.427], [5, 0.614], [6, 0.543], [7, 0.427], [8, 0.5], [9, 1.085], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [2, 4], [3, 4], [3]], [[5, 8], [6, 9], [6, 10], [7, 9], [7, 10], [8, 10]]], [[0, 1.0], [1, 0.078], [2, 1.106], [3, 0.0], [4, 0.427], [5, 0.614], [6, 0.078], [7, 1.106], [8, 0.427], [9, 0.614], [10, 1.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [2, 4], [3, 4], [3]], [[5, 10], [6, 8], [6, 9], [7, 9], [7, 10], [8, 10]]], [[0, 1.0], [1, 1.0], [2, 1.426], [3, 0.543], [4, 2.0], [5, 1.426], [6, 0.543], [7, 2.0], [8, 0.427], [9, 0.0], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], [[5, 8], [6, 7], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.078], [1, 0.278], [2, 0.078], [3, 0.615], [4, 1.0], [5, 0.278], [6, 0.615], [7, 1.164], [8, 1.164], [9, 0.0], [10, 1.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], [[5, 9], [6, 7], [6, 8], [7, 10], [8, 10], [9, 10]]], [[0, 0.078], [1, 0.278], [2, 0.078], [3, 0.615], [4, 1.0], [5, 0.278], [6, 0.615], [7, 1.164], [8, 0.0], [9, 1.164], [10, 1.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], [[5, 8], [6, 7], [6, 10], [7, 9], [8, 10], [9, 10]]], [[0, 0.078], [1, 0.278], [2, 0.278], [3, 0.615], [4, 0.614], [5, 0.278], [6, 1.263], [7, 0.5], [8, 0.614], [9, 0.614], [10, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], [[5, 9], [6, 7], [6, 10], [7, 8], [8, 10], [9, 10]]], [[0, 0.078], [1, 0.278], [2, 0.278], [3, 0.615], [4, 0.614], [5, 0.278], [6, 1.263], [7, 0.5], [8, 0.614], [9, 0.614], [10, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], [[5, 10], [6, 8], [6, 9], [7, 8], [7, 10], [9, 10]]], [[0, 0.078], [1, 1.0], [2, 0.614], [3, 0.078], [4, 1.106], [5, 1.106], [6, 0.0], [7, 0.427], [8, 0.614], [9, 1.0], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2], [1, 4], [3, 4], [3, 4], [2]], [[5, 10], [6, 8], [6, 9], [7, 9], [7, 10], [8, 10]]], [[0, 0.078], [1, 1.0], [2, 0.614], [3, 0.078], [4, 1.106], [5, 1.106], [6, 0.0], [7, 0.427], [8, 1.0], [9, 0.614], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3], [4]], [[5, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.333], [1, 1.333], [2, 1.747], [3, 1.747], [4, 1.814], [5, 1.814], [6, 1.747], [7, 1.747], [8, 0.626], [9, 0.626]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3], [4]], [[5, 9], [6, 8], [7, 9], [8, 9]]], [[0, 1.333], [1, 1.333], [2, 2.166], [3, 1.333], [4, 1.164], [5, 1.333], [6, 1.164], [7, 2.166], [8, 1.164], [9, 1.164]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3], [4]], [[5, 9], [6, 9], [7, 8], [8, 9]]], [[0, 1.333], [1, 1.333], [2, 1.333], [3, 2.166], [4, 1.164], [5, 1.333], [6, 2.166], [7, 1.164], [8, 1.164], [9, 1.164]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 2], [3, 4], [3, 4]], [[6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3, 4]], [[6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 2.0], [1, 0.871], [2, 0.871], [3, 0.871], [4, 0.871], [5, 2.0], [6, 1.263], [7, 1.263], [8, 1.263], [9, 1.263]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3, 4]], [[6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 2.0], [1, 0.871], [2, 0.666], [3, 0.666], [4, 0.871], [5, 2.0], [6, 0.615], [7, 0.615], [8, 0.615], [9, 0.615]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4], [3, 4]], [[6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 2.0], [1, 0.666], [2, 0.871], [3, 0.871], [4, 0.666], [5, 2.0], [6, 0.615], [7, 0.615], [8, 0.615], [9, 0.615]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 9], [8, 10]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 1.0], [4, 1.0], [5, 0.543], [6, 0.543], [7, 1.085], [8, 1.085], [9, 0.543], [10, 0.543]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 7], [5, 9], [6, 9], [6, 10], [7, 8], [8, 10]]], [[0, 0.0], [1, 0.614], [2, 1.0], [3, 1.0], [4, 0.614], [5, 1.106], [6, 0.078], [7, 0.427], [8, 0.427], [9, 0.078], [10, 1.106]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 9], [8, 10]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 1.0], [4, 1.0], [5, 0.543], [6, 0.543], [7, 1.085], [8, 1.085], [9, 0.543], [10, 0.543]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 9], [5, 10], [6, 7], [6, 9], [7, 8], [8, 10]]], [[0, 0.0], [1, 0.614], [2, 1.0], [3, 1.0], [4, 0.614], [5, 0.078], [6, 1.106], [7, 0.427], [8, 0.427], [9, 0.078], [10, 1.106]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 7], [5, 9], [6, 8], [6, 10], [7, 10], [8, 9]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 1.0], [4, 1.0], [5, 0.543], [6, 0.543], [7, 1.085], [8, 1.085], [9, 0.543], [10, 0.543]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 9], [6, 8], [6, 10], [7, 9], [7, 10]]], [[0, 0.0], [1, 1.0], [2, 1.181], [3, 1.181], [4, 1.0], [5, 0.561], [6, 0.561], [7, 2.0], [8, 2.0], [9, 0.561], [10, 0.561]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 9], [6, 9], [6, 10], [7, 8], [7, 10]]], [[0, 0.0], [1, 1.0], [2, 0.614], [3, 0.614], [4, 1.0], [5, 1.106], [6, 0.078], [7, 0.427], [8, 0.427], [9, 0.078], [10, 1.106]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 10], [8, 9]]], [[0, 0.0], [1, 1.0], [2, 1.0], [3, 1.0], [4, 1.0], [5, 0.543], [6, 0.543], [7, 1.085], [8, 1.085], [9, 0.543], [10, 0.543]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 10], [6, 8], [6, 9], [7, 9], [7, 10]]], [[0, 0.0], [1, 1.0], [2, 1.181], [3, 1.181], [4, 1.0], [5, 0.561], [6, 0.561], [7, 2.0], [8, 2.0], [9, 0.561], [10, 0.561]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [7, 10]]], [[0, 0.0], [1, 1.0], [2, 0.614], [3, 0.614], [4, 1.0], [5, 0.078], [6, 1.106], [7, 0.427], [8, 0.427], [9, 0.078], [10, 1.106]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 7], [5, 10], [6, 9], [6, 10], [7, 8], [8, 9]]], [[0, 0.0], [1, 0.614], [2, 1.0], [3, 1.0], [4, 0.614], [5, 1.106], [6, 0.078], [7, 0.427], [8, 0.427], [9, 1.106], [10, 0.078]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 9], [5, 10], [6, 7], [6, 10], [7, 8], [8, 9]]], [[0, 0.0], [1, 0.614], [2, 1.0], [3, 1.0], [4, 0.614], [5, 0.078], [6, 1.106], [7, 0.427], [8, 0.427], [9, 1.106], [10, 0.078]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 8], [7, 9]]], [[0, 0.0], [1, 1.0], [2, 0.614], [3, 0.614], [4, 1.0], [5, 1.106], [6, 0.078], [7, 0.427], [8, 0.427], [9, 1.106], [10, 0.078]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 9], [5, 10], [6, 8], [6, 10], [7, 8], [7, 9]]], [[0, 0.0], [1, 1.0], [2, 0.614], [3, 0.614], [4, 1.0], [5, 0.078], [6, 1.106], [7, 0.427], [8, 0.427], [9, 1.106], [10, 0.078]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 10]]], [[0, 2.0], [1, 1.5], [2, 2.0], [3, 1.5], [4, 1.5], [5, 1.5], [6, 0.5], [7, 0.5], [8, 1.5], [9, 1.5], [10, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 9], [7, 8], [8, 10], [9, 10]]], [[0, 2.0], [1, 1.5], [2, 2.0], [3, 0.427], [4, 0.427], [5, 1.5], [6, 0.219], [7, 0.219], [8, 0.427], [9, 0.427], [10, 2.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 8], [6, 7], [7, 10], [8, 9], [9, 10]]], [[0, 2.0], [1, 1.5], [2, 1.5], [3, 2.0], [4, 1.5], [5, 0.5], [6, 1.5], [7, 0.5], [8, 1.5], [9, 0.5], [10, 1.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 10], [6, 7], [7, 8], [8, 9], [9, 10]]], [[0, 2.0], [1, 1.5], [2, 0.427], [3, 2.0], [4, 0.427], [5, 0.219], [6, 1.5], [7, 0.219], [8, 0.427], [9, 2.5], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 8], [9, 10]]], [[0, 2.0], [1, 0.427], [2, 2.0], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.0], [7, 0.0], [8, 0.427], [9, 0.427], [10, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 8], [9, 10]]], [[0, 2.0], [1, 0.427], [2, 0.427], [3, 2.0], [4, 0.427], [5, 0.0], [6, 0.427], [7, 0.0], [8, 0.427], [9, 0.0], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 7], [5, 9], [6, 9], [6, 10], [7, 8], [8, 10]]], [[0, 2.0], [1, 0.427], [2, 0.427], [3, 1.5], [4, 2.0], [5, 2.5], [6, 0.219], [7, 0.427], [8, 0.219], [9, 0.427], [10, 1.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 9], [8, 10]]], [[0, 2.0], [1, 0.427], [2, 2.0], [3, 1.5], [4, 0.427], [5, 0.427], [6, 0.219], [7, 2.5], [8, 1.5], [9, 0.427], [10, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 9], [5, 10], [6, 7], [6, 9], [7, 8], [8, 10]]], [[0, 2.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 2.0], [5, 0.0], [6, 0.0], [7, 0.427], [8, 0.0], [9, 0.427], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 9], [6, 8], [6, 10], [7, 9], [7, 10]]], [[0, 2.0], [1, 2.0], [2, 1.5], [3, 1.5], [4, 1.5], [5, 1.5], [6, 1.5], [7, 1.5], [8, 0.5], [9, 0.5], [10, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 9], [6, 9], [6, 10], [7, 8], [7, 10]]], [[0, 2.0], [1, 2.0], [2, 1.5], [3, 0.427], [4, 0.427], [5, 1.5], [6, 0.427], [7, 0.427], [8, 0.219], [9, 0.219], [10, 2.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 10], [8, 9]]], [[0, 2.0], [1, 0.427], [2, 1.5], [3, 2.0], [4, 0.427], [5, 0.219], [6, 0.427], [7, 2.5], [8, 1.5], [9, 0.219], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 10], [6, 8], [6, 9], [7, 9], [7, 10]]], [[0, 2.0], [1, 2.0], [2, 0.427], [3, 0.427], [4, 1.5], [5, 0.427], [6, 0.427], [7, 1.5], [8, 2.5], [9, 0.219], [10, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [7, 10]]], [[0, 2.0], [1, 2.0], [2, 0.427], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.0], [9, 0.0], [10, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 7], [5, 10], [6, 9], [6, 10], [7, 8], [8, 9]]], [[0, 2.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 2.0], [5, 0.0], [6, 0.0], [7, 0.427], [8, 0.0], [9, 0.427], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 9], [5, 10], [6, 7], [6, 10], [7, 8], [8, 9]]], [[0, 2.0], [1, 0.427], [2, 1.5], [3, 0.427], [4, 2.0], [5, 0.219], [6, 2.5], [7, 0.427], [8, 0.219], [9, 1.5], [10, 0.427]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 8], [7, 9]]], [[0, 2.0], [1, 2.0], [2, 0.427], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.0], [9, 0.0], [10, 0.0]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 9], [5, 10], [6, 8], [6, 10], [7, 8], [7, 9]]], [[0, 2.0], [1, 2.0], [2, 0.427], [3, 1.5], [4, 0.427], [5, 0.427], [6, 1.5], [7, 0.427], [8, 0.219], [9, 2.5], [10, 0.219]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], [[5, 7], [6, 8], [7, 9], [8, 9]]], [[0, 2.0], [1, 0.938], [2, 0.938], [3, 2.0], [4, 1.5], [5, 0.938], [6, 0.938], [7, 0.5], [8, 0.5], [9, 1.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], [[5, 8], [6, 7], [7, 9], [8, 9]]], [[0, 2.0], [1, 0.938], [2, 0.938], [3, 2.0], [4, 1.5], [5, 0.938], [6, 0.938], [7, 0.5], [8, 0.5], [9, 1.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], [[5, 7], [6, 9], [7, 8], [8, 9]]], [[0, 2.0], [1, 0.938], [2, 2.0], [3, 0.938], [4, 1.5], [5, 0.938], [6, 0.938], [7, 0.5], [8, 1.5], [9, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], [[5, 9], [6, 7], [7, 8], [8, 9]]], [[0, 2.0], [1, 0.938], [2, 2.0], [3, 0.938], [4, 1.5], [5, 0.938], [6, 0.938], [7, 0.5], [8, 1.5], [9, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], [[5, 8], [6, 9], [7, 8], [7, 9]]], [[0, 2.0], [1, 2.0], [2, 0.938], [3, 0.938], [4, 1.5], [5, 0.938], [6, 0.938], [7, 1.5], [8, 0.5], [9, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 3], [1, 4], [2, 4], [3, 4]], [[5, 9], [6, 8], [7, 8], [7, 9]]], [[0, 2.0], [1, 2.0], [2, 0.938], [3, 0.938], [4, 1.5], [5, 0.938], [6, 0.938], [7, 1.5], [8, 0.5], [9, 0.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3, 4]], [[5, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.666], [1, 2.0], [2, 2.0], [3, 0.615], [4, 0.615], [5, 0.871], [6, 0.871], [7, 0.666], [8, 0.615], [9, 0.615]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 2], [3, 4], [3, 4]], [[5, 9], [6, 8], [7, 8], [7, 9]]], [[0, 0.666], [1, 2.0], [2, 2.0], [3, 0.615], [4, 0.615], [5, 0.871], [6, 0.871], [7, 0.666], [8, 0.615], [9, 0.615]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], [[5, 8], [6, 7], [7, 9], [8, 9]]], [[0, 1.612], [1, 1.353], [2, 1.353], [3, 1.426], [4, 1.426], [5, 1.164], [6, 1.164], [7, 1.263], [8, 1.263], [9, 1.085]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], [[5, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.612], [1, 0.321], [2, 1.612], [3, 0.561], [4, 1.879], [5, 1.879], [6, 0.321], [7, 0.448], [8, 0.561], [9, 0.448]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], [[5, 9], [6, 7], [7, 8], [8, 9]]], [[0, 1.612], [1, 1.353], [2, 1.612], [3, 1.106], [4, 1.164], [5, 1.164], [6, 1.353], [7, 0.891], [8, 1.106], [9, 1.085]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], [[5, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.612], [1, 1.612], [2, 1.353], [3, 1.164], [4, 1.106], [5, 1.353], [6, 1.164], [7, 1.106], [8, 0.891], [9, 1.085]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4], [3, 4]], [[5, 9], [6, 8], [7, 8], [7, 9]]], [[0, 1.612], [1, 1.612], [2, 0.321], [3, 1.879], [4, 0.561], [5, 0.321], [6, 1.879], [7, 0.561], [8, 0.448], [9, 0.448]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [3, 4]], [[6, 8], [7, 8]]], [[0, 2.0], [1, 2.0], [2, 2.0], [3, 1.787], [4, 1.787], [5, 2.0], [6, 1.787], [7, 1.787], [8, 2.5]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], [[5, 7], [6, 8]]], [[0, 2.0], [1, 1.444], [2, 1.444], [3, 1.444], [4, 1.444], [5, 1.814], [6, 1.814], [7, 1.814], [8, 1.814]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], [[5, 8], [6, 7]]], [[0, 2.0], [1, 1.444], [2, 1.444], [3, 1.444], [4, 1.444], [5, 1.814], [6, 1.814], [7, 1.814], [8, 1.814]]],
[[[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], []], [[0, 2.0], [1, 2.0], [2, 2.0], [3, 2.0], [4, 2.0], [5, 2.0], [6, 2.0], [7, 2.0]]],
[[[1, 1, 0, 0, 1, 0], [[3, 4], [1], [2], [3], [4]], [[5, 7], [5, 8], [6, 7], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.391], [1, 0.653], [2, 1.11], [3, 0.5], [4, 0.294], [5, 1.164], [6, 0.626], [7, 1.056], [8, 1.47], [9, 0.746]]],
[[[1, 1, 0, 0, 1, 0], [[3, 4], [1], [2], [3], [4]], [[5, 6], [5, 9], [6, 7], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 1.391], [1, 1.11], [2, 0.653], [3, 0.294], [4, 0.5], [5, 1.164], [6, 1.056], [7, 0.626], [8, 0.746], [9, 1.47]]],
[[[1, 1, 0, 0, 1, 0], [[3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.391], [1, 0.653], [2, 0.653], [3, 0.5], [4, 0.5], [5, 1.263], [6, 0.448], [7, 0.448], [8, 0.683], [9, 0.683]]],
[[[1, 1, 0, 0, 1, 0], [[1, 2], [3, 4], [3], [4]], [[5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.739], [1, 1.739], [2, 1.739], [3, 0.5], [4, 0.5], [5, 0.5], [6, 1.739], [7, 1.739], [8, 1.739]]],
[[[1, 1, 0, 0, 1, 0], [[1, 3], [2, 4], [3], [4]], [[5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0]]],
[[[1, 1, 0, 0, 1, 0], [[1, 3], [3, 4], [2], [4]], [[5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.429], [1, 1.429], [2, 1.11], [3, 1.11], [4, 0.696], [5, 0.696], [6, 1.181], [7, 1.181], [8, 1.287]]],
[[[1, 1, 0, 0, 1, 0], [[1, 4], [2, 3], [3], [4]], [[5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.287], [1, 1.181], [2, 1.181], [3, 0.696], [4, 0.696], [5, 1.11], [6, 1.11], [7, 1.429], [8, 1.429]]],
[[[1, 1, 0, 0, 1, 0], [[1, 4], [3, 4], [2], [3]], [[5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.816], [1, 1.746], [2, 0.746], [3, 0.5], [4, 1.747], [5, 1.747], [6, 1.746], [7, 0.746], [8, 1.816]]],
[[[1, 1, 0, 0, 1, 0], [[3, 4], [3, 4], [1], [2]], [[5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 2.5], [1, 1.11], [2, 1.11], [3, 0.871], [4, 0.871], [5, 2.0], [6, 2.0], [7, 1.181], [8, 1.181]]],
[[[1, 1, 0, 0, 1, 0], [[1, 2], [3, 4], [3, 4]], [[5, 6], [5, 7], [6, 7]]], [[0, 2.5], [1, 2.5], [2, 2.5], [3, 1.166], [4, 1.166], [5, 1.166], [6, 2.708], [7, 2.708]]],
[[[1, 1, 0, 0, 1, 0], [[1, 3], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 7]]], [[0, 1.5], [1, 1.5], [2, 1.5], [3, 1.5], [4, 1.5], [5, 1.5], [6, 1.5], [7, 1.5]]],
[[[1, 1, 0, 0, 1, 0], [[1, 4], [2, 3], [3, 4]], [[5, 6], [5, 7], [6, 7]]], [[0, 2.719], [1, 2.302], [2, 2.302], [3, 2.139], [4, 2.139], [5, 2.302], [6, 2.302], [7, 2.719]]],
[[[1, 1, 0, 0, 1, 0], [[1, 3, 4], [2, 3, 4]], [[5, 6]]], [[0, 2.726], [1, 2.726], [2, 2.726], [3, 2.726], [4, 2.726], [5, 2.726], [6, 2.726]]],
[[[1, 1, 1, 0, 0, 0], [[2, 3], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 7]]], [[0, 2.708], [1, 2.708], [2, 1.166], [3, 1.166], [4, 1.166], [5, 2.5], [6, 2.5], [7, 2.5]]],
[[[1, 1, 1, 0, 0, 0], [[2, 3, 4], [2, 3, 4]], [[5, 6]]], [[0, 2.708], [1, 2.708], [2, 2.5], [3, 2.5], [4, 2.5], [5, 2.708], [6, 2.708]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 10], [7, 9], [8, 9], [8, 11], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.5], [2, 0.219], [3, 0.219], [4, 0.0], [5, 0.5], [6, 0.0], [7, 0.0], [8, 0.5], [9, 0.219], [10, 0.219], [11, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 11], [8, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.543], [2, 0.683], [3, 0.448], [4, 0.219], [5, 0.448], [6, 0.448], [7, 0.683], [8, 0.321], [9, 0.448], [10, 0.321], [11, 0.543]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 11], [8, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.5], [2, 0.5], [3, 0.219], [4, 0.448], [5, 1.391], [6, 0.683], [7, 0.448], [8, 0.653], [9, 0.543], [10, 0.653], [11, 0.321]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [7, 11], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.427], [2, 1.085], [3, 0.543], [4, 0.427], [5, 0.427], [6, 0.427], [7, 1.0], [8, 0.0], [9, 0.219], [10, 1.0], [11, 0.543]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 11], [7, 8], [7, 10], [9, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 1.085], [2, 0.427], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.219], [9, 0.219], [10, 0.5], [11, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 8], [6, 9], [6, 11], [7, 10], [8, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.5], [2, 0.5], [3, 0.448], [4, 0.219], [5, 0.683], [6, 1.391], [7, 0.448], [8, 0.543], [9, 0.653], [10, 0.321], [11, 0.653]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 11], [7, 10], [8, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.683], [2, 0.543], [3, 0.219], [4, 0.448], [5, 0.448], [6, 0.448], [7, 0.683], [8, 0.448], [9, 0.321], [10, 0.543], [11, 0.321]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 11], [7, 9], [7, 10], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 1.085], [2, 0.427], [3, 0.427], [4, 0.543], [5, 0.427], [6, 0.427], [7, 1.0], [8, 0.219], [9, 0.0], [10, 0.543], [11, 1.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 11], [7, 8], [7, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.427], [5, 2.0], [6, 2.0], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.427], [11, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 11], [6, 7], [6, 10], [7, 9], [8, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.5], [2, 0.219], [3, 0.0], [4, 0.0], [5, 0.614], [6, 0.0], [7, 0.0], [8, 0.614], [9, 0.0], [10, 0.0], [11, 0.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 11], [6, 9], [6, 10], [7, 8], [8, 9], [8, 10], [9, 11], [10, 11]]], [[0, 0.219], [1, 0.219], [2, 0.5], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.614], [7, 0.0], [8, 0.0], [9, 0.614], [10, 0.0], [11, 0.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 7], [6, 8], [7, 11], [8, 9], [8, 11], [9, 10], [10, 11]]], [[0, 0.219], [1, 0.614], [2, 0.614], [3, 0.219], [4, 0.448], [5, 1.091], [6, 0.404], [7, 0.448], [8, 0.078], [9, 0.294], [10, 0.626], [11, 0.321]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 9], [7, 11], [8, 10], [8, 11], [10, 11]]], [[0, 0.219], [1, 0.427], [2, 1.085], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 0.427], [8, 0.219], [9, 0.219], [10, 0.5], [11, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 11], [7, 10], [8, 9], [8, 11], [9, 10], [10, 11]]], [[0, 0.219], [1, 0.614], [2, 0.614], [3, 0.448], [4, 0.219], [5, 0.404], [6, 1.091], [7, 0.448], [8, 0.294], [9, 0.078], [10, 0.321], [11, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 11], [6, 9], [6, 11], [7, 8], [8, 9], [8, 10], [9, 10], [10, 11]]], [[0, 0.219], [1, 0.219], [2, 0.5], [3, 0.0], [4, 0.219], [5, 0.0], [6, 0.5], [7, 0.0], [8, 0.219], [9, 0.5], [10, 0.219], [11, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 10], [7, 10], [7, 11], [8, 11], [9, 10], [9, 11]]], [[0, 0.219], [1, 1.085], [2, 0.427], [3, 0.219], [4, 0.427], [5, 0.427], [6, 0.0], [7, 1.085], [8, 0.219], [9, 0.0], [10, 0.427], [11, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 8], [6, 11], [7, 10], [7, 11], [8, 9], [9, 10], [9, 11]]], [[0, 0.219], [1, 1.263], [2, 0.278], [3, 0.626], [4, 0.626], [5, 0.5], [6, 0.294], [7, 0.5], [8, 0.278], [9, 0.0], [10, 0.626], [11, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 11], [6, 9], [6, 10], [7, 10], [7, 11], [8, 9], [8, 10], [9, 11]]], [[0, 0.219], [1, 0.5], [2, 0.5], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 1.085], [8, 0.427], [9, 0.427], [10, 0.219], [11, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 9], [6, 11], [7, 10], [7, 11], [8, 9], [8, 10], [8, 11]]], [[0, 0.219], [1, 0.278], [2, 1.263], [3, 0.626], [4, 0.626], [5, 0.294], [6, 0.5], [7, 0.5], [8, 0.0], [9, 0.278], [10, 1.091], [11, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 11], [6, 8], [6, 9], [7, 10], [7, 11], [8, 10], [8, 11], [9, 10]]], [[0, 0.219], [1, 0.427], [2, 1.085], [3, 0.427], [4, 0.219], [5, 0.0], [6, 0.427], [7, 1.085], [8, 0.0], [9, 0.219], [10, 0.219], [11, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 11], [6, 8], [6, 10], [7, 10], [7, 11], [8, 9], [8, 11], [9, 10]]], [[0, 0.219], [1, 1.164], [2, 1.164], [3, 0.427], [4, 0.427], [5, 1.0], [6, 1.0], [7, 1.085], [8, 1.0], [9, 1.0], [10, 0.219], [11, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [1], [2], [3], [4]], [[5, 10], [5, 11], [6, 10], [6, 11], [7, 8], [7, 9], [8, 9], [8, 11], [9, 10]]], [[0, 0.219], [1, 0.219], [2, 0.219], [3, 0.219], [4, 0.219], [5, 0.219], [6, 0.219], [7, 0.219], [8, 0.219], [9, 0.219], [10, 0.219], [11, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], [[5, 9], [6, 7], [6, 8], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 0.321], [1, 0.448], [2, 0.448], [3, 0.543], [4, 0.448], [5, 0.683], [6, 0.321], [7, 0.448], [8, 0.543], [9, 0.5], [10, 0.683]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], [[5, 10], [6, 7], [6, 8], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 0.321], [1, 0.448], [2, 0.448], [3, 0.219], [4, 0.0], [5, 0.321], [6, 0.427], [7, 1.085], [8, 0.427], [9, 1.085], [10, 0.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], [[5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.321], [1, 0.448], [2, 0.448], [3, 0.219], [4, 0.241], [5, 0.321], [6, 0.241], [7, 0.938], [8, 0.241], [9, 0.938], [10, 0.241]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], [[5, 8], [6, 8], [6, 10], [7, 9], [7, 10], [8, 9], [9, 10]]], [[0, 0.321], [1, 1.181], [2, 1.287], [3, 0.219], [4, 0.653], [5, 1.181], [6, 0.219], [7, 1.429], [8, 0.321], [9, 0.653], [10, 1.429]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], [[5, 9], [6, 8], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.321], [1, 0.448], [2, 0.448], [3, 0.891], [4, 0.626], [5, 0.683], [6, 0.561], [7, 1.056], [8, 0.367], [9, 0.278], [10, 0.746]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [2], [3], [4]], [[5, 9], [6, 8], [6, 10], [7, 9], [7, 10], [8, 9], [8, 10]]], [[0, 0.321], [1, 0.448], [2, 0.448], [3, 1.091], [4, 0.653], [5, 0.696], [6, 0.653], [7, 0.5], [8, 0.219], [9, 0.626], [10, 1.391]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 8], [6, 7], [6, 9], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 0.614], [1, 1.106], [2, 0.427], [3, 0.278], [4, 0.219], [5, 1.0], [6, 0.543], [7, 0.427], [8, 0.427], [9, 0.5], [10, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 9], [6, 7], [6, 8], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 0.614], [1, 0.615], [2, 0.278], [3, 0.614], [4, 0.219], [5, 0.614], [6, 0.078], [7, 0.278], [8, 0.278], [9, 0.5], [10, 1.263]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 10], [8, 10], [9, 10]]], [[0, 0.614], [1, 1.164], [2, 0.5], [3, 0.746], [4, 0.219], [5, 1.056], [6, 0.561], [7, 1.391], [8, 0.653], [9, 0.626], [10, 0.653]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 8], [6, 7], [6, 10], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 0.614], [1, 1.106], [2, 0.427], [3, 0.078], [4, 0.0], [5, 1.0], [6, 0.078], [7, 1.0], [8, 0.427], [9, 1.106], [10, 0.614]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 9], [6, 8], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.614], [1, 0.614], [2, 0.5], [3, 0.614], [4, 0.078], [5, 0.615], [6, 0.219], [7, 0.278], [8, 1.263], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.614], [1, 0.614], [2, 0.5], [3, 0.278], [4, 0.891], [5, 0.278], [6, 0.891], [7, 0.614], [8, 0.614], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 9], [6, 8], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.614], [1, 0.614], [2, 0.5], [3, 0.615], [4, 0.219], [5, 0.614], [6, 0.078], [7, 1.263], [8, 0.278], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 10], [6, 8], [6, 9], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.614], [1, 0.614], [2, 0.5], [3, 0.294], [4, 1.091], [5, 0.294], [6, 1.091], [7, 0.5], [8, 0.5], [9, 0.626], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2], [3], [4]], [[5, 10], [6, 8], [6, 10], [7, 8], [7, 9], [8, 9], [9, 10]]], [[0, 0.614], [1, 1.164], [2, 0.5], [3, 0.0], [4, 0.543], [5, 1.353], [6, 1.0], [7, 0.626], [8, 1.091], [9, 0.294], [10, 1.164]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], [[5, 9], [6, 7], [6, 8], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 0.543], [2, 1.085], [3, 0.543], [4, 0.219], [5, 1.0], [6, 0.427], [7, 0.5], [8, 0.427], [9, 1.085], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], [[5, 9], [6, 7], [6, 10], [7, 8], [8, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 0.543], [2, 1.085], [3, 0.543], [4, 0.0], [5, 1.0], [6, 0.543], [7, 1.0], [8, 0.543], [9, 1.085], [10, 1.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], [[5, 10], [6, 7], [6, 8], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 0.543], [2, 1.085], [3, 0.0], [4, 0.543], [5, 1.0], [6, 1.0], [7, 0.543], [8, 0.543], [9, 1.0], [10, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], [[5, 10], [6, 7], [6, 9], [7, 8], [8, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 0.543], [2, 1.085], [3, 0.219], [4, 0.543], [5, 1.0], [6, 0.5], [7, 0.427], [8, 0.427], [9, 0.5], [10, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], [[5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 1.0], [1, 0.891], [2, 1.426], [3, 0.219], [4, 0.891], [5, 1.0], [6, 1.164], [7, 1.0], [8, 1.0], [9, 1.164], [10, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [1], [3], [4]], [[5, 9], [6, 8], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 1.0], [1, 0.891], [2, 1.426], [3, 0.891], [4, 0.219], [5, 1.0], [6, 1.0], [7, 1.164], [8, 1.0], [9, 1.426], [10, 1.164]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 8], [6, 7], [6, 9], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 0.278], [1, 1.263], [2, 0.5], [3, 0.278], [4, 0.278], [5, 0.278], [6, 0.5], [7, 1.263], [8, 0.5], [9, 0.5], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 9], [6, 7], [6, 8], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 0.278], [1, 0.615], [2, 0.614], [3, 0.278], [4, 0.278], [5, 0.078], [6, 0.219], [7, 1.263], [8, 0.614], [9, 0.614], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 8], [6, 7], [6, 10], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 0.278], [1, 1.263], [2, 0.219], [3, 0.278], [4, 0.078], [5, 0.278], [6, 0.614], [7, 0.615], [8, 0.5], [9, 0.614], [10, 0.614]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 10], [6, 7], [6, 8], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 0.278], [1, 0.891], [2, 0.278], [3, 0.278], [4, 0.614], [5, 0.614], [6, 0.278], [7, 0.891], [8, 0.614], [9, 0.614], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 9], [6, 8], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.278], [1, 0.615], [2, 1.164], [3, 0.078], [4, 0.278], [5, 0.078], [6, 1.0], [7, 0.615], [8, 0.0], [9, 1.0], [10, 1.164]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 8], [6, 9], [6, 10], [7, 9], [7, 10], [8, 9], [8, 10]]], [[0, 0.278], [1, 1.263], [2, 0.5], [3, 0.078], [4, 0.278], [5, 0.278], [6, 0.614], [7, 0.615], [8, 0.219], [9, 0.614], [10, 0.614]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 10], [6, 8], [6, 9], [7, 9], [7, 10], [8, 9], [8, 10]]], [[0, 0.278], [1, 0.891], [2, 0.683], [3, 0.367], [4, 0.746], [5, 1.056], [6, 0.448], [7, 0.561], [8, 0.321], [9, 0.448], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [3, 4], [1], [2], [4]], [[5, 10], [6, 9], [6, 10], [7, 8], [7, 9], [8, 9], [8, 10]]], [[0, 0.278], [1, 0.543], [2, 0.5], [3, 1.0], [4, 0.614], [5, 1.106], [6, 0.427], [7, 0.219], [8, 0.427], [9, 1.085], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.219], [1, 0.653], [2, 1.391], [3, 0.448], [4, 0.626], [5, 0.653], [6, 0.448], [7, 0.5], [8, 0.696], [9, 0.321], [10, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 10], [7, 9], [7, 10], [9, 10]]], [[0, 0.219], [1, 0.626], [2, 0.626], [3, 0.0], [4, 0.219], [5, 0.219], [6, 0.0], [7, 0.626], [8, 0.0], [9, 0.219], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 10], [7, 9], [8, 9], [9, 10]]], [[0, 0.219], [1, 0.653], [2, 1.391], [3, 0.448], [4, 0.367], [5, 1.11], [6, 0.561], [7, 0.294], [8, 1.879], [9, 0.321], [10, 1.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 8], [7, 9], [9, 10]]], [[0, 0.219], [1, 0.626], [2, 0.626], [3, 0.219], [4, 0.0], [5, 0.219], [6, 0.626], [7, 0.0], [8, 0.0], [9, 0.626], [10, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 10], [7, 8], [7, 9], [9, 10]]], [[0, 0.219], [1, 0.626], [2, 0.626], [3, 0.0], [4, 0.0], [5, 0.5], [6, 0.427], [7, 0.427], [8, 1.085], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.543], [1, 1.353], [2, 1.164], [3, 0.614], [4, 0.626], [5, 0.0], [6, 1.164], [7, 0.294], [8, 0.5], [9, 1.0], [10, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.543], [1, 1.353], [2, 1.164], [3, 0.614], [4, 0.626], [5, 1.164], [6, 0.0], [7, 0.294], [8, 0.5], [9, 1.0], [10, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 7], [5, 8], [6, 9], [6, 10], [7, 9], [8, 10], [9, 10]]], [[0, 0.543], [1, 1.0], [2, 1.085], [3, 1.0], [4, 0.427], [5, 0.543], [6, 0.219], [7, 0.427], [8, 1.085], [9, 0.5], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 9], [8, 10], [9, 10]]], [[0, 0.543], [1, 1.0], [2, 1.085], [3, 1.0], [4, 0.543], [5, 0.543], [6, 0.0], [7, 1.0], [8, 1.085], [9, 0.543], [10, 1.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 9], [8, 10], [9, 10]]], [[0, 0.543], [1, 1.0], [2, 1.085], [3, 1.0], [4, 0.543], [5, 0.0], [6, 0.543], [7, 1.0], [8, 1.085], [9, 0.543], [10, 1.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 9], [5, 10], [6, 7], [6, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.543], [1, 1.0], [2, 1.085], [3, 1.0], [4, 0.427], [5, 0.219], [6, 0.543], [7, 0.427], [8, 1.085], [9, 0.5], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 7], [5, 10], [6, 9], [6, 10], [7, 8], [8, 9], [9, 10]]], [[0, 0.543], [1, 1.426], [2, 0.427], [3, 1.0], [4, 0.0], [5, 1.0], [6, 1.426], [7, 2.0], [8, 2.0], [9, 0.427], [10, 0.543]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 9], [5, 10], [6, 7], [6, 10], [7, 8], [8, 9], [9, 10]]], [[0, 0.543], [1, 1.426], [2, 0.427], [3, 1.0], [4, 0.0], [5, 1.426], [6, 1.0], [7, 2.0], [8, 2.0], [9, 0.427], [10, 0.543]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 9], [7, 10], [8, 9]]], [[0, 0.543], [1, 0.278], [2, 0.5], [3, 1.106], [4, 0.427], [5, 0.614], [6, 1.0], [7, 1.085], [8, 0.427], [9, 0.427], [10, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [3, 4], [2], [4]], [[5, 9], [5, 10], [6, 8], [6, 10], [7, 9], [7, 10], [8, 9]]], [[0, 0.543], [1, 0.278], [2, 0.5], [3, 1.106], [4, 0.427], [5, 1.0], [6, 0.614], [7, 1.085], [8, 0.427], [9, 0.427], [10, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.0], [1, 2.0], [2, 2.0], [3, 0.448], [4, 0.448], [5, 2.0], [6, 1.12], [7, 1.12], [8, 2.0], [9, 0.404], [10, 0.404]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.0], [1, 2.0], [2, 2.0], [3, 0.543], [4, 0.543], [5, 0.427], [6, 1.0], [7, 1.0], [8, 0.427], [9, 1.426], [10, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 9], [8, 10], [9, 10]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.626], [4, 0.626], [5, 0.219], [6, 0.219], [7, 0.219], [8, 0.219], [9, 0.626], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 9], [8, 10], [9, 10]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.219], [4, 0.219], [5, 0.219], [6, 0.219], [7, 0.626], [8, 0.626], [9, 0.626], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 10], [8, 9], [9, 10]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.219], [4, 0.219], [5, 0.626], [6, 0.626], [7, 0.219], [8, 0.219], [9, 0.626], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 9], [6, 10], [7, 8], [7, 10], [9, 10]]], [[0, 0.0], [1, 0.427], [2, 1.085], [3, 0.427], [4, 0.219], [5, 0.427], [6, 0.626], [7, 0.427], [8, 0.0], [9, 0.5], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 10], [8, 9], [9, 10]]], [[0, 0.0], [1, 0.0], [2, 0.0], [3, 0.367], [4, 0.367], [5, 0.367], [6, 0.367], [7, 0.367], [8, 0.367], [9, 1.333], [10, 1.333]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [7, 10], [9, 10]]], [[0, 0.0], [1, 0.427], [2, 1.085], [3, 0.321], [4, 0.0], [5, 0.448], [6, 0.427], [7, 0.219], [8, 1.085], [9, 0.448], [10, 0.321]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 10], [7, 9], [8, 9], [9, 10]]], [[0, 0.0], [1, 2.0], [2, 2.0], [3, 0.448], [4, 0.448], [5, 1.12], [6, 2.0], [7, 2.0], [8, 1.12], [9, 0.404], [10, 0.404]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 10], [7, 9], [8, 9], [9, 10]]], [[0, 0.0], [1, 2.0], [2, 2.0], [3, 0.543], [4, 0.543], [5, 1.0], [6, 0.427], [7, 0.427], [8, 1.0], [9, 1.426], [10, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 10], [6, 9], [6, 10], [7, 8], [8, 9], [9, 10]]], [[0, 0.0], [1, 0.427], [2, 1.085], [3, 0.0], [4, 0.321], [5, 0.427], [6, 0.448], [7, 1.085], [8, 0.219], [9, 0.321], [10, 0.448]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 9], [5, 10], [6, 7], [6, 10], [7, 8], [8, 9], [9, 10]]], [[0, 0.0], [1, 0.427], [2, 1.085], [3, 0.219], [4, 0.427], [5, 0.626], [6, 0.427], [7, 0.0], [8, 0.427], [9, 0.626], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 9], [7, 10], [8, 9]]], [[0, 0.0], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.427], [5, 2.0], [6, 0.0], [7, 0.0], [8, 2.0], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.427], [1, 1.106], [2, 1.164], [3, 0.427], [4, 0.448], [5, 1.164], [6, 0.404], [7, 1.106], [8, 0.448], [9, 0.666], [10, 0.404]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.427], [1, 1.106], [2, 1.164], [3, 0.427], [4, 0.543], [5, 0.219], [6, 1.0], [7, 0.367], [8, 1.085], [9, 1.0], [10, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 9], [8, 10], [9, 10]]], [[0, 0.427], [1, 0.0], [2, 1.085], [3, 0.427], [4, 0.626], [5, 0.427], [6, 0.219], [7, 0.0], [8, 0.5], [9, 0.427], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 9], [8, 10], [9, 10]]], [[0, 0.427], [1, 0.0], [2, 1.085], [3, 0.427], [4, 0.448], [5, 0.0], [6, 0.321], [7, 1.085], [8, 0.448], [9, 0.219], [10, 0.321]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 9], [5, 10], [6, 7], [6, 9], [7, 8], [8, 10], [9, 10]]], [[0, 0.427], [1, 1.106], [2, 0.614], [3, 0.427], [4, 0.427], [5, 0.543], [6, 1.0], [7, 0.219], [8, 1.085], [9, 0.278], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 9], [5, 10], [6, 7], [6, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.427], [1, 0.0], [2, 0.427], [3, 2.0], [4, 0.0], [5, 0.427], [6, 0.427], [7, 2.0], [8, 0.427], [9, 0.0], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 8], [5, 10], [6, 8], [6, 9], [7, 9], [7, 10], [9, 10]]], [[0, 0.427], [1, 0.427], [2, 0.5], [3, 0.427], [4, 0.0], [5, 0.0], [6, 0.427], [7, 0.626], [8, 1.085], [9, 0.626], [10, 0.219]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 9], [5, 10], [6, 7], [6, 10], [7, 8], [8, 9], [9, 10]]], [[0, 0.427], [1, 2.0], [2, 0.427], [3, 0.427], [4, 0.427], [5, 0.427], [6, 0.427], [7, 0.427], [8, 2.0], [9, 0.427], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 9], [7, 10], [8, 9]]], [[0, 0.427], [1, 0.427], [2, 0.5], [3, 2.0], [4, 0.427], [5, 0.427], [6, 2.0], [7, 0.427], [8, 0.427], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [3, 4], [2], [4]], [[5, 9], [5, 10], [6, 9], [6, 10], [7, 8], [7, 10], [8, 9]]], [[0, 0.427], [1, 1.426], [2, 0.543], [3, 2.0], [4, 0.427], [5, 1.0], [6, 1.426], [7, 0.0], [8, 2.0], [9, 1.0], [10, 0.543]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.219], [1, 1.263], [2, 0.278], [3, 0.614], [4, 0.614], [5, 0.5], [6, 0.278], [7, 0.614], [8, 0.615], [9, 0.278], [10, 0.078]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.219], [1, 1.263], [2, 0.278], [3, 0.614], [4, 0.614], [5, 0.5], [6, 0.278], [7, 0.615], [8, 0.614], [9, 0.278], [10, 0.078]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 9], [8, 10], [9, 10]]], [[0, 0.219], [1, 0.5], [2, 0.5], [3, 1.0], [4, 1.0], [5, 1.085], [6, 1.085], [7, 0.543], [8, 0.543], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 9], [8, 10], [9, 10]]], [[0, 0.219], [1, 1.164], [2, 1.164], [3, 1.0], [4, 1.0], [5, 1.426], [6, 1.426], [7, 0.891], [8, 0.891], [9, 1.0], [10, 1.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 7], [5, 9], [6, 8], [6, 10], [7, 10], [8, 9], [9, 10]]], [[0, 0.219], [1, 0.5], [2, 0.5], [3, 1.0], [4, 1.0], [5, 1.085], [6, 1.085], [7, 0.543], [8, 0.543], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 10], [8, 9], [9, 10]]], [[0, 0.219], [1, 1.164], [2, 1.164], [3, 1.0], [4, 1.0], [5, 1.426], [6, 1.426], [7, 0.891], [8, 0.891], [9, 1.0], [10, 1.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 7], [5, 10], [6, 8], [6, 10], [7, 9], [8, 9], [9, 10]]], [[0, 0.219], [1, 0.278], [2, 1.263], [3, 0.614], [4, 0.614], [5, 0.278], [6, 0.5], [7, 0.615], [8, 0.614], [9, 0.078], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 8], [5, 10], [6, 7], [6, 10], [7, 9], [8, 9], [9, 10]]], [[0, 0.219], [1, 0.278], [2, 1.263], [3, 0.614], [4, 0.614], [5, 0.278], [6, 0.5], [7, 0.614], [8, 0.615], [9, 0.078], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 9], [7, 10], [8, 10]]], [[0, 0.219], [1, 1.085], [2, 0.427], [3, 1.0], [4, 1.106], [5, 1.426], [6, 0.427], [7, 1.0], [8, 1.164], [9, 0.543], [10, 0.367]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 9], [5, 10], [6, 9], [6, 10], [7, 8], [7, 9], [8, 10]]], [[0, 0.219], [1, 1.085], [2, 1.085], [3, 1.12], [4, 1.12], [5, 2.0], [6, 2.0], [7, 0.626], [8, 0.626], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 9], [7, 10], [8, 9]]], [[0, 0.219], [1, 0.427], [2, 1.085], [3, 1.106], [4, 1.0], [5, 0.427], [6, 1.426], [7, 1.0], [8, 1.164], [9, 0.367], [10, 0.543]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [2, 4], [3, 4], [3, 4], [1], [2]], [[5, 9], [5, 10], [6, 9], [6, 10], [7, 8], [7, 10], [8, 9]]], [[0, 0.219], [1, 1.085], [2, 1.085], [3, 1.12], [4, 1.12], [5, 2.0], [6, 2.0], [7, 0.626], [8, 0.626], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3], [4]], [[5, 8], [6, 9], [7, 8], [7, 9], [8, 9]]], [[0, 1.056], [1, 0.746], [2, 0.626], [3, 1.164], [4, 1.11], [5, 1.47], [6, 0.294], [7, 0.653], [8, 0.5], [9, 1.391]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3], [4]], [[5, 9], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 1.056], [1, 0.746], [2, 0.626], [3, 1.164], [4, 0.404], [5, 0.561], [6, 0.615], [7, 0.448], [8, 0.683], [9, 0.448]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [3, 4], [2], [4]], [[5, 9], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 0.321], [1, 1.879], [2, 0.448], [3, 1.612], [4, 0.321], [5, 0.561], [6, 1.612], [7, 1.879], [8, 0.561], [9, 0.448]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2], [4]], [[5, 8], [6, 9], [7, 8], [7, 9], [8, 9]]], [[0, 0.938], [1, 0.938], [2, 0.5], [3, 2.0], [4, 0.938], [5, 2.0], [6, 0.938], [7, 1.5], [8, 1.5], [9, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2], [4]], [[5, 9], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 0.938], [1, 0.938], [2, 0.5], [3, 2.0], [4, 0.938], [5, 0.938], [6, 2.0], [7, 1.5], [8, 1.5], [9, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3], [4]], [[5, 8], [6, 9], [7, 8], [7, 9], [8, 9]]], [[0, 0.871], [1, 1.091], [2, 1.091], [3, 1.164], [4, 1.164], [5, 1.106], [6, 1.106], [7, 0.5], [8, 1.085], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3], [4]], [[5, 9], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 0.871], [1, 1.091], [2, 1.091], [3, 1.164], [4, 1.164], [5, 1.106], [6, 1.106], [7, 0.5], [8, 1.085], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2], [4]], [[5, 8], [6, 9], [7, 8], [7, 9], [8, 9]]], [[0, 1.353], [1, 1.353], [2, 0.891], [3, 1.612], [4, 1.164], [5, 1.612], [6, 1.106], [7, 1.164], [8, 1.106], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2], [4]], [[5, 9], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 1.353], [1, 1.164], [2, 1.263], [3, 1.612], [4, 1.164], [5, 1.353], [6, 1.426], [7, 1.426], [8, 1.085], [9, 1.263]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [3, 4], [1], [2]], [[5, 8], [6, 9], [7, 8], [7, 9], [8, 9]]], [[0, 0.871], [1, 1.263], [2, 1.263], [3, 2.0], [4, 2.0], [5, 0.871], [6, 0.871], [7, 0.871], [8, 1.263], [9, 1.263]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [3, 4], [1], [2]], [[5, 9], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 0.871], [1, 0.615], [2, 0.615], [3, 2.0], [4, 2.0], [5, 0.666], [6, 0.666], [7, 0.871], [8, 0.615], [9, 0.615]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3], [2, 4], [3, 4], [4]], [[5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 0.561], [1, 1.181], [2, 2.0], [3, 1.426], [4, 0.626], [5, 0.561], [6, 0.891], [7, 1.12], [8, 1.741], [9, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3], [2, 4], [3, 4], [4]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.561], [1, 1.879], [2, 0.448], [3, 1.612], [4, 0.448], [5, 0.321], [6, 1.612], [7, 0.561], [8, 1.879], [9, 0.321]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3], [2, 4], [3, 4], [4]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.561], [1, 0.746], [2, 0.626], [3, 1.164], [4, 0.448], [5, 1.056], [6, 0.615], [7, 0.448], [8, 0.683], [9, 0.404]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [3]], [[5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.12], [1, 0.448], [2, 2.0], [3, 1.091], [4, 2.0], [5, 0.696], [6, 0.448], [7, 1.12], [8, 0.696], [9, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [3]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.12], [1, 2.0], [2, 0.448], [3, 1.091], [4, 2.0], [5, 0.696], [6, 1.12], [7, 0.448], [8, 0.696], [9, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [2, 4], [3, 4], [3]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.12], [1, 0.626], [2, 0.626], [3, 0.891], [4, 2.0], [5, 1.741], [6, 0.561], [7, 0.561], [8, 1.181], [9, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [3, 4], [2]], [[5, 7], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 0.404], [1, 0.448], [2, 0.448], [3, 0.615], [4, 1.056], [5, 0.683], [6, 0.626], [7, 1.164], [8, 0.746], [9, 0.561]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [3, 4], [2]], [[5, 8], [6, 7], [6, 9], [7, 9], [8, 9]]], [[0, 0.404], [1, 0.448], [2, 0.448], [3, 0.615], [4, 1.056], [5, 0.683], [6, 0.626], [7, 0.746], [8, 1.164], [9, 0.561]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [3, 4], [2]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.404], [1, 1.181], [2, 1.287], [3, 0.404], [4, 1.181], [5, 1.181], [6, 0.404], [7, 1.287], [8, 1.181], [9, 0.404]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 4], [3, 4], [3, 4], [2]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.404], [1, 1.181], [2, 1.287], [3, 0.404], [4, 1.181], [5, 1.181], [6, 0.404], [7, 1.181], [8, 1.287], [9, 0.404]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 2], [2, 3], [3, 4], [4]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.294], [1, 1.11], [2, 1.391], [3, 1.164], [4, 0.746], [5, 1.056], [6, 0.653], [7, 0.5], [8, 1.47], [9, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 2], [2, 3], [3, 4], [4]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.294], [1, 1.091], [2, 1.091], [3, 1.426], [4, 0.615], [5, 1.106], [6, 0.294], [7, 1.106], [8, 0.615], [9, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 3], [2, 4], [4]], [[5, 7], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.106], [1, 1.106], [2, 2.0], [3, 1.106], [4, 0.219], [5, 1.106], [6, 0.219], [7, 2.0], [8, 1.5], [9, 1.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 3], [2, 4], [4]], [[5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.106], [1, 0.615], [2, 1.426], [3, 1.426], [4, 1.091], [5, 0.294], [6, 0.615], [7, 1.106], [8, 0.294], [9, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 3], [2, 4], [4]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.106], [1, 1.164], [2, 1.085], [3, 1.164], [4, 1.091], [5, 0.871], [6, 1.106], [7, 1.085], [8, 0.5], [9, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 3], [2, 4], [4]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.106], [1, 1.164], [2, 1.085], [3, 1.612], [4, 0.891], [5, 1.353], [6, 1.612], [7, 1.164], [8, 1.106], [9, 1.353]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2, 4], [3]], [[5, 7], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 0.615], [1, 1.106], [2, 1.426], [3, 0.294], [4, 0.615], [5, 1.426], [6, 1.091], [7, 1.106], [8, 0.294], [9, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2, 4], [3]], [[5, 8], [6, 7], [6, 9], [7, 9], [8, 9]]], [[0, 0.615], [1, 1.106], [2, 1.426], [3, 0.294], [4, 0.615], [5, 1.426], [6, 1.091], [7, 0.294], [8, 1.106], [9, 1.091]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2, 4], [3]], [[5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 0.615], [1, 0.615], [2, 0.871], [3, 0.615], [4, 0.666], [5, 0.615], [6, 0.666], [7, 2.0], [8, 2.0], [9, 0.871]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2, 4], [3]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.615], [1, 1.164], [2, 0.683], [3, 0.746], [4, 0.404], [5, 1.056], [6, 0.561], [7, 0.448], [8, 0.448], [9, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [2, 4], [3]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.615], [1, 1.164], [2, 0.683], [3, 0.746], [4, 0.404], [5, 1.056], [6, 0.561], [7, 0.448], [8, 0.448], [9, 0.626]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [3, 4], [2]], [[5, 7], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.164], [1, 1.106], [2, 1.085], [3, 0.871], [4, 1.106], [5, 1.164], [6, 1.091], [7, 1.085], [8, 1.091], [9, 0.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [3, 4], [2]], [[5, 8], [6, 7], [6, 9], [7, 9], [8, 9]]], [[0, 1.164], [1, 0.615], [2, 0.683], [3, 1.056], [4, 0.561], [5, 0.746], [6, 0.404], [7, 0.448], [8, 0.626], [9, 0.448]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [3, 4], [2]], [[5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.164], [1, 1.106], [2, 1.085], [3, 1.353], [4, 1.612], [5, 1.612], [6, 0.891], [7, 1.106], [8, 1.353], [9, 1.164]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [3, 4], [2]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.164], [1, 2.166], [2, 1.164], [3, 1.333], [4, 1.164], [5, 1.333], [6, 1.333], [7, 1.164], [8, 2.166], [9, 1.333]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3], [2, 4], [3, 4], [2]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.164], [1, 1.353], [2, 1.263], [3, 1.353], [4, 1.426], [5, 1.612], [6, 1.164], [7, 1.085], [8, 1.263], [9, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [3, 4], [1]], [[5, 7], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.426], [1, 0.615], [2, 1.106], [3, 0.294], [4, 1.106], [5, 0.615], [6, 1.091], [7, 1.426], [8, 1.091], [9, 0.294]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [3, 4], [1]], [[5, 8], [6, 7], [6, 9], [7, 9], [8, 9]]], [[0, 1.426], [1, 0.891], [2, 1.741], [3, 0.561], [4, 0.561], [5, 1.181], [6, 0.626], [7, 0.626], [8, 2.0], [9, 1.12]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [3, 4], [1]], [[5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.426], [1, 1.263], [2, 1.085], [3, 1.164], [4, 1.612], [5, 1.353], [6, 1.263], [7, 1.426], [8, 1.353], [9, 1.164]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [3, 4], [1]], [[5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.426], [1, 1.263], [2, 1.085], [3, 1.612], [4, 1.164], [5, 1.353], [6, 1.426], [7, 1.263], [8, 1.353], [9, 1.164]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3], [2, 4], [3, 4], [1]], [[5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.426], [1, 2.5], [2, 1.426], [3, 1.426], [4, 1.426], [5, 1.426], [6, 1.426], [7, 1.426], [8, 2.5], [9, 1.426]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 3, 4], [4]], [[5, 8], [6, 8], [7, 8]]], [[0, 1.444], [1, 1.814], [2, 1.814], [3, 2.0], [4, 1.814], [5, 1.444], [6, 1.444], [7, 1.444], [8, 1.814]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3, 4], [2]], [[5, 8], [6, 8], [7, 8]]], [[0, 1.787], [1, 1.787], [2, 2.5], [3, 2.0], [4, 2.0], [5, 2.0], [6, 2.0], [7, 1.787], [8, 1.787]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3], [2, 4], [3, 4]], [[6, 7], [6, 8], [7, 8]]], [[0, 2.0], [1, 1.181], [2, 1.181], [3, 0.871], [4, 0.871], [5, 2.0], [6, 1.11], [7, 1.11], [8, 2.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9]]], [[0, 0.219], [1, 1.5], [2, 1.5], [3, 1.106], [4, 1.106], [5, 0.219], [6, 2.0], [7, 2.0], [8, 1.106], [9, 1.106]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [3, 4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8]]], [[0, 0.219], [1, 1.5], [2, 1.5], [3, 1.106], [4, 1.106], [5, 0.219], [6, 2.0], [7, 2.0], [8, 1.106], [9, 1.106]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 8], [7, 9], [8, 9]]], [[0, 0.891], [1, 1.741], [2, 1.426], [3, 1.12], [4, 1.181], [5, 0.626], [6, 0.626], [7, 0.561], [8, 0.561], [9, 2.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 6], [5, 8], [6, 7], [7, 9], [8, 9]]], [[0, 0.891], [1, 1.741], [2, 1.426], [3, 1.12], [4, 1.181], [5, 0.626], [6, 0.626], [7, 0.561], [8, 0.561], [9, 2.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 7], [5, 8], [6, 7], [6, 9], [8, 9]]], [[0, 0.891], [1, 1.353], [2, 1.353], [3, 1.106], [4, 1.106], [5, 1.612], [6, 1.164], [7, 1.612], [8, 1.164], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 7], [5, 9], [6, 7], [6, 8], [8, 9]]], [[0, 0.891], [1, 1.353], [2, 1.353], [3, 1.106], [4, 1.106], [5, 1.164], [6, 1.612], [7, 1.612], [8, 1.164], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9]]], [[0, 0.891], [1, 1.353], [2, 1.353], [3, 1.106], [4, 1.106], [5, 1.612], [6, 1.164], [7, 1.164], [8, 1.612], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9]]], [[0, 0.891], [1, 1.353], [2, 1.353], [3, 1.106], [4, 1.106], [5, 1.164], [6, 1.612], [7, 1.164], [8, 1.612], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 8]]], [[0, 0.891], [1, 1.426], [2, 1.741], [3, 1.181], [4, 1.12], [5, 0.561], [6, 0.561], [7, 0.626], [8, 0.626], [9, 2.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 3], [2, 4], [2, 4], [3, 4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8]]], [[0, 0.891], [1, 1.426], [2, 1.741], [3, 1.181], [4, 1.12], [5, 0.561], [6, 0.561], [7, 0.626], [8, 0.626], [9, 2.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 8], [6, 7], [7, 9], [8, 9]]], [[0, 2.0], [1, 2.5], [2, 2.0], [3, 2.0], [4, 2.0], [5, 2.0], [6, 2.0], [7, 2.0], [8, 2.0], [9, 2.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 9], [7, 8], [8, 9]]], [[0, 2.0], [1, 1.085], [2, 1.085], [3, 2.0], [4, 1.5], [5, 1.085], [6, 0.5], [7, 1.085], [8, 0.5], [9, 1.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 7], [5, 8], [6, 7], [6, 9], [8, 9]]], [[0, 2.0], [1, 1.106], [2, 1.106], [3, 2.0], [4, 1.5], [5, 1.106], [6, 0.219], [7, 1.106], [8, 0.219], [9, 1.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 9], [6, 7], [7, 8], [8, 9]]], [[0, 2.0], [1, 1.085], [2, 1.085], [3, 2.0], [4, 2.0], [5, 1.085], [6, 2.0], [7, 2.0], [8, 1.085], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9]]], [[0, 2.0], [1, 1.106], [2, 1.106], [3, 1.5], [4, 2.0], [5, 0.219], [6, 1.106], [7, 0.219], [8, 1.106], [9, 1.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8]]], [[0, 2.0], [1, 2.0], [2, 2.5], [3, 2.0], [4, 2.0], [5, 2.0], [6, 2.0], [7, 2.0], [8, 2.0], [9, 2.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3, 4]], [[5, 7], [6, 8], [7, 8]]], [[0, 1.747], [1, 0.746], [2, 1.816], [3, 1.747], [4, 1.746], [5, 1.746], [6, 0.746], [7, 0.5], [8, 1.816]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3], [1, 3, 4], [2, 4], [3, 4]], [[5, 8], [6, 7], [7, 8]]], [[0, 1.747], [1, 1.879], [2, 2.0], [3, 2.166], [4, 1.879], [5, 1.47], [6, 1.747], [7, 2.0], [8, 1.47]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2, 4]], [[5, 7], [6, 8], [7, 8]]], [[0, 2.157], [1, 2.157], [2, 2.5], [3, 2.157], [4, 2.157], [5, 2.157], [6, 2.157], [7, 2.5], [8, 2.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [1, 3, 4], [2, 3], [2, 4]], [[5, 8], [6, 7], [7, 8]]], [[0, 2.157], [1, 2.157], [2, 2.5], [3, 2.157], [4, 2.157], [5, 2.157], [6, 2.157], [7, 2.5], [8, 2.5]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3, 4]], [[5, 7], [6, 8], [7, 8]]], [[0, 0.871], [1, 2.5], [2, 1.11], [3, 2.0], [4, 2.0], [5, 0.871], [6, 1.181], [7, 1.11], [8, 1.181]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 2], [3, 4]], [[5, 8], [6, 7], [7, 8]]], [[0, 0.871], [1, 1.11], [2, 2.5], [3, 2.0], [4, 2.0], [5, 1.181], [6, 0.871], [7, 1.11], [8, 1.181]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2, 4]], [[5, 7], [6, 8], [7, 8]]], [[0, 2.166], [1, 1.47], [2, 1.47], [3, 1.747], [4, 1.747], [5, 1.879], [6, 1.879], [7, 2.0], [8, 2.0]]],
[[[1, 0, 0, 0, 0, 0], [[1, 3, 4], [2, 3, 4], [1, 3], [2, 4]], [[5, 8], [6, 7], [7, 8]]], [[0, 2.166], [1, 2.166], [2, 2.166], [3, 2.166], [4, 2.166], [5, 2.166], [6, 2.166], [7, 2.166], [8, 2.166]]],
[[[1, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [2, 3, 4]], [[6, 7]]], [[0, 2.166], [1, 2.357], [2, 2.357], [3, 2.166], [4, 2.166], [5, 2.166], [6, 2.357], [7, 2.357]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 8], [6, 9], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.626], [1, 1.091], [2, 0.696], [3, 0.5], [4, 0.219], [5, 0.448], [6, 1.391], [7, 0.321], [8, 0.448], [9, 0.653], [10, 0.653]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.626], [1, 1.091], [2, 0.5], [3, 0.294], [4, 0.543], [5, 0.614], [6, 1.164], [7, 1.0], [8, 1.164], [9, 0.0], [10, 1.353]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.626], [1, 1.091], [2, 0.294], [3, 0.5], [4, 0.543], [5, 1.164], [6, 0.614], [7, 1.0], [8, 0.0], [9, 1.164], [10, 1.353]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.626], [1, 1.091], [2, 0.5], [3, 0.696], [4, 0.219], [5, 1.391], [6, 0.448], [7, 0.321], [8, 0.653], [9, 0.448], [10, 0.653]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 10], [7, 8], [7, 9], [7, 10], [9, 10]]], [[0, 0.626], [1, 0.626], [2, 0.5], [3, 0.219], [4, 0.427], [5, 0.427], [6, 0.0], [7, 0.427], [8, 0.427], [9, 0.0], [10, 1.085]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [7, 10], [9, 10]]], [[0, 0.626], [1, 0.626], [2, 0.5], [3, 0.5], [4, 0.427], [5, 1.085], [6, 0.427], [7, 0.427], [8, 0.427], [9, 1.085], [10, 0.5]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 10], [7, 8], [7, 9], [8, 9], [9, 10]]], [[0, 0.626], [1, 1.091], [2, 0.5], [3, 0.294], [4, 0.626], [5, 0.5], [6, 0.294], [7, 0.614], [8, 0.5], [9, 0.614], [10, 1.091]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 9], [6, 10], [7, 8], [7, 9], [7, 10], [8, 10]]], [[0, 0.626], [1, 0.626], [2, 0.5], [3, 0.5], [4, 0.427], [5, 0.427], [6, 1.085], [7, 0.427], [8, 1.085], [9, 0.427], [10, 0.5]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [7, 10], [8, 10]]], [[0, 0.626], [1, 0.626], [2, 0.219], [3, 0.5], [4, 0.427], [5, 0.0], [6, 0.427], [7, 0.427], [8, 0.0], [9, 0.427], [10, 1.085]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 9], [6, 10], [7, 8], [7, 9], [8, 9], [8, 10]]], [[0, 0.626], [1, 1.091], [2, 0.294], [3, 0.5], [4, 0.626], [5, 0.294], [6, 0.5], [7, 0.614], [8, 0.614], [9, 0.5], [10, 1.091]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [3, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 10], [7, 8], [7, 9], [7, 10], [8, 9]]], [[0, 0.626], [1, 0.626], [2, 0.219], [3, 0.219], [4, 0.626], [5, 0.219], [6, 0.219], [7, 0.0], [8, 0.0], [9, 0.0], [10, 0.626]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2], [3], [4]], [[5, 9], [6, 7], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 1.181], [1, 2.0], [2, 0.561], [3, 0.561], [4, 0.891], [5, 1.426], [6, 1.12], [7, 0.626], [8, 0.626], [9, 1.741]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 4], [1], [3], [4]], [[5, 8], [6, 7], [6, 9], [7, 8], [7, 9], [8, 9]]], [[0, 0.746], [1, 0.626], [2, 1.056], [3, 1.47], [4, 0.294], [5, 1.164], [6, 1.11], [7, 0.653], [8, 0.5], [9, 1.391]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 4], [1], [3], [4]], [[5, 9], [6, 7], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 0.746], [1, 0.626], [2, 1.056], [3, 0.561], [4, 0.615], [5, 1.164], [6, 0.404], [7, 0.448], [8, 0.448], [9, 0.683]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3], [4]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 0.653], [1, 2.5], [2, 0.653], [3, 0.294], [4, 0.653], [5, 0.294], [6, 0.653], [7, 0.294], [8, 0.294], [9, 2.5]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.653], [1, 1.391], [2, 0.653], [3, 0.5], [4, 0.448], [5, 0.5], [6, 0.448], [7, 0.683], [8, 1.263], [9, 0.683]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.653], [1, 1.391], [2, 1.11], [3, 0.5], [4, 0.626], [5, 0.294], [6, 1.056], [7, 1.47], [8, 1.164], [9, 0.746]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3], [4]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 0.448], [1, 2.0], [2, 1.12], [3, 0.696], [4, 0.448], [5, 1.12], [6, 1.091], [7, 2.0], [8, 1.091], [9, 0.696]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 0.448], [1, 0.448], [2, 0.683], [3, 0.683], [4, 0.653], [5, 0.653], [6, 1.263], [7, 0.5], [8, 0.5], [9, 1.391]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.448], [1, 0.448], [2, 0.683], [3, 0.404], [4, 0.561], [5, 0.626], [6, 0.615], [7, 1.164], [8, 1.056], [9, 0.746]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.448], [1, 0.448], [2, 0.404], [3, 0.683], [4, 0.626], [5, 0.561], [6, 0.615], [7, 1.056], [8, 1.164], [9, 0.746]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [3, 4], [2], [3]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.5], [1, 1.5], [2, 0.5], [3, 0.5], [4, 2.0], [5, 2.0], [6, 1.085], [7, 1.085], [8, 1.085], [9, 1.085]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [3, 4], [2], [3]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.5], [1, 1.5], [2, 0.219], [3, 0.219], [4, 2.0], [5, 2.0], [6, 1.106], [7, 1.106], [8, 1.106], [9, 1.106]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 4], [3, 4], [2], [3]], [[5, 8], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.5], [1, 1.5], [2, 0.5], [3, 0.5], [4, 2.0], [5, 2.0], [6, 0.938], [7, 0.938], [8, 0.938], [9, 0.938]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3], [2, 4], [3, 4], [1], [4]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 0.626], [1, 0.746], [2, 1.056], [3, 1.47], [4, 0.653], [5, 1.164], [6, 1.11], [7, 0.5], [8, 0.294], [9, 1.391]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3], [2, 4], [3, 4], [1], [4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 0.626], [1, 0.746], [2, 1.056], [3, 0.561], [4, 0.448], [5, 1.164], [6, 0.404], [7, 0.448], [8, 0.615], [9, 0.683]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3], [2, 4], [3, 4], [1], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 8], [8, 9]]], [[0, 0.626], [1, 0.626], [2, 1.12], [3, 1.741], [4, 0.561], [5, 0.891], [6, 2.0], [7, 1.426], [8, 0.561], [9, 1.181]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3], [2, 4], [3, 4], [1], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.626], [1, 0.746], [2, 0.561], [3, 1.056], [4, 0.448], [5, 1.164], [6, 0.448], [7, 0.404], [8, 0.615], [9, 0.683]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3], [2, 4], [3, 4], [1], [4]], [[5, 8], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.626], [1, 1.814], [2, 1.747], [3, 1.747], [4, 0.626], [5, 1.333], [6, 1.747], [7, 1.747], [8, 1.333], [9, 1.814]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [2, 4], [3, 4], [1], [3]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.091], [1, 1.091], [2, 0.871], [3, 0.5], [4, 1.106], [5, 1.164], [6, 1.164], [7, 1.085], [8, 1.106], [9, 1.085]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [2, 4], [3, 4], [1], [3]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.091], [1, 1.091], [2, 0.871], [3, 0.5], [4, 1.106], [5, 1.164], [6, 1.164], [7, 1.085], [8, 1.106], [9, 1.085]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [2, 4], [3, 4], [1], [3]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 8], [8, 9]]], [[0, 1.091], [1, 1.091], [2, 0.294], [3, 0.294], [4, 1.106], [5, 0.615], [6, 1.426], [7, 1.426], [8, 1.106], [9, 0.615]]],
[[[1, 1, 0, 0, 0, 0], [[2, 4], [2, 4], [3, 4], [1], [3]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.091], [1, 1.091], [2, 0.294], [3, 0.294], [4, 1.106], [5, 1.426], [6, 0.615], [7, 1.426], [8, 1.106], [9, 0.615]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2, 3], [2, 4], [3, 4], [4]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 0.674], [1, 3.0], [2, 0.674], [3, 0.674], [4, 0.638], [5, 0.674], [6, 0.638], [7, 0.638], [8, 0.638]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3], [3, 4], [4]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.181], [1, 1.287], [2, 1.181], [3, 0.696], [4, 1.11], [5, 0.696], [6, 1.11], [7, 1.429], [8, 1.429]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 4], [3, 4], [3]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.746], [1, 1.816], [2, 0.746], [3, 0.5], [4, 1.747], [5, 1.747], [6, 0.746], [7, 1.816], [8, 1.746]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 2], [3, 4], [4]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 0.746], [1, 1.816], [2, 1.746], [3, 1.747], [4, 0.746], [5, 1.747], [6, 0.5], [7, 1.746], [8, 1.816]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2, 3], [4]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.181], [1, 1.181], [2, 2.0], [3, 2.0], [4, 1.11], [5, 0.871], [6, 1.11], [7, 0.871], [8, 2.5]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [1, 4], [2, 4], [3]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.879], [1, 2.0], [2, 1.747], [3, 1.47], [4, 1.747], [5, 2.166], [6, 2.0], [7, 1.879], [8, 1.47]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 4], [3, 4], [1]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.814], [1, 1.814], [2, 1.444], [3, 1.444], [4, 1.444], [5, 2.0], [6, 1.814], [7, 1.814], [8, 1.444]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]], [[0, 1.11], [1, 1.429], [2, 1.429], [3, 0.696], [4, 1.181], [5, 1.11], [6, 0.696], [7, 1.181], [8, 1.287]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3, 4]], [[5, 6], [5, 8], [6, 7], [7, 8]]], [[0, 1.11], [1, 1.429], [2, 1.429], [3, 0.696], [4, 1.181], [5, 1.11], [6, 0.696], [7, 1.287], [8, 1.181]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2], [2, 4], [3, 4], [3, 4]], [[5, 7], [5, 8], [6, 7], [6, 8]]], [[0, 1.11], [1, 2.5], [2, 1.11], [3, 0.871], [4, 1.181], [5, 0.871], [6, 1.181], [7, 2.0], [8, 2.0]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]], [[0, 2.0], [1, 1.879], [2, 1.747], [3, 1.47], [4, 2.0], [5, 1.747], [6, 2.166], [7, 1.879], [8, 1.47]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3, 4]], [[5, 6], [5, 8], [6, 7], [7, 8]]], [[0, 2.0], [1, 1.879], [2, 1.47], [3, 1.747], [4, 2.0], [5, 1.747], [6, 2.166], [7, 1.47], [8, 1.879]]],
[[[1, 1, 0, 0, 0, 0], [[1, 4], [2, 3], [2, 4], [3, 4]], [[5, 7], [5, 8], [6, 7], [6, 8]]], [[0, 2.0], [1, 2.0], [2, 1.741], [3, 1.741], [4, 2.0], [5, 2.0], [6, 2.5], [7, 1.741], [8, 1.741]]],
[[[1, 1, 0, 0, 0, 0], [[1, 2, 4], [2, 3, 4], [3, 4]], [[5, 7], [6, 7]]], [[0, 2.302], [1, 2.719], [2, 2.302], [3, 2.139], [4, 2.302], [5, 2.139], [6, 2.302], [7, 2.719]]],
[[[1, 1, 0, 0, 0, 0], [[2, 3, 4], [2, 3, 4], [1, 4]], [[5, 7], [6, 7]]], [[0, 2.357], [1, 2.357], [2, 2.166], [3, 2.166], [4, 2.357], [5, 2.166], [6, 2.166], [7, 2.357]]],
[[[1, 1, 0, 0, 1, 1], [[1, 2, 3, 4]], []], [[0, 3.0], [1, 3.0], [2, 3.0], [3, 3.0], [4, 3.0], [5, 3.0]]],
[[[1, 1, 0, 0, 1, 1], [[1], [2], [3], [4]], [[5, 6], [5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 3.0], [1, 0.674], [2, 0.674], [3, 0.674], [4, 0.674], [5, 0.638], [6, 0.638], [7, 0.638], [8, 0.638]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 8], [6, 7], [6, 9], [7, 10], [8, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 1.085], [2, 0.427], [3, 0.543], [4, 0.278], [5, 0.427], [6, 1.0], [7, 0.219], [8, 0.427], [9, 1.106], [10, 0.614]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [7, 10], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.427], [2, 1.085], [3, 0.5], [4, 0.219], [5, 0.427], [6, 1.0], [7, 0.543], [8, 0.543], [9, 1.085], [10, 1.0]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 8], [7, 10], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.5], [2, 0.5], [3, 1.263], [4, 0.278], [5, 0.5], [6, 0.278], [7, 0.5], [8, 1.263], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [7, 10], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.614], [2, 0.614], [3, 1.263], [4, 0.278], [5, 0.219], [6, 0.078], [7, 0.615], [8, 0.614], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 6], [5, 7], [6, 10], [7, 8], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 1.085], [2, 0.427], [3, 0.427], [4, 1.085], [5, 0.427], [6, 0.427], [7, 0.5], [8, 0.626], [9, 0.626], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 8], [6, 7], [6, 10], [7, 9], [8, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 1.085], [2, 0.427], [3, 0.219], [4, 0.5], [5, 1.0], [6, 0.427], [7, 0.543], [8, 0.543], [9, 1.0], [10, 1.085]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 9], [6, 7], [6, 10], [7, 8], [8, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 1.263], [2, 0.278], [3, 0.5], [4, 0.5], [5, 0.5], [6, 0.278], [7, 0.278], [8, 0.278], [9, 0.5], [10, 1.263]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 8], [6, 9], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.683], [2, 0.543], [3, 0.543], [4, 0.683], [5, 0.448], [6, 0.448], [7, 0.448], [8, 0.321], [9, 0.321], [10, 0.448]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.5], [2, 0.5], [3, 0.5], [4, 0.5], [5, 1.391], [6, 1.391], [7, 0.653], [8, 0.653], [9, 0.653], [10, 0.653]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 1.164], [2, 1.164], [3, 0.5], [4, 0.5], [5, 1.164], [6, 1.164], [7, 1.333], [8, 1.333], [9, 1.164], [10, 1.164]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 7], [6, 9], [7, 8], [8, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 1.263], [2, 0.278], [3, 0.614], [4, 0.614], [5, 0.219], [6, 0.078], [7, 0.278], [8, 0.278], [9, 0.615], [10, 0.614]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.5], [2, 0.5], [3, 1.164], [4, 1.164], [5, 1.164], [6, 1.164], [7, 1.164], [8, 1.164], [9, 1.333], [10, 1.333]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.614], [2, 0.614], [3, 0.614], [4, 0.614], [5, 0.891], [6, 0.891], [7, 0.278], [8, 0.278], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 7], [6, 8], [7, 8], [7, 9], [8, 10], [9, 10]]], [[0, 0.5], [1, 0.543], [2, 0.683], [3, 0.683], [4, 0.543], [5, 0.448], [6, 0.448], [7, 0.321], [8, 0.448], [9, 0.448], [10, 0.321]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.5], [1, 0.5], [2, 0.5], [3, 0.5], [4, 0.5], [5, 1.263], [6, 1.263], [7, 0.278], [8, 0.278], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 10], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.5], [1, 0.614], [2, 0.614], [3, 0.5], [4, 0.5], [5, 1.091], [6, 1.091], [7, 0.294], [8, 0.294], [9, 0.626], [10, 0.626]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 10], [7, 8], [7, 9], [7, 10], [9, 10]]], [[0, 0.5], [1, 0.278], [2, 1.263], [3, 0.5], [4, 0.5], [5, 0.278], [6, 0.5], [7, 0.278], [8, 0.278], [9, 1.263], [10, 0.5]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 8], [7, 9], [7, 10], [8, 9], [9, 10]]], [[0, 0.5], [1, 0.427], [2, 1.085], [3, 0.278], [4, 0.543], [5, 1.0], [6, 0.427], [7, 0.427], [8, 0.219], [9, 0.614], [10, 1.106]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 9], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.5], [1, 0.5], [2, 0.5], [3, 0.614], [4, 0.614], [5, 1.091], [6, 1.091], [7, 0.626], [8, 0.626], [9, 0.294], [10, 0.294]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 8], [7, 10], [8, 9], [9, 10]]], [[0, 0.5], [1, 1.164], [2, 1.164], [3, 1.164], [4, 1.164], [5, 1.612], [6, 1.612], [7, 1.333], [8, 1.333], [9, 1.333], [10, 1.333]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [7, 10], [9, 10]]], [[0, 0.5], [1, 0.278], [2, 1.263], [3, 0.614], [4, 0.614], [5, 0.078], [6, 0.219], [7, 0.278], [8, 0.278], [9, 0.614], [10, 0.615]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 8], [6, 10], [7, 8], [7, 9], [8, 9], [9, 10]]], [[0, 0.5], [1, 0.5], [2, 0.5], [3, 0.278], [4, 1.263], [5, 0.278], [6, 0.5], [7, 1.263], [8, 0.5], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 10], [7, 8], [7, 9], [8, 9], [9, 10]]], [[0, 0.5], [1, 0.614], [2, 0.614], [3, 0.278], [4, 1.263], [5, 0.078], [6, 0.219], [7, 0.614], [8, 0.615], [9, 0.278], [10, 0.278]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 7], [6, 9], [7, 9], [7, 10], [8, 9], [8, 10]]], [[0, 0.5], [1, 0.427], [2, 0.427], [3, 0.427], [4, 0.427], [5, 2.0], [6, 2.0], [7, 0.427], [8, 0.427], [9, 0.427], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 7], [6, 9], [7, 8], [7, 10], [8, 9], [8, 10]]], [[0, 0.5], [1, 0.543], [2, 0.278], [3, 1.085], [4, 0.427], [5, 0.427], [6, 1.0], [7, 1.106], [8, 0.614], [9, 0.219], [10, 0.427]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [7, 9], [7, 10], [8, 10]]], [[0, 0.5], [1, 0.219], [2, 0.5], [3, 1.085], [4, 0.427], [5, 1.0], [6, 0.427], [7, 1.0], [8, 1.085], [9, 0.543], [10, 0.543]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 7], [5, 10], [6, 9], [6, 10], [7, 8], [7, 9], [8, 9], [8, 10]]], [[0, 0.5], [1, 0.5], [2, 0.219], [3, 0.427], [4, 1.085], [5, 0.427], [6, 1.0], [7, 1.085], [8, 1.0], [9, 0.543], [10, 0.543]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [2, 4], [1], [2], [3], [4]], [[5, 8], [5, 10], [6, 9], [6, 10], [7, 8], [7, 9], [7, 10], [8, 9]]], [[0, 0.5], [1, 0.278], [2, 0.543], [3, 0.427], [4, 1.085], [5, 1.0], [6, 0.427], [7, 0.614], [8, 1.106], [9, 0.427], [10, 0.219]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [2], [3], [4]], [[5, 8], [6, 7], [6, 9], [7, 8], [7, 9], [8, 9]]], [[0, 0.683], [1, 0.448], [2, 0.448], [3, 1.263], [4, 0.5], [5, 0.683], [6, 0.653], [7, 0.653], [8, 0.5], [9, 1.391]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [2], [3], [4]], [[5, 9], [6, 7], [6, 8], [7, 8], [7, 9], [8, 9]]], [[0, 0.683], [1, 0.448], [2, 0.448], [3, 0.615], [4, 1.164], [5, 0.404], [6, 0.561], [7, 0.626], [8, 0.746], [9, 1.056]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3], [4]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 0.5], [1, 0.653], [2, 1.391], [3, 0.683], [4, 1.263], [5, 0.653], [6, 0.448], [7, 0.5], [8, 0.448], [9, 0.683]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 0.5], [1, 1.5], [2, 1.5], [3, 1.085], [4, 1.085], [5, 0.5], [6, 2.0], [7, 2.0], [8, 1.085], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 8], [8, 9]]], [[0, 0.5], [1, 0.653], [2, 1.391], [3, 1.47], [4, 1.164], [5, 1.11], [6, 0.626], [7, 0.294], [8, 0.746], [9, 1.056]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 0.5], [1, 1.5], [2, 1.5], [3, 0.938], [4, 0.938], [5, 0.5], [6, 2.0], [7, 2.0], [8, 0.938], [9, 0.938]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3], [4]], [[5, 8], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 0.5], [1, 1.091], [2, 1.091], [3, 1.085], [4, 1.085], [5, 0.871], [6, 1.106], [7, 1.106], [8, 1.164], [9, 1.164]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2], [4]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.263], [1, 1.353], [2, 1.164], [3, 1.426], [4, 1.085], [5, 1.612], [6, 1.164], [7, 1.426], [8, 1.353], [9, 1.263]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.263], [1, 1.353], [2, 1.164], [3, 1.426], [4, 1.085], [5, 1.164], [6, 1.612], [7, 1.426], [8, 1.353], [9, 1.263]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 8], [8, 9]]], [[0, 1.263], [1, 1.426], [2, 1.085], [3, 1.353], [4, 1.164], [5, 1.612], [6, 1.164], [7, 1.426], [8, 1.263], [9, 1.353]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.263], [1, 1.426], [2, 1.085], [3, 1.353], [4, 1.164], [5, 1.164], [6, 1.612], [7, 1.426], [8, 1.263], [9, 1.353]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2], [4]], [[5, 8], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.263], [1, 0.871], [2, 1.263], [3, 0.871], [4, 1.263], [5, 2.0], [6, 2.0], [7, 1.263], [8, 0.871], [9, 0.871]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2], [4]], [[5, 7], [5, 8], [6, 8], [6, 9], [7, 9], [8, 9]]], [[0, 1.085], [1, 1.106], [2, 1.164], [3, 1.085], [4, 0.5], [5, 1.164], [6, 1.091], [7, 1.106], [8, 0.871], [9, 1.091]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 8], [7, 9], [8, 9]]], [[0, 1.085], [1, 1.106], [2, 1.164], [3, 1.106], [4, 1.164], [5, 0.891], [6, 1.612], [7, 1.612], [8, 1.353], [9, 1.353]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2], [4]], [[5, 7], [5, 9], [6, 8], [6, 9], [7, 8], [8, 9]]], [[0, 1.085], [1, 2.0], [2, 1.085], [3, 1.085], [4, 0.5], [5, 2.0], [6, 1.5], [7, 1.085], [8, 0.5], [9, 1.5]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2], [4]], [[5, 8], [5, 9], [6, 7], [6, 9], [7, 8], [8, 9]]], [[0, 1.085], [1, 2.0], [2, 1.085], [3, 2.0], [4, 1.085], [5, 2.0], [6, 2.0], [7, 2.0], [8, 1.085], [9, 1.085]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2], [4]], [[5, 8], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9]]], [[0, 1.085], [1, 1.426], [2, 1.263], [3, 1.426], [4, 1.263], [5, 1.612], [6, 1.164], [7, 1.164], [8, 1.353], [9, 1.353]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3], [2, 4], [4]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.47], [1, 1.879], [2, 2.0], [3, 2.166], [4, 1.47], [5, 1.747], [6, 1.747], [7, 2.0], [8, 1.879]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [2, 4], [3]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 1.741], [1, 2.0], [2, 2.0], [3, 2.5], [4, 1.741], [5, 1.741], [6, 2.0], [7, 2.0], [8, 1.741]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 4], [3, 4], [2]], [[5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 0.696], [1, 1.181], [2, 1.287], [3, 1.11], [4, 1.429], [5, 1.181], [6, 1.11], [7, 1.429], [8, 0.696]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]], [[0, 0.5], [1, 1.739], [2, 1.739], [3, 1.739], [4, 1.739], [5, 1.739], [6, 0.5], [7, 0.5], [8, 1.739]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3, 4]], [[5, 6], [5, 8], [6, 7], [7, 8]]], [[0, 0.5], [1, 1.816], [2, 1.746], [3, 1.746], [4, 1.816], [5, 0.746], [6, 1.747], [7, 1.747], [8, 0.746]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2], [1, 3], [2, 4], [3, 4]], [[5, 7], [5, 8], [6, 7], [6, 8]]], [[0, 0.5], [1, 1.746], [2, 1.816], [3, 1.816], [4, 1.746], [5, 0.746], [6, 1.747], [7, 1.747], [8, 0.746]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]], [[0, 2.5], [1, 1.741], [2, 1.741], [3, 1.741], [4, 1.741], [5, 2.0], [6, 2.0], [7, 2.0], [8, 2.0]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2, 4]], [[5, 6], [5, 8], [6, 7], [7, 8]]], [[0, 2.5], [1, 1.741], [2, 1.741], [3, 1.741], [4, 1.741], [5, 2.0], [6, 2.0], [7, 2.0], [8, 2.0]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 3], [2, 4], [2, 4]], [[5, 7], [5, 8], [6, 7], [6, 8]]], [[0, 2.5], [1, 1.787], [2, 1.787], [3, 1.787], [4, 1.787], [5, 2.0], [6, 2.0], [7, 2.0], [8, 2.0]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], [[5, 6], [5, 7], [6, 8], [7, 8]]], [[0, 2.5], [1, 2.5], [2, 2.5], [3, 2.5], [4, 2.5], [5, 2.5], [6, 2.5], [7, 2.5], [8, 2.5]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], [[5, 6], [5, 8], [6, 7], [7, 8]]], [[0, 2.5], [1, 2.5], [2, 2.5], [3, 2.157], [4, 2.157], [5, 2.157], [6, 2.157], [7, 2.157], [8, 2.157]]],
[[[1, 0, 0, 0, 0, 1], [[1, 3], [1, 4], [2, 3], [2, 4]], [[5, 7], [5, 8], [6, 7], [6, 8]]], [[0, 2.5], [1, 2.157], [2, 2.157], [3, 2.5], [4, 2.5], [5, 2.157], [6, 2.157], [7, 2.157], [8, 2.157]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 2, 4], [3, 4]], [[5, 7], [6, 7]]], [[0, 1.166], [1, 2.708], [2, 2.708], [3, 2.5], [4, 2.5], [5, 1.166], [6, 1.166], [7, 2.5]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3], [1, 3, 4], [2, 4]], [[5, 7], [6, 7]]], [[0, 2.139], [1, 2.302], [2, 2.719], [3, 2.302], [4, 2.719], [5, 2.302], [6, 2.302], [7, 2.139]]],
[[[1, 0, 0, 0, 0, 1], [[1, 2, 3, 4], [1, 2, 3, 4]], []], [[0, 2.5], [1, 2.708], [2, 2.708], [3, 2.708], [4, 2.708], [5, 2.5], [6, 2.5]]],
[[[1, 1, 0, 1, 0, 0], [[1, 4], [2, 4], [3], [4]], [[5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]], [[0, 0.638], [1, 0.638], [2, 0.638], [3, 0.638], [4, 0.674], [5, 0.674], [6, 0.674], [7, 0.674], [8, 3.0]]],
[[[1, 1, 0, 1, 0, 0], [[1, 4], [2, 4], [3, 4]], [[5, 6], [5, 7], [6, 7]]], [[0, 2.0], [1, 2.0], [2, 2.0], [3, 2.0], [4, 2.0], [5, 2.0], [6, 2.0], [7, 2.0]]],
[[[1, 1, 1, 1, 1, 1],[],[]],[[0, 3.5], [1, 3.5], [2, 3.5], [3, 3.5], [4, 3.5]]]]
unique_graphs = [twoballs_comp[0]]
for graph1 in twoballs_comp[1:]:
    isomorphic = False
    for graph2 in unique_graphs:
        if iso(graph1[0], graph2[0], False):
            isomorphic = True
    if not isomorphic:
        unique_graphs.append(graph1)
for newgraph in unique_graphs:
    print newgraph
print len(unique_graphs)