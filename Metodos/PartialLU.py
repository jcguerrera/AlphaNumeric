import copy
import numpy as np

def partialLU(A, b):
    n = len(A)
    message = ''
    det = np.linalg.det(A)
    if(det != 0):
        u = zero_Matrix(n)
        l = lmatrix(n)
        p = lmatrix(n)
        dicL = {}
        dicU = {}
        dicP = {}
        for k in range(n):
            print('step ', k)
            printMatriz(A)
            print('L step', k)

            la = np.around(l,decimals=5)
            printMatriz(la)
            dicL[k] = copy.deepcopy(la)
            ua = np.around(u, decimals=5)
            dicU[k] = copy.deepcopy(ua)
            A, p = searchBiggerandSwap(A, n, k, p)
            for i in range(k + 1, n):
                mult = A[i][k] / A[k][k]
                l[i][k] = mult
                for j in range(k, n):
                    A[i][j] = A[i][j] - mult * A[k][j]

            print('u step', k)
            for i in range(n):
                u[k][i] = A[k][i]
            ua = np.around(u,decimals=5)
            printMatriz(ua)
            dicU[k] = copy.deepcopy(ua)
            print('P step', k)
            pa = np.around(p,decimals=5)
            printMatriz(pa)
            dicP[k] = copy.deepcopy(pa)

        Pb = multAb(p, b)
        lpb = concatenateMatrix(l, Pb)
        z = progSubtitution(lpb)
        uz = concatenateMatrix(u, z)
        x = backSubstitution(uz)
        x = np.around(x,decimals=5)
        print('det', x)
        return (x,dicL,dicU,dicP,None)
    else:
        message = 'Error'
        return (None,None,None,None,message)

def searchBiggerandSwap(Ab, n, i, p):
    row = i

    for j in range(i + 1, n):
        if (abs(Ab[row][i]) < abs(Ab[j][i])):
            row = j
    temp = Ab[i]
    aux = p[i]
    Ab[i] = Ab[row]
    p[i] = p[row]
    Ab[row] = temp
    p[row] = aux
    return Ab, p


def concatenateMatrix(A, b):
    n = len(A)
    for i in range(n):
        A[i].append(b[i], )
    return A


def multAb(A, b):
    n = len(A)
    mult = []
    for i in range(n):
        suma = 0
        for j in range(n):
            suma += b[j] * A[i][j]
        mult.append(suma)
    return mult


def zero_Matrix(n):
    u = []
    for i in range(n):
        u.append([0] * n)
    return u


def lmatrix(n):
    l = zero_Matrix(n)
    for i in range(n):
        l[i][i] = 1
    return l


def backSubstitution(Ab):
    n = len(Ab)
    x = []
    for i in range(n):
        x.append(0)

    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += Ab[i][j] * x[j]
        x[i] = (Ab[i][n] - sum) / Ab[i][i]
    return x


def progSubtitution(Ab):
    n = len(Ab)
    x = []
    for i in range(n):
        x.append(0)

    for i in range(n):
        sum = 0
        for j in range(i):
            sum += Ab[i][j] * x[j]
        x[i] = ((Ab[i][n] - sum) / Ab[i][i])
    return x


def printMatriz(M):
    for i in range(len(M)):
        print(M[i])


'--------------------------------------------------------------'
'''A = [[4.0, -1.0, 0.0, 3.0],
     [1.0, 15.5, 3.0, 8.0],
     [0.0, -1.3, -4.0, 1.1],
     [14.0, 5.0, -2.0, 30.0],
     ]

b2 = [1, 1, 1, 1]

partialLU(A, b2)'''