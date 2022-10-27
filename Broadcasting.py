import numpy as np

my_list = np.arange(1,17)
my_mat  = np.reshape(my_list, (4,4), 'C')

print(my_mat) 

vec_1 = np.arange(1,5)
print(vec_1)

# CONVERT A ROW VECTOR TO COLUMN VECTOR

vec_1 = np.reshape(vec_1, (len(vec_1), 1))

print(my_mat + vec_1)