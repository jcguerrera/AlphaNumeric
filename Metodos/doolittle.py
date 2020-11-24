import sympy as sm
import math
import sys
import json
import base64
import numpy as np
import copy

def doolittlee(A,b,size):
    print(1)
    n = size
    message = ''
    u = zero_Matrix(n)
    l = lmatrix(n)
    dicL = {}
    dicU = {}
    A = np.array(A)
    b = np.array(b)
    L = np.eye(size)
    U = np.eye(size)
    print("Etapa 0:")
    print("Matriz L: ")
    print(L)
    print("Matriz U: ")
    print(U)
    for i in range(size):

        print("Etapa " + str(i+1))
        la = np.around(l, decimals=4)
        dicL[i] = copy.deepcopy(la)
        ua = np.around(u, decimals=4)
        dicU[i] = copy.deepcopy(ua)

        for k in range(i, size): 
            suma = 0;
            for j in range(i):
                suma += (L[i][j] * U[j][k]);
            U[i][k] = A[i][k] - suma;

        for k in range(i, size):
            if (i == k):
                L[i][i] = 1;
            else:
                suma = 0;
                for j in range(i):
                    suma += (L[k][j] * U[j][i]);
                L[k][i] = ((A[k][i] - suma)/U[i][i]);
        la = np.around(L, decimals=4)
        dicL[i] = copy.deepcopy(la)
        ua = np.around(U, decimals=4)
        dicU[i] = copy.deepcopy(ua)

        print("Matriz L: ")
        print(L)
        print("Matriz U: ")
        print(U)
    z = frontSubstitution(L, b)
    x = backSubstitution(U, z)
    printResultVector(x)
    print('------------------------')
    return (x,dicL,dicU,None)

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

def printResultVector(vector):
    n = len(vector)
    for i in range(n):
        print('x' + str(i + 1) + ': ' + str(vector[i]))

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


            
#print(doolittle([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]],[1,1,1,1],4))