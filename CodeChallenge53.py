import numpy as np 

m,n = np.random.randint(3,5),np.random.randint(3,5)
A = np.round(np.random.randn(m,n) * 10)
B = np.round(np.random.randn(m,n) * 10)

# CREATING SYMMETRIC MATRIX
S = A @ A.T 
P = B @ B.T 

# COMPUTE SUM
def computeSum(M1, M2):
    return (M1 + M2)/100 

# COMPUTE MULTIPLY
def computeMul(M1, M2):
    return (M1 @ M2)/100 

# COMPUTE HADAMARD
def computeHadaMard(M1, M2):
    return (np.multiply(M1, M2))/100


if __name__ == '__main__':

    print(S)
    print('')
    print(P)
    print('ADD')

    sum_Mat = computeSum(S,P)
    mul_Mat = computeMul(S,P)
    mul_Had = computeHadaMard(S,P)



    print(sum_Mat)
    print('MUL')
    print(mul_Mat)
    print('HAD')
    print(mul_Had)

    # print(A-A.T)
    

