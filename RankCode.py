import numpy as np 


M = np.round(np.random.rand(5,4) * 10)

print(M)


print("Rank ->", np.linalg.matrix_rank(M))

r,c = np.shape(M)

# print(r,c)
# print(M[r-1])
# print(M[r-2])

M[r-2] = 2*M[r-1]

print(M)
print("Rank ->", np.linalg.matrix_rank(M))

M[r-3] = M[r-2]
print(M)

print("Rank ->", np.linalg.matrix_rank(M))

noise = 0.000000000001

M = M + noise

print(M)
print("Rank ->", np.linalg.matrix_rank(M))