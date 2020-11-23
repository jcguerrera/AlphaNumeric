import sympy as sm
import sys
import pandas as pd


def incremental_search(funcion,xi, delta, nIter):
    results = {}
    if delta <= 0:
        print("El delta debe ser positivo")
        sys.exit(1)
    elif nIter > 0:

        x = sm.symbols('x')
        x_a = xi
        current_X = x_a+delta
        f_a = sm.sympify(funcion).subs(x,x_a)
        currentF = sm.sympify(funcion).subs(x,current_X)
        contador = 0
        while (contador < nIter):
            if currentF*f_a<0:
                results[contador] = [float(x_a),float(current_X)]
            x_a = current_X
            current_X = current_X + delta
            f_a = currentF
            currentF = sm.sympify(funcion).subs(x,current_X)
            contador = contador + 1

        return results

    else:
        print("Las iteraciones deben ser un numero positivo")
        results['message'] = 'Error'
        print('el intervalo no sirve')
        return results

def print_function(results):
    index = []
    x1 = []
    x2 = []
    for i in results:
        index.append(i)
        x1.append(results[i][0])
        x2.append(results[i][1])

    data = {'xi': x1,
            'xs': x2,
            }
    df = pd.DataFrame(data, index=index)
    print(df)

#incremental_search("ln((sin(x)^2)+1)-(1/2)",-3,0.5,100)