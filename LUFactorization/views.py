from django.shortcuts import render
from Metodos.SimpleLU import simpleLU
from Metodos.PartialLU import partialLU
from Metodos.doolittle import doolittlee
from Metodos.crout import croutt
# Create your views here.


def _simpleLU(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        method = request.POST.get('method_type')
        matrix = []
        b = []
        for i in range(n):
            fila = []
            b.append(float(request.POST.get('vector'+str(i))))
            for j in range(n):
                fila.append(float(request.POST.get('matrix'+str(i)+str(j))))
            matrix.append(fila)
        print(matrix)
        print(b)
        try:
            if method == 'S':
                result = simpleLU(matrix,b)
                return render(request, "simpleLU.html", {'x': result[0], 'L': result[1], 'U': result[2],'message':result[3]})
            elif method == 'P':
                result = partialLU(matrix,b)
                return render(request, "simpleLU.html", {'x': result[0], 'L': result[1], 'U': result[2],'P': result[3],'message':result[4]})
        except:
            return render(request, "simpleLU.html", {'data': ''})

    return render(request, "simpleLU.html",{'data':''})

def doolittle(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        matrix = []
        b = []
        for i in range(n):
            fila = []
            b.append(float(request.POST.get('vector'+str(i))))
            for j in range(n):
                fila.append(float(request.POST.get('matrix'+str(i)+str(j))))
            matrix.append(fila)
        print(matrix)
        print(b)
        try:
            print(2)
            result = doolittlee(matrix, b, n)
            print('-------------------')
            print(result)
            return render(request, "doolittle.html", {'x': result[0], 'L': result[1], 'U': result[2],'message':result[3]})
        except:
            return render(request, "doolittle.html", {'data': ''})
    return render(request, "doolittle.html",{'data':''})


def crout(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        matrix = []
        b = []
        for i in range(n):
            fila = []
            b.append(float(request.POST.get('vector'+str(i))))
            for j in range(n):
                fila.append(float(request.POST.get('matrix'+str(i)+str(j))))
            matrix.append(fila)
        print(matrix)
        print(b)
        try:
            print(2)
            result = croutt(matrix, b)
            print('-------------------')
            print(result)
            return render(request, "crout.html", {'x': result[0], 'L': result[1], 'U': result[2],'message':result[3]})
        except:
            return render(request, "crout.html", {'data': ''})
    return render(request, "crout.html",{'data':''})