import re
import numpy as np 

M,N = 3,3
my_mat_1 = np.zeros((M,N))
my_mat_1 = my_mat_1 + 1
diag_mat = np.diag([1,2,3])

# print('')
# print(my_mat_1)
# print('')
# print(diag_mat)

# print('MAT @ D')
# print(my_mat_1 @ diag_mat)

# print('D @ MAT')
# print(diag_mat @ my_mat_1)

# print('LIVE -- EVIL RULE')

L = np.round(np.random.randn(19999,3) * 10)
I = np.round(np.random.randn(3,4) * 10)
V = np.round(np.random.randn(4,3) * 10)
E = np.round(np.random.randn(3,19999) * 10)


LIVE = L @ I @ V @ E

# print('LIVE')
res1 = LIVE.T 
# print(res1)

# print('EVIL')
res2 = E.T @ V.T @ I.T @ L.T 
# print(res2)
row, col = np.shape(LIVE)

# print((res1 - res2) == np.zeros(row,col))

LIVE = np.round(np.abs(LIVE / 10000))

# print(LIVE)


for i in range(row):
    sum = np.sum(LIVE[i])
    LIVE[i] = LIVE[i]/sum 

# print(LIVE)
# print('')
# print(LIVE @ LIVE)
# print('')
# print(LIVE @ LIVE @ LIVE)
# print('')
# print(LIVE @ LIVE @ LIVE @ LIVE) 
# print('')
# print(LIVE @ LIVE @ LIVE @ LIVE @ LIVE) 
# print('')
# print(LIVE @ LIVE @ LIVE @ LIVE @ LIVE @ LIVE) 
# print('')
# print(LIVE @ LIVE @ LIVE @ LIVE @ LIVE @ LIVE @ LIVE)  


res = np.array(np.ones((row, col)))
mid_mat = np.zeros((row,col))

print(res)
print(np.any(res))

print(LIVE)

result = np.array(np.zeros((row, col)))

result = result + 0.1

print(res)
print('')
print(result)

def areSame(A,B):
    row,col = np.shape(A)
    for i in range(row):
        for j in range(col):
            if A[i][j] != B[i][j]:
                return 0

    return 1     

print('BOTH are what', areSame(res, result) == 1)


       

# print(res)

# print(result)

# while not (areSame(res, result) == 1):
#     print("Hello")
#     mid_mat = LIVE
#     LIVE = LIVE @ LIVE 
#     print(LIVE)
#     res = LIVE - mid_mat
#     print('###################')
#     print(res)


# print(LIVE)
     

