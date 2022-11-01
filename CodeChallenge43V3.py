import numpy as np

Outer1 = 4
Common = 3
Outer2 = 5

A = np.round(np.random.randn(Outer1,Common) * 10)
B = np.round(np.random.randn(Common,Outer2) * 10)
C = np.zeros((Outer1, Outer2))

print(A)
print('')
print(B)
print('')
print(C)

row = []
col = []


for i in range(Common):
    row.append(A[:,i])
    col.append(B[0])

row = np.array(row).flatten()
col = np.array(col).flatten()

print(row)
print('')
print(col)

row_rank = []

count = 0

for item in row:
    if count < Outer1:
        row_rank.append((item, count))
        count += 1   
         
    else:
        # print("###########")
        count = 0
        row_rank.append((item, count))
        count += 1  

print('')
print(row_rank)

col_rank = []

count = 0

for item in col:
    if count < Outer2:
        col_rank.append((item, count))
        count += 1   
         
    else:
        # print("###########")
        count = 0
        col_rank.append((item, count))
        count += 1  

print('')
print(col_rank)


pair_list = []
for rw in row_rank:
    for cl in col_rank:
        if rw[1] == cl[1]:
            pair_list.append((rw[0], cl[0], rw[1], cl[1]))


print('')

print(set(pair_list))