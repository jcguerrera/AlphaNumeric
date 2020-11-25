import math
import sympy as sm

def fixedPointt(function1, function2, xa, iter, tol):

    print(xa)
    print(iter)
    print(tol)
    results = {}

    x = sm.symbols('x')
    function1 = sm.sympify(function1)
    function2 = sm.sympify(function2)
    print(function1)
    print(function2)

    fx = function1.subs(x, xa)

    cont = 0
    xn = 0

    error = tol + 1
    while((fx != 0) and error > tol and cont < iter):
        xn = function2.subs(x, xa)
        fx = function1.subs(x, xn)
        error = abs(xn - xa)
        results[cont]=[float(xa),float(xn),float(fx),float(error)]
        xa = xn
        cont += 1
    
    if fx == 0:
        message = ("Xa: " + str(xa) + " is a root")
    elif error < tol :
        message = ("Xa: " + str(xa) + " approximate root with tolerance: " + str(tol))
    else:
        message = ("Fail in iteration: " + str(iter))
    
    return results, message

#print(fixedPointt('x**3 + 4 * x**2 - 10', '(10/(x+4))^(1.0/2)', float(1.5), 11, float(0.000000005)))