from django.shortcuts import render
from Metodos.SOR import sor
from Iterative import templates
from Metodos.Jacobi import Jacobi
from Metodos.gaussSeidel import gaussSeidell

# Create your views here.

def _sor(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        w = request.POST.get('w')
        nIter = request.POST.get('nIter')
        tol = request.POST.get('tol')
        matrix = []
        b = []
        x0 = []
        for i in range(n):
            fila = []
            b.append(float(request.POST.get('vector'+str(i))))
            x0.append(float(request.POST.get('vectorx' + str(i))))
            for j in range(n):
                fila.append(float(request.POST.get('matrix'+str(i)+str(j))))
            matrix.append(fila)
        print(x0)
        try:
            result = sor(matrix,b,x0,float(w),float(tol),float(nIter))
            print(result[4])
            return render(request, "sor.html", {'Radio': result[0], 'T': result[1], 'C': result[2],'data': result[3],'message': result[4]})
        except:
            return render(request, "sor.html", {'data': ''})
    return render(request, "sor.html",{'data':''})

def JacobiP(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        iter = request.POST.get('i')
        t = request.POST.get('t')
        matrix = []
        b = []
        x0 = []
        for i in range(n):
            fila = []
            b.append(float(request.POST.get('vector'+str(i))))
            x0.append(float(request.POST.get('vectorx'+str(i))))
            for j in range(n):
                fila.append(float(request.POST.get('matrix'+str(i)+str(j))))
            matrix.append(fila)
        print(matrix)
        print(b)
        print(x0)

        result = ()
        '''
        A= [[4, -1, 0,3],
        [1, 15.5, 3, 8],
        [0, -1.3, -4, 1.1],
        [14, 5, -2, 30]]

        d = [1,1,1,1]
        x1 = [0, 0, 0,0]
        '''
        try:
            result = Jacobi(matrix,b,float(t),int(iter),x0)
            print(result[0])

            if(result[3]<1):
                return render(request, "jacobi.html",{'data':result[0],'T':result[1],'C':result[2],'spectralRadius':result[3]})
            else:
                return render(request, "jacobi.html",{'message': "The spectral radius must be less than 1.0"})
        
        except:
            return render(request, "jacobi.html",{'message':"You should check in on some of those matrix fields"})
    return render(request, "jacobi.html",{'data':''})


def gausSeidel(request):
    if 'n' in request.POST:
        n = int(request.POST.get('n'))
        nIter = request.POST.get('nIter')
        tol = request.POST.get('tol')
        matrix = []
        b = []
        x0 = []
        for i in range(n):
            fila = []
            b.append(float(request.POST.get('vector'+str(i))))
            x0.append(float(request.POST.get('vectorx' + str(i))))
            for j in range(n):
                fila.append(float(request.POST.get('matrix'+str(i)+str(j))))
            matrix.append(fila)
        print(x0)
        try:
            result = gaussSeidell(matrix, b, float(tol), float(nIter),  x0)
            print(result[4])
            return render(request, "gausSeidel.html", {'Radio': result[0], 'T': result[1], 'C': result[2],'data': result[3],'message': result[4]})
        except:
            return render(request, "gausSeidel.html", {'data': ''})
    return render(request, "gausSeidel.html",{'data':''})