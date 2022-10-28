import numpy as np

Common = np.random.randint(2,7)
Outer1 = np.random.randint(2,7)
Outer2 = np.random.randint(2,7)

print(Common, Outer1, Outer2)

A = np.round(np.random.randn(Outer1,Common) * 10)
B = np.round(np.random.randn(Common,Outer2) * 10)

print(A)
print('')
print(B)

row = []
col = []
for i in range(Common):
    row.append(A[:,i])
    col.append(B[i])

row = np.array(row)
col = np.array(col)

row_flat = row.flatten()
col_flat = col.flatten()

row_count = 0
row_rank = 1
row_list = []

for rv in row_flat:
    if row_count == Outer1:
        row_rank += 1
        row_count = 0
        row_list.append((rv, row_count, row_rank))
        
    else:
        row_list.append((rv, row_count, row_rank))
          
    row_count += 1

col_count = 0
col_rank = 1
col_list = []

for cv in col_flat:
    if col_count == Outer2:
        col_count = 0
        col_rank += 1
        col_list.append((cv, col_count, col_rank))
        
    else:
        col_list.append((cv, col_count, col_rank))    
    col_count += 1    

rank_list = []

INDEX = 1
RANK = 2
VALUE = 0

def cal_num_of_rank_mat(rank):
    C = np.zeros((Outer1,Outer2))
    for rw in row_list:
        for cl in col_list:
            if rw[RANK] == rank and cl[RANK]== rank:
                C[rw[INDEX], cl[INDEX]] = rw[VALUE] * cl[VALUE]           
    rank_list.append(C)


for i in range(1,row_rank+1):
    cal_num_of_rank_mat(i)

Mat_Sum = np.zeros((Outer1,Outer2))

for item in rank_list:
    Mat_Sum += item 

print('')
print(Mat_Sum)
print('')
print(np.matmul(A,B))