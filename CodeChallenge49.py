import numpy as np
import matplotlib.pyplot as plt
 
theta = np.linspace( 0 , 2 * np.pi , 100 )

# print(theta)
radius = 0.4
x,y = np.array(radius * np.cos( theta )), np.array(radius * np.sin( theta ))

# nx,ny = np.array(radius * np.cos( theta )), np.array(radius * np.sin( theta ))

# circle_mat = np.array([x,y])
circle_mat = np.vstack((np.array(radius * np.cos( theta )), np.array(radius * np.sin( theta ))))
# rotation_mat = np.identity(2) *2
multi_factor = 4
angle = 30
deg = np.deg2rad(angle)
thetha = deg
rot_mat = np.array([[(multi_factor*np.cos(thetha)), -np.sin(thetha)],[np.sin(thetha),  np.cos(thetha)]])

new_circle_mat = rot_mat @ circle_mat
row, col = np.shape(new_circle_mat)

print(row, col)

nx,ny = new_circle_mat[0], new_circle_mat[1]

# print(np.shape(circle_mat))


figure, axes = plt.subplots( 1 )
axes.plot( x, y )
axes.plot( nx, ny )
axes.set_aspect( 1 ) 
plt.title( 'Parametric Equation Circle' )
plt.show()