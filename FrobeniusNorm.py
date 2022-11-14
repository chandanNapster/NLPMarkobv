import numpy as np

# FROBINIUS DOT PRODUCT

def frob_v1(M):
    M = M * M
    M = np.array(M) 
    return M 
    print(M)

def frob_v2(M):
    M = np.array(M)
    M = M.T @ M
    r,c = np.shape(M)
    sum = 0
    for i in range(r):
        sum += M[i][i]
    print(sum)    

M = np.round(np.random.randn(5,4) * 10)


MM = frob_v1(M)

r,c = np.shape(MM)

sum = 0
for i in range(r):
    for j in range(c):
        sum += MM[i][j]


print(sum)

frob_v2(M)
