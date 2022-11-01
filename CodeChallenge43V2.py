import numpy as np

Outer1 = 4
Common = 2
Outer2 = 5

A = np.round(np.random.randn(Outer1,Common) * 10)
B = np.round(np.random.randn(Common,Outer2) * 10)
C = np.zeros((Outer1, Outer2))

print(A)
print('')
print(B)
print('')

num_of_rank = Common
rank_Matrix_list = []

for i in range(num_of_rank):
    row = A[:,i]
    col = B[i]
    rank_Matrix_list.append(np.outer(row, col))

for i in rank_Matrix_list:
    C += i 

print(C)
print('')
print(np.matmul(A,B))