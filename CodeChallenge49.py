import numpy as np
import matplotlib.pyplot as plt
 
theta = np.linspace( 0 , 2 * np.pi , 2 )

# print(theta)
radius = 0.4
x,y = np.array(radius * np.cos( theta )), np.array(radius * np.sin( theta ))
 
figure, axes = plt.subplots( 1 )
 
axes.plot( x, y )
axes.set_aspect( 1 )

i_mat = np.identity(2)

new_x, new_y = x* i_mat, y * i_mat

axes.plot( new_x, new_y )
axes.set_aspect( 1 )

# print(x,y)
 
plt.title( 'Parametric Equation Circle' )
plt.show()