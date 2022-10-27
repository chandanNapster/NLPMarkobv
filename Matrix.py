import numpy as np


# A = np.random.randn(4,5)

# print(A)

# print('\n')
# U = np.triu(A)

# print(U)

# L = np.tril(A)


# # Diag = np.diag([1,2,34,6,7,89,0])

# # print('\n')
# # print(Diag)

# C = np.concatenate((A,U,L), axis=1)

# print(C)


# A = np.round(np.random.rand(3,3) * 10)

# # SHIFTING A MATRIX
# I = np.identity(3)
# lambd = 5
# SUM = A + lambd * I
# print(SUM)

# Code Challenge Lecture 35

# M,N = 13,64
# lambd = np.round(np.random.randn()*10)

# print(lambd)
# A = np.round(np.random.randn(M,N) * 10)
# B = np.round(np.random.randn(M,N) * 10)

# SUM = lambd*(A+B)

# DIS_SUM = lambd*A + lambd*B 

# ZERO_MATRIX = SUM - DIS_SUM
# NP_ZEROS = np.zeros((M,N))
# count = 0
# for i in range(M):
#     for j in range(N):
#         if ZERO_MATRIX[i][j] != NP_ZEROS[i][j]:
#             count+=1

# if count > 0:
#     print("NOT SAME")
# else:
#     print("SAME")      
# 
             



# my_mat_t = my_mat.transpose()

# print(my_mat)
# print("TRANSPOSE using just T")
# print(my_mat.T)
# # SYMMETRIC MATRIX

# print("\n")
# print(my_mat_t * -1)

# # SKEW-SYMMETRIC

# ones = np.ones((4,4))

# ones_upper = np.triu(ones)

# print(ones_upper * -1)

M , N = 4,4

my_mat_B = np.round(np.random.randn(M,N) * 10)
my_mat_A = np.round(np.random.randn(M,N) * 10)

trace_enabled = False
if M==N:
    trace_enabled = True

def traceCal(my_mat):
    diag = []
    if M > N:
        for i in range(N):
            diag.append(my_mat[i][i])
    else:
        for i in range(M):
            diag.append(my_mat[i][i])

    diag = np.array(diag)    
    # print(diag)
    trace = 0
    if trace_enabled:
        for ele in diag:
            trace += ele
    else:
        trace = trace 
    return trace 

def sumMat(m1,m2):
    return m1+m2 



# onez = np.ones(5)

# print(onez)

# onezMat = np.diag(onez)

# print(onezMat)

# print(np.diag(my_mat))

# CODE CHALLENGE 39

# print(my_mat_A)
# print(my_mat_B)

sum_M = sumMat(my_mat_A,my_mat_B)

# print(sum_M)

if traceCal(my_mat_B) + traceCal(my_mat_A) == traceCal(sum_M):
    print("linear")

lambd = 5

if traceCal(sum_M*lambd) == lambd * traceCal(sum_M):
    print("Linear again")


