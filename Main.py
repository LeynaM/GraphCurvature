import numpy as np
import CurvatureCalculator as curve

def summary(g):
    adjmatrix = adjmat(g)
    curvature = curve.curv_calc(adjmatrix, 0)
    outdegree = outdeg(g[1:])
    s1out = s1outreg(outdegree)
    curve_sharp = curvesharp(curvature, outdegree)
    print "\nCurvature: %.3f\nS1 out-reg: %s\nCurvature-sharp: %s" % (curvature, s1out, curve_sharp)
    return

def adjmat(g):
    length = 4 + len(g)
    m = np.zeros((length,length))
    m[0:5,0:5] = one_ball(g[0])
    two_ball(g[1:], m)
    return m

def one_ball(g1):
    m1 = np.zeros((5,5))
    i = (1,1,1,2,2,3)
    j = (2,3,4,3,4,4)
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
            m[i+5, g2[i]] = 1
            m[g2[i], i+5] = 1
        else:
            for j in range(len(g2[i])):
                m[i+5, g2[i][j]] = 1
                m[g2[i][j], i+5] = 1

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
    k = (7 - 0.25*sum(outdeg))*0.5
    if curve == k:
        return 'True'
    else:
        return 'False'

summary(((1,1,1,1,0,0),(2,3,4),(4)))

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
