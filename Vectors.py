from tkinter import PROJECTING
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


v1 = [3,-2]
v2 = [3,7]

# PLOT 2D vector
# plt.plot([0,v2[0]], [0,v2[1]])
# plt.show()

# PLOT 3d VECTOR

# fig = plt.figure(figsize=plt.figaspect(1))
# ax = fig.gca()
# ax.plot([0,v2[0]], [0,v2[1]], [0,v2[2]], linewidth = 3)
# plt.show()

v1 = np.array(v1)
v2 = np.array(v2)
v3 = v1 + v2

# plt.plot([0,v1[0]], [0,v1[1]], 'b', label='v1')
# plt.plot([0,v2[0]] + v1[0], [0,v2[1]] + v1[1], 'r', label='v2')
# plt.plot([0,v3[0]], [0, v3[1]], 'k', label='v1 + v2')
# plt.show()

# lambd = -2.3

# v1m = v1*lambd  

# plt.plot([0,v1[0]], [0,v1[1]], 'b', label='v1')
# plt.plot([0,v1m[0]], [0,v1m[1]], 'r', label='v2')


# plt.axis('on')
# axlim = max([abs(max(v1)), abs(max(v1m))]) * 1.5
# plt.axis((-axlim,axlim,-axlim,axlim))
# plt.grid()
# plt.show()

# method 1
# dp1 = sum(np.multiply(v1,v2))

# # method 2
# dp2 = np.dot(v1,v2)

# # method 3
# dp3 = np.matmul(v1,v2)



# print(dp1)
# print(dp2)
# print(dp3)

# # method 4
# dp4 = 0

# for i in range(len(v1)):
#     dp4 += v1[i] * v2[i]

# print(dp4)    


# DISTRIBUTIVE OF DOT PRODUCT

# res1 = np.dot(v1, v2+v3)

# res2 = np.dot(v1,v2) + np.dot(v1,v3)

# print(res1, res2) 


# ASSOCIATIVITY

res1 = np.dot(v1, np.dot(v2,v3))
res2 = np.dot(np.dot(v1,v2), v3)

print(res1, res2) 