import numpy as np

def adjmat(a):
    length = 4 + len(a)
    m = np.zeros((length,length))
    m[0:5,0:5] = one_ball(a[0])
    two_ball(a[1:], m)
    return m




def one_ball(a1):
    m1 = np.ones((5,5))
    i = (1,1,1,2,2,3)
    j = (2,3,4,3,4,4)
    for n in range(6):
        if a1[n] == 0:
            m1[i[n]][j[n]] = a1[n]
            m1[j[n]][i[n]] = a1[n]
    return m1



def two_ball(a2, m):
    for i in range(len(a2)):
        for j in range(len(a2[i])):
            m[i+5][a2[i][j]] =  1
            m[a2[i][j]][i+5] =  1
            m[i+5][i+5] = 1
                

print adjmat(((1,1,1,0,0,0),(2,3),(3,4)))


