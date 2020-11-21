import numpy as np
import math

def cholesky(A, b):
    #Inicialización
    n = len(A)
    L = np.eye(n)
    U = np.eye(n)

    #factorization
    for i in range(n-1):
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

    print("Matriz L")
    print(L)
    print("Matriz U")
    print(U)
    z = frontSubstitution(L, b)
    x = backSubstitution(U, z)
    print(x)


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


A = [[4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]]
#A = np.array(A)
#b = np.ones(3)
#cholesky(A, b)   