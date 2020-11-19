from GaussianElimination_splines import simpleGaussianElimination,partialGaussianElimination,totalGaussianElimination, backSubstitution, sortResult

def matrix_cuad(x, b):
    a = [[0 for i in range((len(x)-1)*3)] for j in range((len(x)-1)*3)]
    a[0][0] = x[0]**2
    a[0][1] = x[0]
    a[0][2] = 1
    a[1][0] = x[1]**2
    a[1][1] = x[1]
    a[1][2] = 1

    j = 3
    for i in range(2,len(x)):
        a[i][j] = x[i]**2
        a[i][j+1] = x[i]
        a[i][j+2] = 1
        j += 3  

    i = 1
    j = 0
    for k in range(len(x),((len(x)*2)-2)):
        b += [0]
        a[k][j] = x[i]**2
        a[k][j+1] = x[i]
        a[k][j+2] = 1
        a[k][j+3] = -(x[i]**2)
        a[k][j+4] = -x[i]
        a[k][j+5] = -1 
        i += 1
        j += 3
        
    i = 1
    j = 0
    for k in range(((len(x)*2)-2),len(a)-1):
        b += [0]
        a[k][j] = 2*x[i]
        a[k][j+1] = 1
        a[k][j+2] = 0
        a[k][j+3] = -2*x[i]
        a[k][j+4] = -1
        a[k][j+5] = 0 
        i += 1
        j += 3
        
    b += [0]
    a[len(a)-1][0] = 2
    return a,b

def traces(x):
    result = ""
    j = 0
    for i in range(len(x)):
        if j == 0:
            if x[i] >= 0.0:
                result += "+"+str(x[i])+"x**2"
            else:
                result += str(x[i])+"x**2"
        elif j == 1:
            if x[i] >= 0.0:
                result += "+"+str(x[i])+"x"
            else:
                result += str(x[i])+"x"
        else:
            if x[i] >= 0.0:
                result += "+"+str(x[i])+" "
            else:
                result += str(x[i])+" "
            j = -1
        j += 1
    print("\n Traces: \n")
    for i in result.split(" "):
        print(i)
    

if __name__ == "__main__":
    x = [-1,0,3,4]
    y = [15.5,3,8,1]
    b = y
    A, b = matrix_cuad(x,b)
    print("A:  \n"+str(A))
    print("b: \n"+str(b))
    t1=totalGaussianElimination(A, b)
    #t2=partialGaussianElimination(A, b)
    #t3=simpleGaussianElimination(A, b)

    traces(t1)
    #traces(t2)
    #traces(t3)
