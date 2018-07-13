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
    adjmatrix = adjmat(g)
    for i in range(4):
        col = 4 - sum(adjmatrix[i + 1])
        if col != 0:
            for j in range(int(col)):
                g.append([i + 1])
    return g


def adjmat(g):
    length = 4 + len(g)
    m = np.zeros((length, length))
    m[0, 1:5] = 1
    m[1:5, 0] = 1
    m[1:5, 1:5] = one_ball(g[0])
    two_ball(g[1:], m)
    return m


def one_ball(g1):
    m1 = np.zeros((4, 4))
    i = (1, 1, 1, 2, 2, 3)
    j = (2, 3, 4, 3, 4, 4)
    for n in range(6):
        if g1[n] == 1:
            m1[i[n]-1, j[n]-1] = g1[n]
            m1[j[n]-1, i[n]-1] = g1[n]
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
    outdeg = [0, 0, 0, 0]
    for i in range(1,len(g2)):
        for j in range(len(g2[i])):
            outdeg[g2[i][j] - 1] += 1
    return outdeg


def curvesharp(curve, outdeg):
    k = (7 - 0.25 * sum(outdeg)) * 0.5
    if abs(curve - k) <= 1e-6 :
        return True
    else:
        return False


def iso(g1, g2):
    g1 = standardise(g1)
    g2 = standardise(g2)
    a = g1[1:]
    b = g2[1:]
    len_a = len(a)
    if len_a != len(b):
        return False
    else:
        p = list(permutations([0, 1, 2, 3]))
        m1 = one_ball(g1[0])
        m2 = one_ball(g2[0])
        for i in p:
            m1_new = m1[i, :]
            m1_new = m1_new[:, i]
            if np.array_equal(m1_new, m2):

                for j in range(len_a):
                    for k in range(len(a[j])):
                        a[j][k] = i[a[j][k]-1] + 1
                for i in range(len_a):
                    a[i].sort()
                    b[i].sort()
                a.sort()
                b.sort()
                if a == b:
                    return True
        return False



def part(n, g):
    b = outdeg(standardise(g))
    l = []
    for i in range(len(b)):
        if b[i] != 0:
            l.append(i+1)
    if n == 0:
        return 0
    else:
        if n in l:
            m = ((n))
        else:
            m = ()
        #while n-i >= 0:
        #    for i in l:
        #        m = [i]
        #        m += part(n-i, g)
        #        #m += i
        for i in range(1,n):
            for j in part(n-i, g):
                m.sort()
                m += sorted(((i,) + j))
        return m

def partition(n, g):
    b = outdeg(standardise(g))
    l = []
    for i in range(len(b)):
        if b[i] != 0:
            l.append(i + 1)
    m = []
    if n<= len(l):
        m.append([n])
    for x in range(1, n):
        for y in partition(n - x, g):
            if x <= len(l):
                s = sorted([x] + y)
                if s not in m:
                    m.append(s)
    return m



[[1, 1, 1, 2], [1, 1, 1, 1, 1], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4]]



def generate(g):
    oneballs = [[0, 0, 0, 0, 0, 0,], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]
    a_1 = [[1], [2], [3], [4]]
    a_2 = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    a_3 = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    a_4 = [[1, 2, 3, 4]]
    b = outdeg(standardise(g))
    n = sum(b)
    parts = partition(n, g)
    for a in parts:
            if max(b) <= len(a):
                for i in range(len(a)):
                    if a[i] > 4:







g = [[0, 0, 1, 1, 0, 0]]
h = standardise(g)




a = standardise([[0, 1, 1, 1, 0, 0], [2, 3], [1, 4]])

b = standardise([[1, 1, 0, 0, 0, 1], [1, 2], [3, 4]])
g = (standardise([[0, 1, 1, 1, 0, 1]]))
#print part(5, g)
#print partition(6, g)
#print outdeg(h)

#print generate([[1, 0, 1, 0, 0, 1]])

#print standardise([[1, 0, 1, 1, 0, 1], [1, 2]])
#print iso2([[0, 1, 1, 1, 0, 0], [2, 3], [1, 4]], [[1, 1, 0, 0, 0, 1], [1, 2], [3, 4]])

#print standardise([[1, 0, 0, 0, 0, 0], [2, 4], [1, 3], [4]])

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
