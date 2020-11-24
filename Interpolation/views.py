from django.shortcuts import render
import requests
from Interpolation import templates
from Metodos.lagrange import lagrange
from Metodos.vandermonde import vandermonde
from Metodos.Dif_Divididas import divide_dif


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
                if(x[i]==x[j]):
                    return render(request, "lagrange.html", {'message': 'Error: There are equal values of x'})

        data = lagrange(x, y)
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
                if(x[i]==x[j]):
                    return render(request, "lagrange.html", {'message': 'Error: There are equal values of x'})
        data = vandermonde(x, y)
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

        result = divide_dif(x, y)
        print(result[0])
        return render(request, "dif_Divididas.html", {'Polinomio': result[0], 'D': result[1]})

    return render(request, "dif_Divididas.html", {'data': ''})
