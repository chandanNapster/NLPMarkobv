import numpy as np

def angle_btw_vectors(vector1, vector2):
    cos_theta = dotProduct(vector1, vector2)/(length_of_Vector(vector1) * length_of_Vector(vector2))
    theta = np.rad2deg(np.arccos(cos_theta))
    return theta

def dotProduct(vector1, vector2):
    return np.dot(vector1,vector2)

def length_of_Vector(vector):
    return np.sqrt(dotProduct(vector, vector))

def unitVector(vector):
    lambd = 1/length_of_Vector(vector)
    return lambd * vector

def find_orthogonal_vector(vector):
    orthogonal_vectors = 0
    while(not(89.99999999999< orthogonal_vectors < 90.000000001)):
        ortho_vec = np.round(np.random.randn(4) * 10)
        orthogonal_vectors = angle_btw_vectors(vector,ortho_vec)
    return ortho_vec


if __name__ == '__main__':
    a = np.round(np.random.randn(4) * 10)
    b = np.round(np.random.randn(4) * 10)
    print("######--PRINT TWO VECTORS--#####")
    print(a)
    print(b)
    print("######--LENGTH TWO VECTORS--#####")        
    print(length_of_Vector(a))
    print(length_of_Vector(b))
    unit_a = unitVector(a)
    unit_b = unitVector(b)
    print("######--TWO UNIT VECTORS--#####")
    print(unit_a)
    print(unit_b)
    print("######--LENGTH OF TWO UNIT VECTORS--#####")
    print(length_of_Vector(unit_a))
    print(length_of_Vector(unit_b))
    print("######--ANGLE BETWEEN TWO VECTORS--#####")
    print(angle_btw_vectors(a,b))
    print("######--ANGLE BETWEEN TWO UNIT VECTORS--#####")
    print(angle_btw_vectors(unit_a,unit_b))
    print("FIND ORTHOGINAL VECTOR")
    print("ORTHOGINAL VECTOR TO {0} IS {1}".format(a,find_orthogonal_vector(a)))
    print(angle_btw_vectors(a,find_orthogonal_vector(a)))
    print("ORTHOGINAL VECTOR TO {0} IS {1}".format(b,find_orthogonal_vector(b)))
    print(angle_btw_vectors(b,find_orthogonal_vector(b)))
        
