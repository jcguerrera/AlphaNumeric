from Metodos.GaussianElimination_splines import simpleGaussianElimination,partialGaussianElimination,totalGaussianElimination, backSubstitution, sortResult
import numpy as np

def matrix_cub(x, b):
    a = [[0 for i in range((len(x)-1)*4)] for j in range((len(x)-1)*4)]
    a[0][0] = x[0]**3
    a[0][1] = x[0]**2
    a[0][2] = x[0]
    a[0][3] = 1
    a[1][0] = x[1]**3
    a[1][1] = x[1]**2
    a[1][2] = x[1]
    a[1][3] = 1

    j = 4
    for i in range(2,len(x)):
        a[i][j] = x[i]**3
        a[i][j+1] = x[i]**2
        a[i][j+2] = x[i]
        a[i][j+3] = 1
        j += 4  

    i = 1
    j = 0
    for k in range(len(x),((len(x)*2)-2)):
        b += [0]
        a[k][j] = x[i]**3
        a[k][j+1] = x[i]**2
        a[k][j+2] = x[i]
        a[k][j+3] = 1
        a[k][j+4] = -(x[i]**3)
        a[k][j+5] = -(x[i]**2)
        a[k][j+6] = -x[i]
        a[k][j+7] = -1
        i += 1
        j += 4
        
    i = 1
    j = 0
    for k in range(((len(x)*2)-2),((len(x)*3)-4)):
        b += [0]
        a[k][j] = 3*(x[i]**2)
        a[k][j+1] = 2*x[i]
        a[k][j+2] = 1
        a[k][j+3] = 0
        a[k][j+4] = -(3*(x[i]**2))
        a[k][j+5] = -(2*x[i])
        a[k][j+6] = -1
        a[k][j+7] = 0 
        i += 1
        j += 4
        
    i = 1
    j = 0
    for k in range(((len(x)*3)-4),((len(x)*4)-6)):
        b += [0]
        a[k][j] = 6*x[i]
        a[k][j+1] = 2
        a[k][j+2] = 0
        a[k][j+3] = 0
        a[k][j+4] = -6*x[i]
        a[k][j+5] = -2
        a[k][j+6] = 0
        a[k][j+7] = 0 
        i += 1
        j += 4
        
    b += [0]*2
    a[len(a)-2][0] = 6*x[0]
    a[len(a)-2][1] = 2
    a[len(a)-1][len(a)-4] = 6*x[len(x)-1]
    a[len(a)-1][len(a)-3] = 2

    return a, b




def traces(x):
    result = ""
    j = 0
    for i in range(len(x)):
        if j == 0:
            if x[i] >= 0.0:
                result += "+"+str(x[i])+"x**3"
            else:
                result += str(x[i])+"x**3"
        elif j == 1:
            if x[i] >= 0.0:
                result += "+"+str(x[i])+"x**2"
            else:
                result += str(x[i])+"x**2"
        elif j == 2:
            if x[i] >= 0.0:
                result += "+"+str(x[i])+"x"
            else:
                result += str(x[i])+"x"
        else:
            if x[i] >= 0.0:
                result += "+"+str(x[i])+" "
            else:
                result += str(x[i])+""
            j = -1
        j += 1

    return(result)

def trazcub_spline(x,y,d):
    unique_elements, count_vector_x = np.unique(x,return_counts=True)
    unique_elements, count_vector_y = np.unique(y,return_counts=True)
    validate = False
    for i in count_vector_x,count_vector_y:
        if(i.all()>1):
            validate = True
            break
    if(validate):
        message= 'There are similar points in vector X or Y'
        return None,None, None,None, None, message

    b = y
    A, b = matrix_cub(x,b)

    try:
        if(d=="T"):
            t1=totalGaussianElimination(A, b)
            return traces(t1[0]),A,b,t1[1],t1[0], None

        elif(d=="P"):
            t2=partialGaussianElimination(A, b)
            return traces(t2[0]),A,b,t2[1],t2[0], None
        elif(d=="S"):
            t3=simpleGaussianElimination(A, b)
            return traces(t3[0]),A,b,t3[1],t3[0], None

    except:
        message= 'Error: Division by 0'
        return None,None, None,None, None, message
    
