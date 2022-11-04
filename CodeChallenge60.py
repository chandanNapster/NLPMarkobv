import numpy as np 

m,n = 5,5
A = np.round(np.random.randn(m,n) * 10)

SM = A @ A.T 

SML = np.tril(SM)
SMU = np.triu(SM)
SMU = SMU * -1

SkM = SML + SMU 

# print(SM)
# print('')
# print(SkM)

def create_a_skew_symmetric_matrix(matrix):
    SM = matrix
    SML = np.tril(SM)
    SMU = np.triu(SM)
    SMU = SMU * -1
    SkM = SML + SMU
    return SkM  

def mat_asym_index(matrix):
    return norm(til(matrix)) / norm(matrix)

def mat_sym_index(matrix):
    return 1-mat_asym_index(matrix)

def til(matrix):
    return (matrix - matrix.T)/2

def norm(matrix):
    return np.sqrt(trace(matrix))

def trace(matrix):
    matrix = matrix @ matrix.T
    trace = 0
    row,col = np.shape(matrix)
    for i in range(row):
        for j in range(col):
            if i == j:
                trace += matrix[i][j]
    return trace 

def create_X_percent_symmetric_matrix(percent):
    percent = percent/100
    lower = percent - 0.01
    upper = percent + 0.01
    mat = np.round(np.random.randn(m,n) * 10)
    sym = mat_sym_index(mat)
    while not (lower < sym < upper):
        mat = np.round(np.random.randn(m,n) * 10)
        sym = mat_sym_index(mat)
        print('The sym is',sym)
    return mat 

def create_X_percent_symmetric_matrix_v2(percent, M):
    percent = percent/100
    return percent*(M + M.T) + (1 - percent)*(M - M.T)

if __name__ == '__main__':
    # print(A)
    # print(mat_asym_index(SM))
    # print(mat_asym_index(SkM))
    # print(mat_sym_index(SkM))

    # print(mat_asym_index(A))
    # print(mat_asym_index(A @ A))    
    # print(mat_asym_index(A @ A @ A))  
    mat = create_X_percent_symmetric_matrix(80)
    # sk_mat = create_a_skew_symmetric_matrix(mat)
    # print(mat)
    # print(sk_mat)
    # print(mat_sym_index(mat))
    # print(1- mat_sym_index(sk_mat))

    # new_mat = mat + sk_mat
    # print(mat_sym_index(new_mat))
    print('######################')
    print(mat)
    print(mat_sym_index(mat))
    print('######################')

    new_mat_v2 = create_X_percent_symmetric_matrix_v2(80, mat)

    print(new_mat_v2)

    print(mat_sym_index(new_mat_v2))
    print('######################')