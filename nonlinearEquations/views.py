from django.shortcuts import render

# Create your views here.
from Metodos.Bisection import bisection
from Metodos.falseRule import falseRule
from Metodos.IncrementalSearch import incremental_search


def bisectionP(request):
    if 'f_function' in request.POST:
        funcion = request.POST.get('f_function')
        xi = request.POST.get('x0_value')
        xs = request.POST.get('x1_value')
        nIter = request.POST.get('nIter')
        iter = request.POST.get('tol')

        print(funcion, xi, xs, nIter, iter)
        data = bisection(str(funcion), float(xi), float(xs), float(nIter), float(iter))
        print(data)

        return render(request, "bisection.html", {'data': data})

    return render(request, "bisection.html", {'data': ''})


def incremental_SearchP(request):
    print('hola')
    if 'f_function' in request.POST:
        funcion = request.POST.get('f_function')
        xi = request.POST.get('x_value')
        delta = request.POST.get('delta')
        nIter = request.POST.get('nIter')

        print(funcion, xi, delta, nIter)
        la_que_sirve = 'ln((sin(x)^2)+1)-(1/2)'
        funcion = funcion.replace(' ', '')
        if (la_que_sirve == funcion):
            print('Moreno GEI')

        data = incremental_search(str(funcion),float(xi),float(delta),float(nIter))
        print(data)

        return render(request, "IncrementalSearch.html", {'data': data})

    return render(request, "IncrementalSearch.html", {'data': ''})

def falseRuleP(request):
    if 'f_function' in request.POST:
        funcion = request.POST.get('f_function')
        a = request.POST.get('a')
        b = request.POST.get('b')
        nIter = request.POST.get('nIter')
        iter = request.POST.get('tol')

        print(funcion, a, b, nIter, iter)
        data = falseRule(float(a), float(b), str(funcion), float(nIter), float(iter))
        print(data)

        return render(request, "falseRule.html", {'data': data,'message':data['message']})

    return render(request, "falseRule.html", {'data': ''})