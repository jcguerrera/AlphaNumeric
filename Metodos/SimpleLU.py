import numpy as np
import math as math
import copy

def simpleLU(A, b):

    n = len(A)
    det = np.linalg.det(A)
    message = ''
    if(det != 0):
        u = zero_Matrix(n)
        l = lmatrix(n)
        dicL = {}
        dicU = {}

        for k in range(n):
            print('step ', k)
            printMatriz(A)
            print('L step', k)
            printMatriz(l)
            dicL[k] = copy.deepcopy(l)
            dicU[k] = copy.deepcopy(u)
            if (A[k][k] == 0):
                A = searchAndSwapZero(A, n, k)
            for i in range(k + 1, n):
                mult = A[i][k] / A[k][k]

                l[i][k] = mult
                for j in range(k, n):
                    A[i][j] = A[i][j] - mult * A[k][j]

            print('u step', k)
            for i in range(n):
                u[k][i] = A[k][i]
            printMatriz(u)
            dicU[k] = copy.deepcopy(u)

        print('u', dicU)
        lb = concatenateMatrix(l, b)
        z = progSubtitution(lb)
        uz = concatenateMatrix(u, z)
        x = backSubstitution(uz)
        print('x ', x)

        return (x,dicL,dicU,message)
    else:
        message = 'Error'
        return ('', '', '', message)




def searchAndSwapZero(Ab, n, i):
    for j in range(i + 1, n):
        if (Ab[j][i] != 0):
            temp = Ab[i]
            Ab[i] = Ab[j]
            Ab[j] = temp
            break
    return Ab

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

simpleLU(A, b2)'''
