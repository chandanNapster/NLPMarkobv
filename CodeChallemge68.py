import numpy as np

m,n = 10,6

A = np.round(np.random.rand(m,n) * 10)
B = np.round(np.random.rand(m,n) * 10)
AT = A.T
BT = B.T
C = A @ AT
D = B @ BT 

def cal_rank(matrix):
    return np.linalg.matrix_rank(matrix)

print(A)
print('')
print(B)
print('')
print(C)
print('')
print(D)
print('RANK OF A')
print(cal_rank(A))
print('RANK OF B')
print(cal_rank(B))
print('RANK OF AT')
print(cal_rank(AT))
print('RANK OF BT')
print(cal_rank(BT))
print('RANK OF C')
print(cal_rank(C))
print('RANK OF D')
print(cal_rank(D))

print("Rank of SumAB")
SumAB = A + B
print(cal_rank(SumAB))

def cal_two_mat_sum_rank(A,B):
    return cal_rank(A) + cal_rank(B)
print("Rank A + B")
print(cal_two_mat_sum_rank(A,B))

print("RANK C AND D")
print(cal_rank(C + D))

print("C + D")
print(C + D)

if m == n:
    print("Rank of A + AT")
    print(cal_rank(A+AT))
    print("Rank of B + BT")
    print(cal_rank(B+BT))