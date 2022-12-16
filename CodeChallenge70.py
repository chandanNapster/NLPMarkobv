import numpy as np 

vec = [1,2,3,4]

list1 = [[4,3,6,2],[0,4,0,1]]
list2 = [[1,2,2,2],[0,0,1,2]]



S = np.array(list1)
T = np.array(list2)


print(np.linalg.matrix_rank(S.T))
print(np.linalg.matrix_rank(T.T))

print("AFTER ADDING")

list1.append(vec)
list2.append(vec)

S = np.array(list1)
T = np.array(list2)


print(np.linalg.matrix_rank(S))
print(np.linalg.matrix_rank(T))