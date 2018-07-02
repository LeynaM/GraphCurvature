from numpy.linalg import eigvalsh
import numpy as np
import json
#from sympy.matrices import *


def weight_to_adj(W):
    n = len(W)
    A = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            if W[i][j] != 0:
                A[i][j] = 1
    return A


def W_two_ball(A, W, i):
    S1 = one_sphere(A, i)
    S2 = two_sphere(A, i)
    O = []
    O.append(i)
    O.extend(S1)
    O.extend(S2)
    n = len(O)
    RES = [[0 for x in range(n)] for x in range(n)]
    for j in range(n):
        for k in range(n):
            RES[j][k] = W[O[j]][O[k]]
    return RES


def lap(A):
    n = len(A)
    RES = [[0 for x in range(n)] for x in range(n)]
    D = [0] * n
    for i in range(n):
        D[i] = -sum(A[i])
    for i in range(n):
        for j in range(n):
            RES[i][j] = A[i][j]
    for i in range(n):
        RES[i][i] = D[i]
    return RES


def evs(A):
    V = eigvalsh(A)
    for i in range(len(V)):
        V[i] = format(V[i], 'f')
    return V


def swap(A, i, j):
    B = np.array(A)
    B[[i, j]] = B[[j, i]]
    B[:, [i, j]] = B[:, [j, i]]
    C = B.tolist()
    return C


def intersect(a, b):
    return list(set(a) & set(b))


def neighbours_2(A, i):
    M = np.array(A)
    M2 = np.dot(M, M) + M
    n = len(A)
    RES = []
    V = M2[i]
    for j in range(n):
        if V[j] != 0:
            RES.append(j)
    return RES


def mu_two_ball(A, MU, i):
    S1 = one_sphere(A, i)
    S2 = two_sphere(A, i)
    O = []
    O.append(i)
    O.extend(S1)
    O.extend(S2)
    n = len(O)
    RES = [0 for x in range(n)]
    for j in range(n):
        RES[j] = MU[O[j]]
    return RES


def two_ball(A, i):
    S1 = one_sphere(A, i)
    S2 = two_sphere(A, i)
    O = []
    O.append(i)
    O.extend(S1)
    O.extend(S2)
    n = len(O)
    RES = [[0 for x in range(n)] for x in range(n)]
    for j in range(n):
        for k in range(n):
            RES[j][k] = A[O[j]][O[k]]
    return RES


def mat_order(A, i):
    S1 = one_sphere(A, i)
    S2 = two_sphere(A, i)
    return [i, S1, S2]


def one_sphere(A, i):
    n = len(A)
    RES = []
    for j in range(n):
        if A[i][j] == 1:
            RES.append(j)
    return RES


def two_sphere(A, i):
    M = np.array(A)
    M2 = np.dot(M, M)
    n = len(A)
    RES = []
    V = M2[i]
    for j in range(n):
        if V[j] != 0:
            if A[i][j] != 1:
                if i != j:
                    RES.append(j)
    return RES


def fourGamma(A, i):
    B = two_ball(A, i)
    n = len(B)
    RES = [[0 for x in range(n)] for x in range(n)]
    RES[0][0] = 2 * sum(B[0])
    for j in range(1, n):
        if B[0][j] == 1:
            RES[j][j] = 2
            RES[0][j] = -2
            RES[j][0] = -2
    return RES


def fourGamma2(A, i):
    B = two_ball(A, i)
    n = len(B)
    RES = [[0 for x in range(n)] for x in range(n)]
    d = sum(B[0])
    S1 = one_sphere(B, 0)
    S2 = two_sphere(B, 0)
    E = [len(intersect(one_sphere(B, j), S1)) for j in range(n)]
    F = [len(intersect(one_sphere(B, j), S2)) for j in range(n)]
    RES[0][0] = d * (d + 3)
    for j in S1:
        RES[j][j] = 5 - d + 3 * F[j] + 4 * E[j]
        RES[0][j] = -3 - d - F[j]
        RES[j][0] = -3 - d - F[j]
    for j in S2:
        RES[j][j] = E[j]
        RES[0][j] = E[j]
        RES[j][0] = E[j]
    for j in S1:
        for k in S1:
            if j != k:
                RES[j][k] = 2 - 4 * B[j][k]
    for j in S1:
        for k in S2:
            RES[j][k] = -2 * B[j][k]
            RES[k][j] = -2 * B[j][k]
    return RES


def fourGamma2Mu(A, MU, i):
    B = two_ball(A, i)
    M = mu_two_ball(A, MU, i)
    n = len(B)
    RES = [[0 for x in range(n)] for x in range(n)]
    d = sum(B[0])
    mx = 1.0 * M[0]
    S1 = one_sphere(B, 0)
    S2 = two_sphere(B, 0)
    RES[0][0] = (1.0 * d * d) / (mx ** 2) + (3.0 / (mx)) * sum([1.0 / (1.0 * M[y]) for y in S1])
    for j in S1:
        RES[j][j] = 3.0 / (mx * M[j]) + 2.0 / (mx ** 2) - (1.0 * d) / (mx ** 2) + (3.0 / (mx * M[j])) * sum(
            [B[j][z] for z in S2]) + (1.0 / mx) * sum([(1.0 / (1.0 * M[z]) + 3.0 / (1.0 * M[j])) * B[j][z] for z in S1])
        RES[0][j] = -3.0 / (mx * M[j]) - (1.0 * d) / (mx ** 2) - (1.0 / (mx * M[j])) * sum([B[j][z] for z in S2]) - (
                    1.0 / mx) * sum([(-1.0 / (1.0 * M[z]) + 1.0 / (1.0 * M[j])) * B[j][z] for z in S1])
        RES[j][0] = -3.0 / (mx * M[j]) - (1.0 * d) / (mx ** 2) - (1.0 / (mx * M[j])) * sum([B[j][z] for z in S2]) - (
                    1.0 / mx) * sum([(-1.0 / (1.0 * M[z]) + 1.0 / (1.0 * M[j])) * B[j][z] for z in S1])
    for j in S2:
        RES[j][j] = (1.0 / mx) * sum((1.0 / M[y]) * B[y][j] for y in S1)
        RES[0][j] = (1.0 / mx) * sum((1.0 / M[y]) * B[y][j] for y in S1)
        RES[j][0] = (1.0 / mx) * sum((1.0 / M[y]) * B[y][j] for y in S1)
    for j in S1:
        for k in S1:
            if j != k:
                RES[j][k] = 2.0 / (mx ** 2) - (1.0 / mx) * (2.0 / (1.0 * M[j]) + 2.0 / (1.0 * M[k])) * B[j][k]
    for j in S1:
        for k in S2:
            RES[j][k] = (-2.0 * B[j][k]) / (mx * M[j])
            RES[k][j] = (-2.0 * B[j][k]) / (mx * M[j])
    return RES


def fourGamma2Norm(A, i):
    MU = [sum([A[j][k] for k in range(len(A))]) for j in range(len(A))]
    return fourGamma2Mu(A, MU, i)


def fourGammaNorm(A, i):
    d = sum(A[i])
    M = (1.0 / (1.0 * d)) * np.array(fourGamma(A, i))
    return M.tolist()


def curv_sign(A, i):
    M = fourGamma2(A, i)
    ev = evs(M)
    if ev[0] < 0:
        return -1
    if ev[1] == 0:
        return 0
    else:
        return 1


def curv_sign_norm(A, i):
    M = fourGamma2Norm(A, i)
    ev = evs(M)
    if ev[0] < 0:
        return -1
    if ev[1] == 0:
        return 0
    else:
        return 1


def curv_calc(A, i):
    M = fourGamma2(A, i)
    N = fourGamma(A, i)
    ev = evs(M)
    if ev[1] == 0 and ev[0] == 0:
        return 0
    if ev[0] < 0:
        K = 0
        t = 0
        while t == 0:
            K -= 0.001
            if evs(np.array(M) - K * np.array(N))[0] == 0:
                t += 1
        return K
    if ev[1] > 0:
        K = 0
        t = 0
        while t == 0:
            K += 0.001
            if evs(np.array(M) - K * np.array(N))[0] < 0:
                t += 1
        return K - 0.001


def curv_calc_norm(A, i):
    M = fourGamma2Norm(A, i)
    N = fourGammaNorm(A, i)
    ev = evs(M)
    if ev[1] == 0 and ev[0] == 0:
        return 0
    if ev[0] < 0:
        K = 0
        t = 0
        while t == 0:
            K -= 0.001
            if evs(np.array(M) - K * np.array(N))[0] == 0:
                t += 1
        return K
    if ev[1] > 0:
        K = 0
        t = 0
        while t == 0:
            K += 0.001
            if evs(np.array(M) - K * np.array(N))[0] < 0:
                t += 1
        return K - 0.001


def fourGammaFULL(W, MU, i):
    A = weight_to_adj(W)
    B = two_ball(A, i)
    M = mu_two_ball(A, MU, i)
    Y = W_two_ball(A, W, i)
    n = len(B)
    RES = [[0 for x in range(n)] for x in range(n)]
    d = sum(Y[0])
    mx = 1.0 * M[0]
    RES = [[0 for x in range(n)] for x in range(n)]
    RES[0][0] = (2.0 * d) / mx
    for j in range(1, n):
        if B[0][j] == 1:
            RES[j][j] = (2 * Y[0][j]) / mx
            RES[0][j] = (-2 * Y[0][j]) / mx
            RES[j][0] = (-2 * Y[0][j]) / mx
    return RES


def fourGammatwoFull(W, MU, i):
    A = weight_to_adj(W)
    B = two_ball(A, i)
    M = mu_two_ball(A, MU, i)
    Y = W_two_ball(A, W, i)
    n = len(B)
    RES = [[0 for x in range(n)] for x in range(n)]
    d = sum(Y[0])
    mx = 1.0 * M[0]
    S1 = one_sphere(B, 0)
    S2 = two_sphere(B, 0)
    RES[0][0] = (1.0 * d * d) / (mx ** 2) + (3.0 / (mx)) * sum([(1.0 * Y[0][y] * Y[0][y]) / (1.0 * M[y]) for y in S1])
    for j in S1:
        RES[j][j] = (3.0 * Y[0][j] * Y[0][j]) / (mx * M[j]) + (2.0 * Y[0][j] * Y[0][j]) / (mx ** 2) - (
                    1.0 * d * Y[0][j]) / (mx ** 2) + ((3.0 * Y[0][j]) / (mx * M[j])) * sum([Y[j][z] for z in S2]) + (
                                1.0 / mx) * sum(
            [((Y[0][z] * Y[z][j] * 1.0) / (1.0 * M[z]) + (3.0 * Y[0][j] * Y[j][z]) / (1.0 * M[j])) * B[j][z] for z in
             S1])
        RES[0][j] = (-3.0 * Y[0][j] * Y[0][j]) / (mx * M[j]) - ((1.0 * Y[0][j]) / (mx * M[j])) * sum(
            [Y[j][z] for z in S2]) - (d * Y[0][j]) / (mx ** 2) - (1.0 / mx) * sum(
            [((Y[0][j] * Y[z][j] * 1.0) / (1.0 * M[j]) - (1.0 * Y[0][z] * Y[j][z]) / (1.0 * M[z])) * B[j][z] for z in
             S1])
        RES[j][0] = (-3.0 * Y[0][j] * Y[0][j]) / (mx * M[j]) - ((1.0 * Y[0][j]) / (mx * M[j])) * sum(
            [Y[j][z] for z in S2]) - (d * Y[0][j]) / (mx ** 2) - (1.0 / mx) * sum(
            [((Y[0][j] * Y[z][j] * 1.0) / (1.0 * M[j]) - (1.0 * Y[0][z] * Y[j][z]) / (1.0 * M[z])) * B[j][z] for z in
             S1])
    for j in S2:
        RES[j][j] = (1.0 / mx) * sum(((1.0 * Y[0][y] * Y[y][j]) / (1.0 * M[y])) * B[y][j] for y in S1)
        RES[0][j] = (1.0 / mx) * sum(((1.0 * Y[0][y] * Y[y][j]) / (1.0 * M[y])) * B[y][j] for y in S1)
        RES[j][0] = (1.0 / mx) * sum(((1.0 * Y[0][y] * Y[y][j]) / (1.0 * M[y])) * B[y][j] for y in S1)
    for j in S1:
        for k in S1:
            if j != k:
                RES[j][k] = (2.0 * Y[0][k] * Y[0][j]) / (mx ** 2) - (1.0 / mx) * (
                            (2.0 * Y[0][j] * Y[j][k]) / (1.0 * M[j]) + (2.0 * Y[0][k] * Y[j][k]) / (1.0 * M[k])) * B[j][
                                k]
    for j in S1:
        for k in S2:
            RES[j][k] = (-2.0 * B[j][k] * Y[0][j] * Y[j][k]) / (mx * M[j])
            RES[k][j] = (-2.0 * B[j][k] * Y[0][j] * Y[j][k]) / (mx * M[j])
    return RES
