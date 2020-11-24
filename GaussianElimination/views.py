from django.shortcuts import render
import requests
from GaussianElimination import templates
from Metodos.GaussianElimination import simpleGaussianElimination, partialGaussianElimination, totalGaussianElimination
import numpy
# Create your views here.

def GaussianEliminationP(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        method = request.POST.get('method_type')
        matrix = []
        b = []
        for i in range(n):
            fila = []
            b.append(int(request.POST.get('vector'+str(i))))
            for j in range(n):
                fila.append(int(request.POST.get('matrix'+str(i)+str(j))))
            matrix.append(fila)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if(i!=j):
                    if(matrix[i]==matrix[j]):
                        return render(request, "matriz.html",{'message':'Error: there are equal rows, Division by zero imminent'})
        det = numpy.linalg.det(matrix)
        if det==0:
            return render(request, "matriz.html",{'message':'Error: Matrix must be nonsingular'})
        result = ()
        try:
            if method == 'S':
                result = simpleGaussianElimination(matrix,b)
            elif method == 'P':
                result = partialGaussianElimination(matrix,b)
            elif method == 'T':
                result = totalGaussianElimination(matrix,b)
        except:
            return render(request, "matriz.html",{'message':'Error: Something went wrong'})
        print('result:', result[1])
        return render(request, "matriz.html",{'x':result[0],'steps':result[1]})
    return render(request, "matriz.html",{'data':''})