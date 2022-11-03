import numpy as np 

A = np.round(np.random.randn(2,3) * 10)
B = np.round(np.random.randn(5,4) * 10)

# print(A)
# print('')
# print(B)

# FRIBUNUOUS DOT PRODUCT
# ELEMENT WISE MULTIPLICATION ALL THE MATRICES
# THEN ADD ALL ELEMENTS IN THE RESULTANT MATRIX

# mu = np.multiply(A,B)

# sum = 0
# for i in range(5):
#     for j in range(4):
#         sum += mu[i][j]

# print(sum)

# print(np.sum(np.multiply(A,B)))

# print(A @ B.T)

# norm(A) = trace(np.sqrt(np.dot(A.T,A)))
# length(A) = np.sqrt(np.dot(A,A))

# CONVERT MATRIX INTO A VECTOR
# COLUMN WISE CONCATENATION

def mat2Vec(matrix):
    row, col = np.shape(matrix)
    arr = []
    for i in range(col):
        arr.append(matrix[:,i])
    arr = np.array(arr).flatten()    
    return arr 

def trace_of_mat(matrix):
    trace = 0
    row, col = np.shape(matrix)
    for i in range(row):
        for j in range(col):
            if i == j:
                trace += matrix[i][j]
    return trace

def norm_of_Mat(matrix):
    return np.sqrt(trace_of_mat(matrix.T @ matrix))

def length_of_vec(vector):
    return np.sqrt(np.dot(vector,vector))

if __name__ == '__main__':
    arr1 = mat2Vec(A) 
    print(norm_of_Mat(A))
    print(length_of_vec(arr1))

