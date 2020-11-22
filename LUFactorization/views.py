from django.shortcuts import render
from Metodos.SimpleLU import simpleLU
from Metodos.PartialLU import partialLU
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
        result = ()
        if method == 'S':
            result = simpleLU(matrix,b)
            return render(request, "simpleLU.html", {'x': result[0], 'L': result[1], 'U': result[2]})
        elif method == 'P':
            result = partialLU(matrix,b)
            return render(request, "simpleLU.html", {'x': result[0], 'L': result[1], 'U': result[2],'P': result[3]})

    return render(request, "simpleLU.html",{'data':''})