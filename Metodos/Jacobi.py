import math
import numpy as np
def Jacobi(A, b, t, iter, x0):
    n = len(A)
    l = len(A[0])
    result = {}
    if (n!=l):
        return("A is not a square matrix please check and run again.")
    else:
        det = np.linalg.det(A)
        if det != 0:
            x =[None] * n
            aux=0
            cont = 0
            error = t + 1
            iteration = 1
            T = np.zeros((n, n))
            C = np.zeros(n)
    
            while(error > t and cont <= iter):
                error = 0
                for i in range(0,n):
                    sum = 0
                    for j in range(0,n):
                        if (i != j):
                            sum = sum + A[i][j] * x0[j]
                            T[i][j] = -A[i][j] / A[i][i]
                            C[i] = b[i] / A[i][i]



                    x[i] = (b[i] - sum) / A[i][i]
                    aux = x[i] - x0[i]
                    error = error + math.pow(aux, 2)

                error = math.pow(error, 0.5)



                for i in range(0,n):
                    x0[i] = x[i]
                    print("x"+str(i+1)+": "+str(round(x0[i],4)))



                result[iteration]=(float(error),x)
                iteration=iteration+1
                cont = cont+1

            print(result)
            print("")
            print("T: \n"+str(T))
            print("")
            print("C: \n"+str(C))
            print("")
            spectralRadius = np.amax(abs(T))
            print("Spectral radius: \n"+str(spectralRadius))

        
            if (error < t):
                return(result, T, C,spectralRadius )
            else:
                print ("no solution reached in " + str (iter) + " iterations")
                return       
        else:
            message = 'Determinant Value = 0, try again with another matrix'
        print(message)
        return None, None, None, None, message
    
    
    

    
  
    

        
  
