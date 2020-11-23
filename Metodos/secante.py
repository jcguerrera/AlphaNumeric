import abc
import sympy as sm


def secant(x0, x1, nInterations, tol, function):
    results = {}
    add = {}

    x = sm.symbols('x')
    fx0 = sm.sympify(function).subs(x, x0)

    if (fx0 == 0):
        print(x0 + "is root")
    else:
        fx1 = sm.sympify(function).subs(x, x1)
        cont = 1
        error = tol + 1
        det = fx1 - fx0
        xi = 0
        results [cont-1] = [float (x0), float (fx0), float (0)]
        results [cont] = [float (x1), float (fx1), float (0)]
        while (fx1 != 0 and error> tol and det!= 0 and cont <nInterations):

            xi = x1 -((fx1 * (x1-x0)) / det)
            error = abs(xi-x1)
            x0 = x1
            fx0 = fx1
            x1 = xi
            fx1 = sm.sympify(function).subs(x, x1)
            det = fx1 - fx0
            cont = cont + 1
            results [cont] = ([round(float (xi),10), round(float (fx1),10), round(float (error),10)])

        
           

        if (fx1 == 0):
           
            add = (str(x0)+" is a root")
        

        elif (error <tol):
            add= (str(x1)+" was found as an approximation with a tolerance of = "+str(tol))
        
        elif (det == 0):
            add= (str(x1)+"is a possible multiple root")

        else:
            add=("The method failed in "+str(nInterations)+ " iterations")

    return results,add
#print(secant(0.5, 1.0, 100, 0.0000001, 'ln ((sin (x) ^ 2) +1) - (1/2)')[0])