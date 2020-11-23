import numpy as np
from scipy import linalg as LA
import pandas as pd
import copy

def sor(A, b, x0, w, tol, Nmax):
    results = {}
    det = np.linalg.det(A)
    if(det != 0):
        d = np.diag(A)
        D = np.diagflat(d)
        L = -np.tril(A) + D
        U = -np.triu(A) + D
        T = np.linalg.inv(D - (w * L)).dot((1 - w) * D + (w * U))
        C = w * np.linalg.inv(D - (w * L)).dot(b)
        xant = x0
        E = 1000
        cont = 0
        val, evec = np.linalg.eig(T)
        resp = max(abs(val))
        while E > tol and cont < Nmax:
            xact = np.dot(T, xant) + C
            short = ['{:.6f}'.format(elem) for elem in xact]
            E = np.linalg.norm(xant - xact)
            xant = xact
            cont = cont + 1
            results[cont] = [float(E), short]

        print_iter(results)
        print('Spectral Radious ', resp)
        print('T', T)
        print('C', C)

        return (resp,T,C,results)
    else:
        results['message'] = 'Error'
        return ('','','',results)


def print_iter(results):
    index = []
    x = []
    error = []
    for i in results:
        index.append(i)
        error.append(results[i][0])
        x.append(results[i][1])

    data = {'Error': error,
            'X': x
            }
    df = pd.DataFrame(data, index=index)
    print(df)


'''
A = [[4.0, -1.0, 0.0, 3.0],
     [1.0, 15.5, 3.0, 8.0],
     [0.0, -1.3, -4.0, 1.1],
     [14.0, 5.0, -2.0, 30.0],
     ]

b2 = [1, 1, 1, 1]
x = [0, 0, 0, 0]

sor(A, b2, x, 1.5, 0.0000001, 100)
'''



