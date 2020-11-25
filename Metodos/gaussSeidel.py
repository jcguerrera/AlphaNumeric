import math
import numpy as np


def gaussSeidell(A, b, t, iter, x0):
    print('hola')
    results = {}
    message = ''
    n = len(A)
    l = len(A)
    if (n != l):
        message = ("A is nor a square matrix.")
        return None, None, None, None, message
    else:
        x = [None]*n
        aux = 0
        cont = 0
        E = t + 1
        iteration = 1
        while (E > t and cont <= iter):
            print("iter: ", iteration)
            E = 0
            for i in range(0, n):
                suma = 0
                for j in range(0, n):
                    if (i != j):
                        suma = suma + A[i][j] * x0[j]
                x[i] = (((b[i] - suma) / A[i][i]))
                aux = x[i] - x0[i]
                E = E + math.pow(aux, 2)
                x0[i] = x[i]
                print("x", (i + 1), ": ", x0[i])

            E = math.pow(E, 0.5)
            print("E = ", E)
            print("")
            iteration = iteration + 1
            cont = cont+1
            results[cont] = [float(E), x0]

        if (E < t):
            D = np.diag(np.diag(A))
            U = -np.triu(A, 1)
            L = -np.tril(A, -1)
            T = (np.dot((np.linalg.inv(D-L)), U))
            C = (np.dot((np.linalg.inv(D-L)), b))
            print("T: ")
            print(T)
            print("C:")
            print(C)
            values, normalized_eigenvectors = np.linalg.eig(T)  # T es la matriz
            spectral_radius = max(abs(values))
            print("\nSpectral Radius: ", spectral_radius)
            print('------------------------------------------------')
            return spectral_radius, T, C, results, None
        else:
            message = "Can not find a solution in ", iter, " iterations"
            return None, None, None, None, message

    
    D = np.diag(np.diag(A))
    U = -np.triu(A, 1)
    L = -np.tril(A, -1)
    T = (np.dot((np.linalg.inv(D-L)), U))
    C = (np.dot((np.linalg.inv(D-L)), b))
    print("T: ")
    print(T)
    print("C:")
    print(C)
    values, normalized_eigenvectors = np.linalg.eig(T)  # T es la matriz
    spectral_radius = max(abs(values))
    print("\nSpectral Radius: ", spectral_radius)
    print('----------------------------------------')
    return spectral_radius, T, C, results, None 


#A = [[4, -1, 0, 3],
#     [1, 15.5, 3, 8],
#     [0, -1.3, -4, 1.1],
#     [14, 5, -2, 30]]
#b = [1, 1, 1, 1]
#x0 = [0, 0, 0, 0]
#t = math.pow(10, -7)
#iter = 100
#print(gaussSeidell(A, b, t, iter, x0))

