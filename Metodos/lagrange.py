#import sympy as sm
import math

def lagrange(x, y):
    n = len(x)
    l = []
    ld = []
    for i in x:
        l1 = ''
        l2 = 1
        for j in x:
            if(i!=j):
                if(j<0):
                    l1+= '(x + '+str(abs(j))+') '
                else:
                    l1+= '(x - '+str(abs(j))+') '
                l2 = l2*(i-j)
        l.append(l1)
        ld.append(l2)

    i = 0
    lf = []
    l1 = 1
    while(i<len(y)):
        l1 = y[i]/ld[i]
        lf.append(l1)
        i+=1
    
    i = 0
    polinomio = ''
    while(i<len(l)):
        if(lf[i]>=0):
            polinomio+= ' + '+str(round(lf[i],3))+l[i]
        else:
            polinomio+= ' '+str(round(lf[i],3))+l[i]
        i+=1
    return(polinomio)

#x = [-1, 0, 3, 4]
#y = [15.5, 3, 8, 1]

#lagrange(x, y)