import numpy as np
import math
import copy

def choleskyy(A, b):

    A = np.array(A)
    b = np.array(b)
    #Inicialización
    n = len(A)
    L = np.eye(n)
    U = np.eye(n)

    message = ''
    dicL = {}
    dicU = {}
    det = np.linalg.det(A)
    if det != 0:
        #factorization
        for i in range(n-1):
            la = np.around(L, decimals=4)
            dicL[i] = copy.deepcopy(la)
            ua = np.around(U, decimals=4)
            dicU[i] = copy.deepcopy(ua)
            suma = 0
            for j in range(i):
                suma += (L[i][j] * U[j][i])
            L[i][i] = math.sqrt(A[i][i] - suma)
            U[i][i] = L[i][i]

            for k in range(i+1,n):
                suma = 0
                for j in range(i):
                    suma += (L[k][j] * U[j][i])
                L[k][i] = (A[k][i] - suma) / U[i][i]

            for k in range(i+1,n):
                suma = 0
                for j in range(i):
                    suma += (L[i][j] * U[j][k])
                U[i][k] = (A[i][k] - suma) / L[i][i]

        suma = 0
        for j in range(n-1):
            suma += (L[n-1][j] * U[j][n-1])
        L[n-1][n-1] = math.sqrt(A[n-1][n-1] - suma)
        U[n-1][n-1] = L[n-1][n-1]

        la = np.around(L, decimals=4)
        dicL[i] = copy.deepcopy(la)
        ua = np.around(U, decimals=4)
        dicU[i] = copy.deepcopy(ua)

        print("Matriz L")
        print(L)
        print("Matriz U")
        print(U)
        z = frontSubstitution(L, b)
        x = backSubstitution(U, z)
        print(x)

        print(x)
        print(dicL)
        print(dicU)
        return (x,dicL,dicU,None)
    else:
        message = 'Determinant Value = 0, try again with another matrix'
        print(message)
        return None, None, None, message

def frontSubstitution(A, b):
    n = len(A)
    x = np.zeros((n))
    for i in range(n):
        sum = 0
        for j in range(i):
            sum +=  A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]
    return x

def backSubstitution(A, b):
    n = len(A)
    x = np.zeros((n))
    for i in range(n-1, -1, -1):
        sum = 0.0
        for j in range (i+1, n):
            sum += A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]
    return x


#A = [[4, 12, -16],
#    [12, 37, -43],
#    [-16, -43, 98]]
#A = np.array(A)
#b = np.ones(3)
#choleskyy(A, b)   