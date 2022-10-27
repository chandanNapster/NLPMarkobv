import numpy as np


factor = 20
vec1 = np.round(np.random.rand(1,4) * factor)
vec1 = vec1.flatten()

vec2 = np.round(np.random.rand(1,4) * factor)
vec2 = vec2.flatten()

def length_of_vector(vector):
    return np.abs(np.sqrt(np.dot(vector,vector)))

def dot_product(vector1, vector2):
    return np.abs(np.dot(vector1,vector2))    

def unit_vector(vector):
    length = length_of_vector(vector)
    vector = vector*(1/length)
    return vector

def angle_between_vectors(vector1, vector2):
    thetha = np.rad2deg(np.arccos(
                                    np.dot(vector1,vector2)    /
                                    (length_of_vector(vector1) * length_of_vector(vector2))
                                 )
                       )    
    return thetha                  

length_of_vector_1 = length_of_vector(vec1)
length_of_vector_2 = length_of_vector(vec2)
mag_of_dot_product = dot_product(vec1, vec2)

print(length_of_vector_1, length_of_vector_2)
print(mag_of_dot_product)

# CALCULATE THE UNIT VECTOR
print("UNIT VECTOR CALCULATION")
norm_vector_1 = unit_vector(vec1)
print(norm_vector_1) 

norm_vector_2 = unit_vector(vec2)
print(norm_vector_2)

length_of_vector_1 = length_of_vector(norm_vector_1)
length_of_vector_2 = length_of_vector(norm_vector_2)
mag_of_dot_product = dot_product(norm_vector_1, norm_vector_2)

print(length_of_vector_1, length_of_vector_2)
print(mag_of_dot_product)

print(np.cos(np.deg2rad(angle_between_vectors(norm_vector_1,norm_vector_2))))
