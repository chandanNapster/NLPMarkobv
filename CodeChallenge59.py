import numpy as np


# PROVE THAT <Aw,v> == <v, Aw>

# <A,B> = trace(A transpose B)
n1 = 3
n2 = 3
n3 = 3
n4 = 3


v = np.round(np.random.randn(n1) * 10)
w = np.round(np.random.rand(n2) * 10)
A = np.round(np.random.randn(n3,n4) * 10)

A = A @ A.T 

Aw = np.dot(A,w)
Av = np.dot(A,v)


    
def frob_norm(M1, V1):
    return np.dot(M1, V1)

if __name__ == '__main__':
    print('v')
    print(v)
    print('w')
    print(w)
    print('Aw')
    print(Aw)
    print('')
    print(frob_norm(Aw, v))  
    print(frob_norm(w, Av))  