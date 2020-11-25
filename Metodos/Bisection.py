import sympy as sm
import math
import sys
import json
import base64
import pandas as pd


def bisection(funcion, xi, xs, nIter, iter):
    results = {}
    response = ''
    message = ''
    try:
        if nIter > 0:
            x = sm.symbols('x')
            fxi = sm.sympify(funcion).subs(x, xi)
            fxs = sm.sympify(funcion).subs(x, xs)
            if (fxi == 0):
                print(fxi)
                response= 'xi is a root'
                return None,response,None
            elif (fxs == 0):
                print(fxs)
                response = 'xs is a root'
                return None, response, None
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
            if (len(results) == 0):
                response = 'Error in given data'
                message = 'Error in given data'
                return (None, response, message)

            response = 'Succesful output'
            return results,response ,None
        else:
            response='Iteration number is not positive'
            message = 'Error'
            return (None,response,message)
    except:
        message = 'Error in given data'
        return (None, response, message)


print(bisection('ln(x)-1',1,2,100,0.0000001))

#bisection('ln((sin(x)^2)+1)-(1/2)',0,1,100,0.0000001)

