import numpy as np
import itertools
from itertools import permutations
from itertools import combinations
import time

import CurvatureCalculator as curvature
import copy
from operator import itemgetter
import ast
import math
from itertools import repeat
from itertools import chain
from itertools import izip

def adjmat(g):
    length = len(g[1]) + 1
    m = np.zeros((4 + length, 4 + length), dtype=int)
    m[0, 1:5] = 1
    m[1:5, 0] = 1
    m[1:5, 1:5] = one_ball(g[0])
    for i in range(1, length - 1):
        if type(g[1][i]) is int:
            m[i + 4, g[1][i]] = 1
            m[g[1][i], i + 4] = 1
        else:
            for j in range(len(g[1][i])):
                m[i + 4, g[1][i][j]] = 1
                m[g[1][i][j], i + 4] = 1
    return m


def one_ball(g1):
    m1 = np.zeros((4, 4), dtype=int)
    i = (1, 1, 1, 2, 2, 3)
    j = (2, 3, 4, 3, 4, 4)
    for n in range(6):
        if g1[n] == 1:
            m1[i[n] - 1, j[n] - 1] = 1
            m1[j[n] - 1, i[n] - 1] = 1
    return m1


def standardise(g):
    gnew = copy.deepcopy(g)
    adjmatrix = adjmat(gnew)
    col_sum = np.sum(adjmatrix[1:, 1:5], axis=0)
    for i in range(4):
        col = 3 - int(col_sum[i])
        if col != 0:
            for j in range(col):
                gnew[1].append([i + 1])
    gnew[1].sort(key=itemgetter(0))
    gnew[1].sort(key=len, reverse=True)
    return gnew

def iso(g1, g2):
    print g1
    print g2
    # Return false if number of two sphere vertices are different
    num_radial = len(g1[1])
    if num_radial != len(g2[1]):
        return False
    # Create dictionary for each network graph
    network1 = {}
    network2 = {}
    for i in range(5 + num_radial):
        network1[i] = []
        network2[i] = []
    # Connect one sphere to 'given' centre
    for i in range(1, 5):
        network1[0].append(i)
        network1[i].append(0)
        network2[0].append(i)
        network2[i].append(0)
    # Establish one ball connections
    j = (1, 1, 1, 2, 2, 3)
    k = (2, 3, 4, 3, 4, 4)
    for i in range(6):
        if g1[0][i] == 1:
            network1[j[i]].append(k[i])
            network1[k[i]].append(j[i])
        if g2[0][i] == 1:
            network2[j[i]].append(k[i])
            network2[k[i]].append(j[i])
    # Establish radial connections
    radial1 = g1[1]
    radial2 = g2[1]
    for i in range(num_radial):
        for j in range(len(radial1[i])):
            network1[i + 5].append(radial1[i][j])
            network1[radial1[i][j]].append(i + 5)
        for j in range(len(radial2[i])):
            network2[i + 5].append(radial2[i][j])
            network2[radial2[i][j]].append(i + 5)
    # Establish spherical connections
    # if len(g) == 3:
    #     for i in g[2]:

    # Return false if number of vertices with same degree is different
    degrees1 = [[], [], [], []]
    degrees2 = [[], [], [], []]
    for i in range(len(network1)):
        degrees1[len(network1[i])-1].append(network1.keys()[i])
        degrees2[len(network2[i])-1].append(network2.keys()[i])
    if degrees1 != degrees2:
        return False

    # Permute vertices to match networks
    # Permutations of vertices with one degree:
    vertex_perms = []
    num_perms = []
    vertices1 = []
    # degrees1 = [[5, 6], [7, 8, 9], [10, 11, 12, 13], [0, 1, 2, 3, 4, 14]]
    # degrees2 = [[5, 6], [7, 8, 9], [10, 11, 12, 13], [0, 1, 2, 3, 4, 14]]
    for i in range(4):
        num_deg = len(degrees2[i])
        if num_deg == 1:
            perms = [tuple(degrees2[i])]
            vertex_perms.append(perms)
        if num_deg > 1:
            perms = list(list(permutations(degrees2[i])))
            vertex_perms.append(perms)
        # Create list of tuples for network one vertices grouped by degree
        if degrees1[i]:
            vertices1.append(tuple(degrees1[i]))
            # Remove empty sets from degrees
            num_perms.append(len(degrees1[i]))
    # Duplicate and merge permutation for each degree to get all permutations
    num_perms = map(lambda x: math.factorial(x), num_perms)
    total_perms = reduce(lambda x, y: x * y, num_perms, 1)
    perms = list(chain.from_iterable(list(repeat(vertex_perms[0], total_perms/num_perms[0]))))
    all_perms = [list(chain.from_iterable(list(repeat(vertex_perms[0], total_perms/num_perms[0]))))]
    indi_repeats = num_perms[0]
    for i in range(1, len(num_perms)):
        perms = []
        for j in range(len(vertex_perms[i])):
            perms.extend(list(repeat(vertex_perms[i][j], indi_repeats)))
        all_perms.append(list(chain.from_iterable(list(repeat(perms, total_perms/len(perms))))))
        indi_repeats = indi_repeats*num_perms[i]

    # Compare permutations of the second network with the first network
    for n in range(1, total_perms):
        network_cmp = copy.deepcopy(network2)
        cmp_keys = network2.keys()
        for i in range(len(vertices1)):
            for j in range(len(vertices1[i])):
                vertex1 = vertices1[i][j]
                vertex2 = all_perms[i][n][j]
                if vertex1 != vertex2:
                    # Switch keys
                    # delete? cmp_keys = map(lambda x: vertex1 if x == vertex2 else x, cmp_keys)
                    cmp_keys[vertex1] = vertex2
                    for k in range(len(network1)):
                        network_cmp[k] = map(lambda x: -vertex2 if x == vertex1 else x, network_cmp[k])
        # Combine switched keys and values
        network_cmp_cmplt = copy.deepcopy(network_cmp)
        for k in range(len(cmp_keys)):
            network_cmp_cmplt[cmp_keys[k]] = sorted(map(abs, network_cmp[k]))
        if network1 == network_cmp_cmplt:
            return True
    return False











# iso pair 0
print "NetworkA"
networkA = [[1, 1, 0, 0, 1, 1], [[1, 2, 3], [4]]]
print "NetworkB"
networkB = [[1, 1, 0, 0, 1, 1], [[1, 3, 4], [2]]]

isomorphic = iso(networkA,networkB)
print "iso, netA == nB: %s (T)\n\n" %(isomorphic)

# iso pair 1
print "NetworkA"
networkA = [[1, 0, 1, 1, 0, 1], [[1, 2], [3, 4]]]
print "NetworkB"
networkB = [[0, 1, 1, 1, 1, 0], [[1, 3], [2, 4]]]

isomorphic = iso(networkA , networkB)
print "iso, netA == nB: %s (T)\n\n" %(isomorphic)
# #
# # non iso pair 1
print "Network1"
network1 = [[1, 1, 0, 0, 1, 1], [[1, 4], [2, 3]]]
print "Network2"
network2 = [[1, 1, 0, 0, 1, 1], [[1, 2], [3, 4]]]
#
isomorphic = iso(network1 , network2)
print "net1 == n2: %s (F)\n\n" %(isomorphic)
# #
# # iso pair 2
print "NetworkA"
networkA = [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 2, 3], [2, 3, 4], [1, 4]]]
print "NetworkB"
networkB = [[0, 0, 0, 0, 0, 0], [[1, 2, 3, 4], [1, 3, 4], [1, 2, 4], [2, 3]]]

isomorphic = iso(networkA , networkB)
print "iso, netA == nB: %s (T)\n\n" %(isomorphic)
# #
# #
