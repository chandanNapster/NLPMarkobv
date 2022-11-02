import numpy as np

n = 4
A = np.round(np.abs(np.random.randn(n,n) * 10)) + 1
dig = []

for i in range(n):
    dig.append(np.random.randint(1,n))

D = np.diag(dig)

print(D)
print('')
print(A)

def std_mul(M1, M2):
    return M1 @ M2 

def had_mul(M1, M2):
    return np.multiply(M1, M2)

print('STD FULL')
print(std_mul(A,A))
print('HAD FULL')
print(had_mul(A,A))

print('STD DIG')
print(std_mul(D,D))
print('HAD DIG')
print(had_mul(D,D))