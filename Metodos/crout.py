import numpy as np
import copy

def croutt(a, b):
    a = np.array(a)
    b = np.array(b)
    print('adios')
    message = ''
    dicL = {}
    dicU = {}
    cout = 0
    m, n = a.shape
    print('ono')
    if (m !=n ):
        print('error')
        message = ("Crout cannot be used.")#Ensure that the number of equations is equal to the number of unknowns
        return (None,None,None, message)
    else:
        print('in')
        l = np.zeros((n,n))
        u = np.zeros((n,n))
        s1 = 0
        s2 = 0

        for m in range(1,n+1):
            print("Stage " + str(m) + ": ")
            la = np.around(l, decimals=4)
            dicL[m] = copy.deepcopy(la)
            ua = np.around(u, decimals=4)
            dicU[m] = copy.deepcopy(ua)
            for i in range(n):
                l[i][0] = a[i][0]
                u[i][i] = 1
            for j in range(1, n):
                u[0][j] = a[0][j] / l[0][0]
            for k in range(1, n):
                for i in range(k, n):
                    for r in range(k): s1 += l[i][r] * u[r][k]
                    l[i][k] = a[i][k] - s1
                    s1 = 0                #Initialize s1 after each summation=0
                for j in range(k+1, n):
                    for r in range(k): s2 += l[k][r] * u[r][j]
                    u[k][j] = (a[k][j] - s2) / l[k][k]
                    s2 = 0                #Initialize s2 after each summation=0
                la = np.around(l, decimals=4)
                dicL[m] = copy.deepcopy(la)
                ua = np.around(u, decimals=4)
                dicU[m] = copy.deepcopy(ua)
            print("U: ")
            print(u)
            print("L: ")
            print(l)

        # 
        y = np.zeros(n)
        s3 = 0
        y[0] = b[0] / l[0][0]    # First calculate the first x solution
        for k in range(1, n):
            for r in range(k):
                s3 += l[k][r] * y[r]
            y[k] = (b[k]-s3) / l[k][k]
            s3 = 0

        x = np.zeros(n)
        s4 = 0
        x[n-1] = y[n-1]
        for k in range(n-2, -1, -1):
            for r in range(k+1, n):
                s4 += u[k][r] * x[r]
            x[k] = y[k] - s4
            s4 = 0

        for i in range(n):
            print("x" + str(i + 1) + " = ", x[i])

        print(x)
        print(dicL)
        print(dicU)
        return (x,dicL,dicU,None)




if __name__ == '__main__':            #When the module is run directly, the following code blocks will be run. When the module is imported, the code blocks will not be run.
    a = np.array([  [4, -1, 0, 3],
                [1, 15.5, 3, 8],
                [0, -1.3, -4, 1.1],
                [14, 5, -2, 30]
                ])
    b = np.array([1,1,1,1])
    croutt(a, b)


