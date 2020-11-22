from django.shortcuts import render
from Metodos.SOR import sor
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

        result = sor(matrix,b,x0,float(w),float(tol),float(nIter))
        return render(request, "sor.html", {'Radio': result[0], 'T': result[1], 'C': result[2],'data': result[3]})


    return render(request, "sor.html",{'data':''})