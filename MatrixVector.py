import numpy as np

m = 4
N = np.round(np.random.randn(m,m) * 10)


S = (N @ N.T)/10 

w = np.array([1,2,3,4])

# print(N)
# print('')
# print(N.T)
# print(S)


SL = np.tril(S)
SU = np.triu(S)

# print(SL)
# print('')
# print(SU)

SL = SL *-1

newS = SU + SL

# print(newS)
v = S@w 
v1 = w.T @ S.T 
v2 = w.T @ S 
print(v1)

print('')
print(v2)


# print(S@w)
# print('')
# print(w@S)

# print(N@w)
# print('')
# print(w@N)
print('########')

v = N@w 
v1 = w.T @ N.T 
v2 = w.T @ N 
print(v1)

print('')
print(v2)