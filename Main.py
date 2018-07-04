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

G = ((1,1,0,0,1,0), (2, 3), (2, 4))
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
    l = []
    for k in range(1, 5):
        n = 0
        for i in range(1,len(G[1:])):
            for j in range(len(G[i])):
                if G[i][j] == k:
                    n =+ 1
                else:break

        l.append(n)
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] != l[j]:
                return 'No'
            else:
                return 'yes'
#print s1outreg(G)

def outreg(G):
    l = G[1:]
    s=[[]]
    for k in range(1, 5):
        n = 0
        r= []
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] == k:
                    n +=1
                    s.append(n)
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] != s[j]:
                return 'No'
            else:
                return 'Yes'
print outreg(G)








