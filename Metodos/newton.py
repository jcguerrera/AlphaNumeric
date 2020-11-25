import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

def newtonn(function, x0, iter, tol):
    results = {}

    x = sm.symbols('x')
    function = sm.sympify(function)
    dFunction = sm.diff(function, x)

    fx = function.subs(x, x0)
    dFx = dFunction.subs(x, x0)

    cont = 1
    error = tol + 1
    
    while( (fx != 0) and error > tol and (dFx != 0) and cont < iter):
        x1 = x0 - fx/dFx
        fx = function.subs(x, x1)
        dFx = dFunction.subs(x, x1)
        error = abs(x1-x0)

        results[cont]=[float(x0),float(x1),float(fx),float(dFx),float(error)]

        x0 = x1
        cont += 1

    if fx == 0:
        message = ("X0: " + str(x0) + " is root")
    elif error < tol:
        message = ("X0: " + str(x0) + " approximate root with tolerance: " + str(tol))
    elif dFx == 0:
        message = ("X0: " +  str(x0) + " is probably a multiple root")
    else:
        message = ("Fail in iteration: " + str(iter))
    
    return results, message


def draw():
    x = np.linspace(-2, 2, 100)
    plt.plot(x, x**3 - np.cos(x))
    plt.grid()
    plt.show()


#print(newtonn('x^3 - cos(x)', 1.0, 10, 0.000000005))
#draw()