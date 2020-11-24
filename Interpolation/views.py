from django.shortcuts import render
import requests
from Interpolation import templates
from Metodos.lagrange import lagrange
from Metodos.vandermonde import vandermonde
from Metodos.Dif_Divididas import divide_dif
from Metodos.Trazcuad_spline import trazcuad_spline
from Metodos.Trazcub_spline import trazcub_spline
from Metodos.Trazlin_spline import trazlin_spline


# Create your views here.

def lagrangeP(request):
    if 'x' in request.POST:
        x = request.POST.get('x')
        y = request.POST.get('y')
        x = x.split(',')
        y = y.split(',')
        if len(x) == len(y):
            for i in range(len(x)):
                try:
                    x[i] = float(x[i])
                    y[i] = float(y[i])
                except:
                    return render(request, "lagrange.html", {'polinomio': 'error: valores inválidos'})
            print(x, y)
            data = lagrange(x, y)
            return render(request, "lagrange.html", {'polinomio': data})
        else:
            return render(request, "lagrange.html",
                          {'polinomio': 'el tamaño de los vectores es diferente o el separador no es el indicado'})
    return render(request, "lagrange.html", {'polinomio': ''})


def vandermondeP(request):
    if 'x' in request.POST:
        x = request.POST.get('x')
        y = request.POST.get('y')
        x = x.split(',')
        y = y.split(',')
        if len(x) == len(y):
            for i in range(len(x)):
                try:
                    x[i] = float(x[i])
                    y[i] = float(y[i])
                except:
                    return render(request, "vandermonde.html", {'polinomio': 'error: valores inválidos'})
            print(x, y)
            data = vandermonde(x, y)
            return render(request, "vandermonde.html", {'polinomio': data})
        else:
            return render(request, "vandermonde.html",
                          {'polinomio': 'el tamaño de los vectores es diferente o el separador no es el indicado'})
    return render(request, "vandermonde.html", {'polinomio': ''})


def _NewtonP(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))

        x = []
        y = []
        for i in range(n):
            x.append(float(request.POST.get('vector' + str(i))))
            y.append(float(request.POST.get('vectorx' + str(i))))

        print(x)

        result = divide_dif(x, y)
        print(result[0])
        return render(request, "dif_Divididas.html", {'Polinomio': result[0], 'D': result[1]})

    return render(request, "dif_Divididas.html", {'data': ''})

def splinesP(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        method_splines = request.POST.get('method_type_splines')
        method_gauss = request.POST.get('method_type_gauss')
        x = []
        y = []
        aux=[]
        traces =[]
        for i in range(n):
            fila = []
            x.append(float(request.POST.get('vector'+str(i))))
            y.append(float(request.POST.get('vectorx'+str(i))))

        result = ()

        try:
            print(method_splines)
            print(method_gauss)
            if method_splines == 'cuad':
                result = trazcuad_spline(x,y,method_gauss)
            elif method_splines == 'lin':
                result = trazlin_spline(x,y,method_gauss)
            elif method_splines == 'cub':
                result = trazcub_spline(x,y,method_gauss)

            traces=result[0].split(" ")
            return render(request, "splines.html",{'traces':traces,'steps':result[3],'A':result[1],'b':result[2],'x':result[4]})
   
        except:
             return render(request, "splines.html",{'message':"You should check in on some of those matrix fields"})
    return render(request, "splines.html",{'data':''})   
