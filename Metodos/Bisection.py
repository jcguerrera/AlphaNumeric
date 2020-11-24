import sympy as sm
import math
import sys
import json
import base64
import pandas as pd


def bisection(funcion, xi, xs, nIter, iter):
    results = {}
    if nIter > 0:
        x = sm.symbols('x')
        fxi = sm.sympify(funcion).subs(x, xi)
        fxs = sm.sympify(funcion).subs(x, xs)
        sm.plot(funcion)
        if (fxi == 0):
            print(fxi)
        elif (fxs == 0):
            print(fxs)
        elif (fxs * fxi < 0):
            xm = (xi + xs) / 2
            fxm = sm.sympify(funcion).subs(x, xm)
            count = 1
            error = iter + 1
            results[count] = [float(xi), float(xm), float(xs), float(fxm), float(error)]
            while ((error > iter) and (count < nIter)):
                if (fxi * fxm < 0):
                    xs = xm
                else:
                    xi = xm
                xaux = xm
                xm = (xi + xs) / 2
                fxm = sm.sympify(funcion).subs(x, xm)
                error = abs(xm - xaux)
                count += 1
                results[count] = [float(xi), float(xm), float(xs), float(fxm), float(error)]
            print(results)
        return results
    else:
        results['message'] = 'Error'
        print('el intervalo no sirve')
        return results


#print(bisection('ln((sin(x)^2)+1)-(1/2)',0,1,100,0.0000001))

#bisection('ln((sin(x)^2)+1)-(1/2)',0,1,100,0.0000001)

