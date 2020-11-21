import sympy as sm
import math
import sys

def falseRule(a, b, funcion, limite_iteraciones, tolerancia):
    results = {}
    x = sm.symbols('x')
    funcion = sm.sympify(funcion)
    fa = funcion.subs(x, a)
    fb = funcion.subs(x, b)
    if(fa == 0):
        print('a es raiz')
    elif(fb == 0):
        print('b es raiz')
    elif(fa * fb < 0):
        error = 1
        cont = 1
        c = (fb*a - fa*b)/(fb - fa)
        fc = funcion.subs(x, c)
        print('iter|    a    |   c   |   b   |   fc  |   error')
        while(fc != 0 and cont < limite_iteraciones and error > tolerancia):
            results[cont]=[float(a),float(c),float(b),float(fc),float(error)]
            print(cont,a,c,b,fc,error)
            if (fa * fc < 0):
                b = c
                fb = funcion.subs(x, c)
            else:
                a = c
                fa = funcion.subs(x, c)
            caux = c
            c = (fb*a - fa*b)/(fb - fa)
            fc = funcion.subs(x, c)
            error = abs(caux - c)
            cont+=1
        if (fc == 0):
            print('c is a root '+ str(c))
            results['message']='c is a root '+ str(c)
        elif (error < tolerancia):
            print('c is an approximation of the root c: '+ str(c) +' error: '+ str(error)+ ' in the iteration '+str(cont))
            results['message']='c is an approximation of the root c: '+ str(c) +' error: '+ str(error)+ ' in the iteration '+str(cont)
        else:
            print('number of maximum iterations reached, convergence was not reached')
            results['message']='number of maximum iterations reached, convergence was not reached'
    else:
        print('inadequate interval, does not satisfy the theorem fa * fb < 0')
        results['message']='inadequate interval, does not satisfy the theorem fa * fb < 0'
    return results

#funcion = 'ln((sin(x)^2)+1)-(1/2)'
#falseRule(-1.2, -0.8, funcion, 100, 0.0000001)