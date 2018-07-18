import numpy as np
from itertools import permutations
import time
import CurvatureCalculator as curvature
import copy

oneballs = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]
all_2ball_vertices = [[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
                      [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]],
                      [[1, 2, 3, 4]]]

def summary(g):
    gs = standardise(g)
    adjmatrix = adjmat(gs)
    curv = curvature.curv_calc(adjmatrix, 0)
    outdegree = outdeg(gs[1:])
    s1out = s1outreg(outdegree)
    curve_sharp = curv_sharp(curv, outdegree)
    print "\nCurvature: %11.3f\nS1 out-reg: %10s\nCurvature-sharp: %s" % (curv, s1out, curve_sharp)
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
    gnew = g[:]
    adjmatrix = adjmat(gnew)
    for i in range(4):
        col = 4 - sum(adjmatrix[i + 1])
        if col != 0:
            for j in range(int(col)):
                gnew.append([i + 1])
    return gnew


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


def curv_sharp(curve, outdeg):
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


def partition(n):
    m = [[n]]
    for x in range(1, n):
        for y in partition(n - x):
            s = sorted([x] + y, reverse=True)
            if s not in m:
                m.append(s)
    return m

h = []
def fill_twoballs(b, part, two_sphere):
    if len(part) == 0:
        two_sphere.sort()
        if two_sphere not in h:
            h.append(two_sphere)
        return
    if part[0] == 1:
        new_two_sphere = two_sphere[:]
        for i in range(4):
            for j in range(b[i]):
                new_two_sphere = new_two_sphere + [[i+1]]
        new_two_sphere.sort()
        new_two_sphere.sort(key=len, reverse=True)
        if new_two_sphere not in h:
            h.append(new_two_sphere)
        return
    p = part[0]
    part_new = part[1:]
    for a in all_2ball_vertices[p - 2]:
        valid = True
        b_new = b[:]
        for i in a:
            if b[i-1] == 0:
                valid = False
            b_new[i-1] -= 1
        if valid:
            new_two_sphere = two_sphere + [a]
            fill_twoballs(b_new, part_new, new_two_sphere)
    return

def generate():
    all_two_balls = []
    positivecurvature = []
    curvaturesharp = []
    for oneball in oneballs[:-1]:
        b = outdeg(standardise([oneball]))
        n = sum(b)
        l = 0
        for i in range(len(b)):
            if b[i] != 0:
                l += 1
        parts = partition(n)
        partsnew = []
        for a in parts:
            if max(a) <= l and max(b) <= len(a):
                partsnew.append(a)
        two_spheres = []
        for part in partsnew:
            twoball = []
            #h = []
            fill_twoballs(b, part, twoball)
            two_spheres.append(h)
        oneball_graphs = []
        for i in two_spheres:
            for j in i:
                graph = [oneball]
                for k in j:
                    graph.append(k)
                isomorphic = False
                for l in oneball_graphs:
                    isomorphic = iso(l,graph)
                if not isomorphic:
                      oneball_graphs.append(graph)
                curv = curvature.curv_calc(adjmat(graph), 0)
                if curv >= 0:
                    positivecurvature.append(graph)
                if curv_sharp(curv, b):
                    curvaturesharp.append(graph)
        all_two_balls.append(oneball_graphs)
    all_two_balls.append([[oneballs[-1]]])
    for list in all_two_balls:
        for graph in list:
            print graph

h = []
two_sphere = [[0, 0, 1, 1, 0, 0]]
b = outdeg(standardise(two_sphere))
part = [3, 2, 1, 1, 1]
fill_twoballs(b, part, two_sphere)
print h


#generate()
    # length = 0
    # print "All of the graphs:"
    # for oneballsubset in all_two_balls:
    #     length += len(oneballsubset)
    #     for graph in oneballsubset:
    #         print graph
    # print "Number of graphs generated: ", length
    # print "Graphs with positive curvature:"
    # print positivecurvature
    # print "Number of graphs with positive curvature: ", len(positivecurvature)
    # print "Graphs that are curvature sharp:"
    # print curvaturesharp
    # print "Number of graphs that are curvature sharp: ", len(curvaturesharp)


#generate()