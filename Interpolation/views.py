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
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        x = []
        y = []
        for i in range(n):
            x.append(float(request.POST.get('vector'+str(i))))
            y.append(float(request.POST.get('vectorb'+str(i))))
        for i in range(1,len(x)):
            if(x[i]<x[i-1]):
                return render(request, "lagrange.html", {'message': 'Insert Vector X\'s data in a incremental order'})
            for j in range(1,len(x)):
                if(i!=j):
                    if(x[i]==x[j]):
                        return render(request, "lagrange.html", {'message': 'Error: There are equal values of x'})
        try:
            data = lagrange(x, y)
        except:
            return render(request, "lagrange.html",{'message':'Error: Something went wrong'})
        return render(request, "lagrange.html", {'polinomio': data})
    return render(request, "lagrange.html", {'polinomio': ''})


def vandermondeP(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        x = []
        y = []
        for i in range(n):
            x.append(float(request.POST.get('vector'+str(i))))
            y.append(float(request.POST.get('vectorb'+str(i))))
        for i in range(1,len(x)):
            if(x[i]<x[i-1]):
                return render(request, "vandermonde.html", {'message': 'Insert Vector X\'s data in a incremental order'})
            for j in range(1,len(x)):
                if(i!=j):
                    if(x[i]==x[j]):
                        return render(request, "vandermonde.html", {'message': 'Error: There are equal values of x'})
        try:
            data = vandermonde(x, y)
        except:
            return render(request, "vandermonde.html",{'message':'Error: Something went wrong'})
        ecuacion=''
        for i in data[0]:
            n=n-1
            if(i>=0):
                ecuacion+='+'+str(i)+'x^'+str(n)
            else:
                ecuacion+=str(i)+'x^'+str(n)
        return render(request, "vandermonde.html", {'polinomio': data[0],'matriz':data[1], 'ecuacion':ecuacion})
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
        try:
            result = divide_dif(x, y)
            print(result[0])
            return render(request, "dif_Divididas.html", {'Polinomio': result[0], 'D': result[1],'message':result[2]})
        except:
            return render(request, "dif_Divididas.html", {'data': ''})
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

        print(method_splines)
        print(method_gauss)
        if method_splines == 'cuad':
            result = trazcuad_spline(x,y,method_gauss)
        elif method_splines == 'lin':
            result = trazlin_spline(x,y,method_gauss)
        elif method_splines == 'cub':
            result = trazcub_spline(x,y,method_gauss)

        if result[0] != None:
            traces=result[0].split(" ")
        return render(request, "splines.html",{'traces':traces,'steps':result[3],'A':result[1],'b':result[2],'x':result[4], 'message':result[5]})

    return render(request, "splines.html",{'data':''})   
