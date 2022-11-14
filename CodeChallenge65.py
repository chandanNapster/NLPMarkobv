import numpy as np

M = np.round(np.random.rand(10,4) * 10)
N = np.round(np.random.rand(10,4)  * 10)



print(M)



def calculateRank(M):
    return np.linalg.matrix_rank(M)



print('')
print(N)

print('')
NT = N.T
print(NT)

# MNT = NT @ M 

# print('')
# print(MNT)
# print(" ")
# print("rank is -->", calculateRank(MNT))


print("rank is -->", calculateRank(M))
print("rank is -->", calculateRank(N.T))

print(M @ N.T)
print("rank is -->", calculateRank(M @ N.T))

def createMatrix(m,r):
    return np.round(np.random.rand(m,r) * 10)

def createMatrixOfRank(m,n,r):
    M = createMatrix(m,r)
    N = createMatrix(n,r)
    MN = M @ N.T 
    return MN 


my_mat = createMatrixOfRank(190,1000,100)

print(my_mat)
print('')
print("rank is -->", calculateRank(my_mat))

