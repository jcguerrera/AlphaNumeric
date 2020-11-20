from django.shortcuts import render
import requests
from Interpolation import templates
from Metodos.lagrange import lagrange
from Metodos.vandermonde import vandermonde
# Create your views here.

def lagrangeP(request):
    if 'x' in request.POST:
        x = request.POST.get('x')
        y = request.POST.get('y')
        x = x.split(',')
        y = y.split(',')
        if len(x)==len(y):
            for i in range(len(x)):
                try:
                    x[i] = float(x[i])
                    y[i] = float(y[i])
                except:
                    return render(request, "lagrange.html",{'polinomio':'error: valores inválidos'})
            print(x,y)
            data = lagrange(x,y)
            return render(request, "lagrange.html",{'polinomio':data})
        else:
            return render(request, "lagrange.html",{'polinomio':'el tamaño de los vectores es diferente o el separador no es el indicado'})
    return render(request, "lagrange.html",{'polinomio':''})

def vandermondeP(request):
    if 'x' in request.POST:
        x = request.POST.get('x')
        y = request.POST.get('y')
        x = x.split(',')
        y = y.split(',')
        if len(x)==len(y):
            for i in range(len(x)):
                try:
                    x[i] = float(x[i])
                    y[i] = float(y[i])
                except:
                    return render(request, "vandermonde.html",{'polinomio':'error: valores inválidos'})
            print(x,y)
            data = vandermonde(x,y)
            return render(request, "vandermonde.html",{'polinomio':data})
        else:
            return render(request, "vandermonde.html",{'polinomio':'el tamaño de los vectores es diferente o el separador no es el indicado'})
    return render(request, "vandermonde.html",{'polinomio':''})