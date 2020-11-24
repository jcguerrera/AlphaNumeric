from Metodos.GaussianElimination_splines import simpleGaussianElimination,partialGaussianElimination,totalGaussianElimination


def matrix_lin(x, b):
    a = [[0 for i in range((len(x)-1)*2)] for j in range((len(x)-1)*2)]
    a[0][0] = x[0]
    a[0][1] = 1
    a[1][0] = x[1]
    a[1][1] = 1

    j = 2
    for i in range(2,len(x)):
        a[i][j] = x[i]
        a[i][j+1] = 1
        j += 2
        
    i = 1
    j = 0
    for k in range(len(x),((len(x)*2)-2)):
        b += [0]
        a[k][j] = x[i]
        a[k][j+1] = 1
        a[k][j+2] = -x[i]
        a[k][j+3] = -1
        i += 1
        j += 2

    return a,b
    
def traces(x):
    
    
    result = ""
    for i in range(len(x)):
        if i % 2 == 0:
            if x[i] >= 0.0:
                    result += "+"+str(x[i])+"x"
            else:
                    result += str(x[i])+"x"
        else:
            if x[i] >= 0.0:
                    result += "+"+str(x[i])+" "
            else:
                    result += str(x[i])+" "
    

    return(result)
        


def trazlin_spline(x,y,d):
    ''' x = [-1,0,3,4]
    y = [15.5,3,8,1]'''

    b = y
    A, b = matrix_lin(x,b)


    if(d=="T"):
        t1=totalGaussianElimination(A, b)
        return traces(t1[0]),A,b,t1[1],t1[0]

    elif(d=="P"):
        t2=partialGaussianElimination(A, b)
        return traces(t2[0]),A,b,t2[1],t2[0]
    elif(d=="S"):
        t3=simpleGaussianElimination(A, b)
        return traces(t3[0]),A,b,t3[1],t3[0]
    
#print(trazlineal_spline("T")[4])