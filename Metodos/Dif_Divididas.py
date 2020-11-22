import numpy as np

def divide_dif(x,y):
    n = len(x)
    D = np.zeros((n,n))

    D[:,0] = np.conjugate(y)

    for i in range(1,n):
        aux0 = D[i-1:n,i-1]
        aux1 = np.diff(aux0)
        aux2 = np.subtract(x[i:n],x[0:n-1-i+1])
        D[i:n,i] = np.divide(aux1,np.transpose(aux2))

    res = np.diag(D)

    r = '' + '{0:+}'.format(res[0])
    m = '(x' + '{0:+}'.format(-x[0]) + ')'
    for i in range(1,n):
        r += '{0:+}'.format(res[i]) + m
        m += '(x' + '{0:+}'.format(-x[i]) + ')'
    r = r.replace('x+0','x')
    print('Matrix D: \n',D)
    print('Coef: ',res)
    print('Newton Polinom : ', r)

    return (r,D)


'''x = [-1, 0, 3, 4]
y = [15.5, 3, 8, 1]

divide_dif(x,y)'''