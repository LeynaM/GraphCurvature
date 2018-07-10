import numpy as np
from itertools import permutations
import time
import CurvatureCalculator as curve


def summary(g):
    gs = standardise(g)
    adjmatrix = adjmat(gs)
    curvature = curve.curv_calc(adjmatrix, 0)
    outdegree = outdeg(gs[1:])
    s1out = s1outreg(outdegree)
    curve_sharp = curvesharp(curvature, outdegree)
    print "\nCurvature: %11.3f\nS1 out-reg: %10s\nCurvature-sharp: %s" % (curvature, s1out, curve_sharp)
    return


def norm2(g):
    gnorm = [[0 for i in range(4)] for i in range(1, len(g) + 1)]
    gnorm[0] = [g[0][i] for i in range(len(g[0]))]
    g2 = g[1:]
    for j in range(4):
        for i in range(len(g2)):
            if j + 1 in g2[i]:
                gnorm[i + 1][j] = 1
    return gnorm


def norm(g):
    gnorm = [g[0]]
    for i in range(1, len(g)):
        leaf = [0, 0, 0, 0]
        for j in range(len(g[i])):
            leaf[g[i][j] - 1] = 1
        gnorm.append(leaf)
    return gnorm


def standardise(g):
    l = [[0 for i in range(1)] for i in range(4)]
    adjmatrix = adjmat(g)
    g = [[g[i][j] for j in range(len(g[i]))] for i in range(len(g))]
    for i in range(len(l)):
        l[i] = [sum(adjmatrix[i + 1])]
        l[i][0] = 4 - (l[i][0])
    for i in range(4):
        if l[i] != [0]:
            for j in range(int(l[i][0])):
                g.append([i + 1])
    return g


def adjmat(g):
    length = 4 + len(g)
    m = np.zeros((length, length))
    m[0:5, 0:5] = one_ball(g[0])
    two_ball(g[1:], m)
    return m


def one_ball(g1):
    m1 = np.zeros((5, 5))
    i = (1, 1, 1, 2, 2, 3)
    j = (2, 3, 4, 3, 4, 4)
    m1[0, 1:5] = 1
    m1[1:5, 0] = 1
    for n in range(6):
        if g1[n] == 1:
            m1[i[n], j[n]] = g1[n]
            m1[j[n], i[n]] = g1[n]
    return m1


def two_ball(g2, m):
    for i in range(len(g2)):
        if type(g2[i]) is int:
            m[i + 5, g2[i]] = 1
            m[g2[i], i + 5] = 1
        else:
            for j in range(len(g2[i])):
                m[i + 5, g2[i][j]] = 1
                m[g2[i][j], i + 5] = 1


def s1outreg(outdeg):
    s1 = True
    for i in range(4):
        if outdeg[i] != outdeg[0]:
            s1 = False
    return s1


def outdeg(g2):
    outdeg = np.zeros(4)
    for i in range(len(g2)):
        if type(g2[i]) is int:
            outdeg[g2[i] - 1] += 1
        else:
            for j in range(len(g2[i])):
                outdeg[g2[i][j] - 1] += 1
    return outdeg


def curvesharp(curve, outdeg):
    k = (7 - 0.25 * sum(outdeg)) * 0.5
    if curve == k:
        return True
    else:
        return False


def iso(g1, g2):
    if len(g1) != len(g2):
        return False
    else:
        for i in g1[1:]:
            if i not in g2[1:]:
                return False
        p = list(permutations([0, 1, 2, 3]))
        m1 = one_ball(g1[0])
        m2 = one_ball(g2[0])
        m1_one = m1[1:, 1:]
        m2_one = m2[1:, 1:]
        for i in p:
            m1_one_new = m1_one[i, :]
            m1_one_new = m1_one_new[:, i]
            if np.array_equal(m1_one_new, m2_one):
                return True
        return False



print iso(((1, 0, 1, 1, 0, 1), (1, 2), (4), (3)), ((1, 1, 0, 0, 1, 1), (1, 2), (4), (3)))

# print standardise([[1, 0, 0, 0, 0, 0], [2, 4], [1, 3]])

# summary(((1,1,1,1,0,0),(2,3,4),(4)))

# def two_ball2(a2, m):
#    for i in range(len(a2)):
#        m[i+5, i+5] = 1
#        for j in range(4):
#            if a2[i][j] == 1
#                m[i+5, j+1] = 1
#                m[j+1, i+5] = 1
#
# def s1outreg2(G):
#     g = G[1:]
#     m = np.zeros((len(g),4))
#     for i in range(len(g)):
#         m[i] = g[i]
#     freq = m.sum(axis = 0)
#     s1 = True
#     for i in range(4):
#         if freq[i] != freq[0]:
#             s1 = False
#     return s1
