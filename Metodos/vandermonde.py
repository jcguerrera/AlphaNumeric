from Metodos.GaussianElimination import *

def vandermonde(x, y):
    matriz = []
    for i in range(len(x)):
        matriz.append([])
    fila = 0

    for i in x:
        for j in range(len(x)-1,-1,-1):
            matriz[fila].append(i**j)
        fila+=1
    print('A:')
    printMatriz(matriz)
    return totalGaussianElimination(matriz, y)[0]
    

#x = [-1, 0, 3, 4]
#y = [15.5, 3, 8, 1]

#vandermonde(x,y)