import numpy as np
import math 


# row = 4
# col = 6
# my_mat_1 = np.random.randint(1,10,(row,col))
# my_mat_2 = np.random.randint(1,10,(row,col))

# print(my_mat_1)
# print(my_mat_2)

# print("#############")
# dp1 = np.zeros(col)
# for i in range(col):
#     print(my_mat_1[:,i] * my_mat_2[:,i])
#     dp1[i] = np.dot(my_mat_1[:,i], my_mat_2[:,i])

# print(dp1)    

# print(my_mat_1, my_mat_2)

# for i in range(2):
#     for j in range(2):
#         # print(my_mat_1[i][j], '--->', my_mat_2[i][j], 'The dot product',  my_mat_1[i][j]*my_mat_2[i][j])
#         print(my_mat_1[1], my_mat_2[1])

# lent = 5

# vec1 = [16,-2,4]
# vec2 = [.5,2,-1]
# vec2T = np.transpose(np.random.randn(1,10))
# vec1T = np.transpose(np.random.randn(1,10))


# res1 = np.dot(vec1, vec2)
# res2 = np.dot(vec2, vec1)
# print(res1)
# res2 = np.dot(vec2, vec1)

# sum = 0
# for i in range(lent):
#     sum += vec1[i] * vec2[i]


# print(res1, sum)


# ANGLE BETWEEN TWO VECTORS

# length_of_vec1 = np.sqrt(np.dot(vec1,vec1))
# length_of_vec2 = np.sqrt(np.dot(vec2,vec2))

# tetha = np.arccos((np.dot(vec1,vec2)) / (length_of_vec1*length_of_vec2))

# angle = math.radians(90)
# print(angle)

# print(math.cos(angle))




# a = [1,-2]
# b = [2,3]
# c = [0,2]

# # a.b = a.b.cos(thetha)

# length_of_a = np.sqrt(np.dot(a,a))
# length_of_b = np.sqrt(np.dot(b,b))
# length_of_c = np.sqrt(np.dot(c,c))

# theta = np.arccos(np.dot(a,b)/(length_of_a * length_of_b))

# print(math.degrees(theta))

# print(np.rad2deg(theta))



# SIGN OF THE DOT PRODUCT IS INVARIANT TO THE SCALE OF THE VECTOR


# CALCULATE DOT PRODUCT OF A VECTOR

def dotProduct(v1, v2):
    return np.dot(v1,v2)

# CALCULATE LENGTH OF A VECTOR
def length_of_vector(v):
    return np.sqrt(np.dot(v,v))

def vectorAngle(v1,v2):
    return np.rad2deg(np.arccos(dotProduct(v1,v2)/(length_of_vector(v1)* length_of_vector(v2))))

# GENERATE VECTORS
v1 = np.random.randn(3)
v2 = np.random.randn(3)

# GENERATE SCALARS 
s1 = np.random.randint(1,10)
s2 = np.random.randint(1,10)

print(s1,s2)
print(v1,v2)
print(length_of_vector(v1), length_of_vector(v2))
print(v1*s1, v2*s2)

print(dotProduct(v1,v2))
print(dotProduct(v1*s1, v2*s2))

print(f'{vectorAngle(v1,v2): 4f}')
print(f'{vectorAngle(v1*s1,v2*s2): 4f}')

op1 = np.outer(v1,v2)
print(op1)

# terrible programming but helps conceptually
op = np.zeros((len(v1), len(v2)))

for i in range(len(v1)):
    for j in range(len(v2)):
        op[i][j] = v1[i] * v2[j]


# FINDING THE UNIT VECTOR

print(v1)

unit_vector = v1*(1/length_of_vector(v1))

print("THE UNIT VECTOR IS")
print(unit_vector)

print(length_of_vector(unit_vector))

def findUnitVector(vector):
    return vector*(1/length_of_vector(vector))


vector1 = np.random.rand(4) * 10
vector2 = np.random.rand(4) * 10

print(length_of_vector(vector1))
print(length_of_vector(vector2))

print("The dot product is -->",np.abs(
                                    dotProduct(
                                        vector1,
                                        vector2)))

vector1 = findUnitVector(vector1)
vector2 = findUnitVector(vector2)

print(vector1)
print(vector2)

print(
    length_of_vector(
        vector1))
print(
    length_of_vector(
        vector2))

print(dotProduct(
    vector1,
    vector2))



