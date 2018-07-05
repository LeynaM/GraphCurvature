import numpy as np
import CurvatureCalculator as curve

def adjmat(a):
    length = 4 + len(a)
    m = np.zeros((length,length))
    m[0:5,0:5] = one_ball(a[0])
    two_ball(a[1:], m)
    return m

def one_ball(a1):
    m1 = np.zeros((5,5))
    i = (1,1,1,2,2,3)
    j = (2,3,4,3,4,4)
    m1[0, 1:5] = 1
    m1[1:5, 0] = 1
    for n in range(6):
        if a1[n] == 1:
            m1[i[n], j[n]] = a1[n]
            m1[j[n], i[n]] = a1[n]
    return m1

def two_ball(a2, m):
    for i in range(len(a2)):
        if type(a2[i]) is int:
            m[i+5, a2[i]] = 1
            m[a2[i], i+5] = 1
        else:
            for j in range(len(a2[i])):
                m[i+5, a2[i][j]] = 1
                m[a2[i][j], i+5] = 1

G = ((1,1,0,0,1,0), (0,1,1,0), (1,0,0,1))

A = adjmat(((1,1,0,0,1,0), (2, 3), (1, 4), (3), (4)))

#def two_ball2(a2, m):
#    for i in range(len(a2)):
#        m[i+5, i+5] = 1
#        for j in range(4):
#            if a2[i][j] == 1
#                m[i+5, j+1] = 1
#                m[j+1, i+5] = 1
             

#print A, curve.curv_calc(A, 0)

def s1outreg(G):
    g = G[1:]
    freq = np.zeros(4)
    for i in range(len(g)):
        if type(g[i]) is int:
            freq[g[i]-1] += 1
        else:
            for j in range(len(g[i])):
                freq[g[i][j]-1] += 1
    s1 = True
    for i in range(4):
        if freq[i] != freq[0]:
            s1 = False
    return s1

#print s1outreg(((1,1,0,0,1,0), (2, 1), (1, 4)))


def s1outreg2(G):
    g = G[1:]
    m = np.zeros((len(g),4))
    for i in range(len(g)):
        m[i] = g[i]
    freq = m.sum(axis = 0)
    s1 = True
    for i in range(4):
        if freq[i] != freq[0]:
            s1 = False
    return s1


#print s1outreg2(((1,1,0,0,1,0), (0,1,1,0), (1,1,0,1)))

def avoutx(G):
    g = G[1:]
    s = np.zeros(len(g))
    for i in range(len(g)):
        if type(g[i]) is int:
            s[i] = 1
        else:
            s[i] = len(g[i])
    total = sum(s)
    return 0.25*total

#print avoutx(((1,1,0,0,1,0), (2, 1), (1, 4, 3), (2)))

def outdeg(G, y):
    g = G[1:]
    n = 0
    for i in range(len(g)):
        if type(g[i]) is int:
            if g[i] == y:
                n +=1
        else:
            for j in range(len(g[i])):
                if g[i][j] == y:
                    n +=1
    return n

def avoutx2(G):
    s = np.zeros(4)
    for i in range(1,5):
        s[i-1] = outdeg(G, i)
    return 0.25*sum(s)

#print avoutx2(((1,1,0,0,1,0), (2, 1), (1, 4, 3), (2)))

#print outdeg(((1,1,0,0,1,0), (2, 1,3), (1, 4, 3), (2)), 3)

def curvesharp(G):
    if curve.curv_calc(adjmat(G), 0) == 0.5*(7-avoutx(G)):
        return 'True'
    else:
        return 'False'

print curvesharp(((1,1,0,0,1,0), (2, 1), (1, 4, 3), (2)))

