import sympy as sm
import math
import sys 
import json
import base64
import pandas as pd


def roots_mult(x0, nInterations, tol, function, function2, function3):
    results = {}
    add = {}
    x = sm.symbols ('x')
    fx0 = sm.sympify (function) .subs (x, x0)
    dfx0 = sm.sympify (function2) .subs (x, x0)
    d2fx0 = sm.sympify (function3) .subs (x, x0)

    cont = 0
    error = tol + 1
    xn = 0
    det = (math.pow (dfx0,2)) - (fx0 * d2fx0)
    results [cont] = [float (x0), float (fx0), float (0)]
    while (fx0!= 0 and error> tol and det != 0 and cont <nInterations):
        xn = x0 - ((fx0 * dfx0) / det)
        fx0 = sm.sympify (function) .subs (x, xn)
        dfx0 = sm.sympify (function2) .subs (x, xn)
        d2fx0 = sm.sympify (function3) .subs (x, xn)
        det = (math.pow (dfx0,2)) - (fx0 * d2fx0)
        error = abs (xn-x0)
        x0 = xn
        cont = cont + 1
        results [cont] =([round(float (x0),18), round(float (fx0),18), round(float (error),18)])

    
    
    if (fx0 == 0):
        add =(str (x0) + "is a root")

    elif (error<tol):
        add =(str (x0) + "was found as an approximation with a tolerance of =" + str (tol))
    
    elif (det == 0):
        add =("is an indeterminacy")

    else:
        add =("The method failed in" + str (nInterations) + "iterations")
    
    return results,add
