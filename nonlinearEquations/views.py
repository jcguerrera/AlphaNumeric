import io

from django.http import HttpResponse
from django.shortcuts import render
import sympy as sm
from matplotlib.backends.backend_agg import FigureCanvasAgg
from Metodos.Bisection import bisection
from Metodos.falseRule import falseRule
from Metodos.IncrementalSearch import incremental_search
from Metodos.secante import secant
from Metodos.raices_mult import roots_mult
from Metodos.newton import newtonn
from Metodos.fixedPoint import fixedPointt
# Create your views here.



def bisectionP(request):
    if 'f_function' in request.POST:
        funcion = request.POST.get('f_function')
        xi = request.POST.get('x0_value')
        xs = request.POST.get('x1_value')
        nIter = request.POST.get('nIter')
        iter = request.POST.get('tol')

        print(funcion, xi, xs, nIter, iter)
        try:
            data,noti,message = bisection(str(funcion), float(xi), float(xs), float(nIter), float(iter))
            print(data)

            return render(request, "bisection.html", {'data': data,'message':noti,'Error':message})
        except:
            return render(request, "bisection.html", {'data': ''})
    return render(request, "bisection.html", {'data': ''})


def incremental_SearchP(request):
    if 'f_function' in request.POST:
        funcion = request.POST.get('f_function')
        xi = request.POST.get('x_value')
        delta = request.POST.get('delta')
        nIter = request.POST.get('nIter')

        print(funcion, xi, delta, nIter)
        try:
            data,noti,message = incremental_search(str(funcion),float(xi),float(delta),float(nIter))
            print(data)

            return render(request, "IncrementalSearch.html", {'data': data,'message':noti,'Error':message})
        except:
            return render(request, "IncrementalSearch.html", {'data':''})
    return render(request, "IncrementalSearch.html", {'data': ''})

def falseRuleP(request):
    if 'f_function' in request.POST:
        funcion = request.POST.get('f_function')
        a = request.POST.get('a')
        b = request.POST.get('b')
        nIter = request.POST.get('nIter')
        iter = request.POST.get('tol')

        print(funcion, a, b, nIter, iter)
        try:
            data = falseRule(float(a), float(b), str(funcion), float(nIter), float(iter))
        except:
            return render(request, "falseRule.html",{'message':'Error: Something went wrong'})
        #print(data)

        return render(request, "falseRule.html", {'data': data,'message':data['message']})

    return render(request, "falseRule.html", {'data': ''})



def secanteP(request):
    if 'x0' in request.POST:
        x0 = request.POST.get('x0')
        x1 = request.POST.get('x1')
        i = request.POST.get('i')
        t = request.POST.get('t')
        f = request.POST.get('f')
        funcion= f.replace(' ', '')
        try:
            data = secant(float(x0),float(x1),float(i),float(t),funcion)
            return render(request, "secante.html",{'data':data[0],'add':data[1]})
        except:
            return render(request, "secante.html",{'message':"You should check in on some of those matrix fields"})

    return render(request, "secante.html",{'secante':''})


def raices_multiplesP(request):
    if 'x0' in request.POST:
        x0 = request.POST.get('x0')
        i = request.POST.get('i')
        t = request.POST.get('t')
        f1 = request.POST.get('f1')
        f2 = request.POST.get('f2')
        f3 = request.POST.get('f3')

        funcion_1= f1.replace(' ', '')
        funcion_2= f2.replace(' ', '')
        funcion_3= f3.replace(' ', '')
        try:
            
            data = roots_mult(float(x0),float(i),float(t),funcion_1,funcion_2,funcion_3)
            return render(request, "raices_multiples.html",{'data':data[0],'add':data[1]})

        except: 
            return render(request, "raices_multiples.html",{'message':"You should check in on some of those matrix fields"})

        
        
    return render(request, "raices_multiples.html",{'raices_multiples':''})


def newton(request):
    if 'f_function' in request.POST:
        function = request.POST.get('f_function')
        x0 = request.POST.get('x0')
        i = request.POST.get('iter')
        tol = request.POST.get('tol')

        function= function.replace(' ', '')

        try:
            
            data,message = newtonn(str(function), float(x0), int(i), float(tol))
            return render(request, "newton.html", {'data': data, 'message' : message})

        except: 
            print(2)
            return render(request, "newton.html", {'data': ''})
    return render(request, "newton.html",{'data':''})


def fixedPoint(request):
    if 'f_function1' in request.POST:
        function1 = request.POST.get('f_function1')
        function2 = request.POST.get('f_function2')
        xa = request.POST.get('xa')
        i = request.POST.get('iter')
        tol = request.POST.get('tol')

        function1 = function1.replace(' ', '')
        function2 = function2.replace(' ', '')

        try:
            print(1)
            data,message = fixedPointt(str(function1), str(function2), float(xa), int(i), float(tol))
            print(data)
            return render(request, "fixedPoint.html", {'data': data, 'message' : message})

        except: 
            print(2)
            return render(request, "fixedPoint.html", {'data': ''})
    return render(request, "fixedPoint.html",{'data':''})