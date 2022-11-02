import numpy as np
import matplotlib.pyplot as plt 

n = 1000
F = np.zeros((n,n))

omeg_power = (-2 * np.pi * np.sqrt(-1, dtype=complex) )/n 

omeg = np.power(np.e, omeg_power)

for i in range(n):
    for j in range(n):
        m = (i)*(j)
        F[i][j] = np.power(omeg, m)

print(F)        

vec = []

for i in range(n):
    vec.append(np.random.randint(1,100))

vec = np.array(vec)

print(vec)

X = F @ vec

print(X)

print(np.real(np.fft.fft(vec)))


plt.imshow(F)
# plt.imshow(X)
plt.show()

