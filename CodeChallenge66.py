import numpy as np

m,n,r = 4,6,4
lambd = 1

F = np.round(np.random.rand(m,n) * 10)

def reducedRankMatrix(m,n,r):
    MR = np.round(np.random.rand(m,r) * 5)
    NR = np.round(np.random.rand(r,n) * 5)
    Redu = MR @ NR 
    return Redu

R = reducedRankMatrix(m,n,r)
print(F)
print('')
print("Rank of F -->", np.linalg.matrix_rank(F))
print('******************************')
print(R)
print('')
print("Rank of R -->", np.linalg.matrix_rank(R))
print(lambd * F)
print('')
print("Rank of lambda * F -->", np.linalg.matrix_rank(lambd * F))
print('******************************')
print(lambd * R)
print('')
print("Rank of lambda * R -->", np.linalg.matrix_rank(lambd * R))
print("#######################################")

print(lambd * np.linalg.matrix_rank(F), '\n', np.linalg.matrix_rank(lambd * F))


# RANK OF A MATRIX, ITS TRANSPOSE, MATRIX @ ITS TRANSPOSE and ITS TRANSPOSE @ MATRIX ARE ALL THE SAME


def rank_of_matrix(M):
    return np.linalg.matrix_rank(M)

def rank_of_2_matrix(M,N):
    minList = []
    m,n = rank_of_matrix(M), rank_of_matrix(N)
    minList.append(m)
    minList.append(n)
    return np.min(minList)

print("Rank of F",rank_of_matrix(F))
print("****************")
FT = F.T
print("Rank of F.T",rank_of_matrix(FT))
print("****************")

print("Rank of F and FT",rank_of_2_matrix(F, FT))
print("****************")

print("Rank of FT and F",rank_of_2_matrix(FT, F))
print("****************")
