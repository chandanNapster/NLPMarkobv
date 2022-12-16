import numpy as np

m,n = 5,6
my_mat = np.abs(np.round(np.random.randn(m,n) * 10))




def min_dist(matrix):
    row,col = np.shape(matrix)
    r, c = 0,0
    current = []
    while r < row and c < col:
        current.append([r,c])
        if r == row - 1:
            r,c = r, c + 1
        elif c == col - 1:
            r,c = r + 1, c
        elif r == row - 1 and c == col - 1:
            r,c = r,c      
        else:
            if matrix[r + 1][c] < matrix[r][c+1]: r,c = r + 1, c  
            else: r,c =  r, c + 1
    return current

print(my_mat)
print('')
# print(min_dist(my_mat))



# RECURSIVE SOLUTION

matrix = my_mat
row, col = np.shape(matrix)
cost_list = []

def get_cost_list_element_index(i,j):
    for x in range(len(cost_list)):
        if cost_list[x] == [i,j]:
            return x

def cost(i,j):
    if i >= row or j >= col: return
    
    # if [i,j] in cost_list: return [i,j] 
    
    if i == row - 1:
        cost_list.append([i,j])
        print(i,j)
        return cost(i, j + 1)
    elif j == col - 1:
        cost_list.append([i,j])
        print(i,j)
        return cost(i + 1, j)
    elif i == row - 1 and j == col - 1:
        print(i,j)
        cost_list.append([i,j])
        return         
    else:    
        if matrix[i + 1][j] < matrix[i][j + 1]:
            print(i,j)
            cost_list.append([i + 1, j])
            return cost(i + 1, j)  
        else:
            print(i,j)
            cost_list.append([i, j + 1])
            return cost(i, j + 1)


cost_list.append([0,0])

cost(0,0)
print(cost_list)


# print(my_mat) 
# print(min_dist(my_mat))
 


# def min_cost_v1(matrix):
#     row, col = np.shape(matrix)
#     print(row, col)
     
#     minCost = matrix[0][0]
#     mcList = []
#     mcList.append(minCost)
#     for i in range(row):
#         for j in range(col):
#             if i == row-1 and j == col - 1:
#                 minCost += matrix[i][j] 
#                 print("final")
#                 mcList.append(matrix[i][j])  
#             elif i == row - 1:
#                 minCost = minCost + matrix[i][j+1]
#                 print("row corner")
#                 mcList.append(matrix[i][j+1])    
#             elif j == col - 1:
#                 minCost = minCost + matrix[i+1][j]
#                 print("col corner")
#                 mcList.append(matrix[i+1][j])
#             else:

#                 minCost = minCost + min(matrix[i+1][j], matrix[i][j+1])    
#                 print("not row not col")
#                 mcList.append(min(matrix[i+1][j], matrix[i][j+1]))
#     return mcList


# def min_cost(matrix):
#     row, col = np.shape(matrix)
#     print(row, col)
#     current_row, current_col = 0,0 
#     cost = []
#     cost.append(matrix[0,0])
#      # mcList.append(minCost)
#     for i in range(row):
#         for j in range(col):
#             if i == row-1 and j == col - 1:
#                 # minCost += matrix[i][j] 
#                 # currentCell = matrix[i][j]
#                 # currentCell_row_index = i
#                 # currentCell_col_index = j 
#                 print("final")
#                 current_row = i
#                 current_col = j 
#                 cost.append(matrix[i][j])
#                 # mcList.append(matrix[i][j])  
#             elif i == row - 1:
#                 # minCost = minCost + matrix[i][j+1]
#                 print("row corner")
#                 current_row  = i
#                 current_col = j + 1
#                 cost.append(matrix[i][j+1])
#                 # mcList.append(matrix[i][j+1])    
#             elif j == col - 1:
#                 # minCost = minCost + matrix[i+1][j]
#                 print("col corner")
#                 current_row = i+1
#                 current_col = j
#                 cost.append(matrix[i+1][j])
#                 # mcList.append(matrix[i+1][j])
#             else:
#                 # minCost = minCost + min(matrix[i+1][j], matrix[i][j+1])    
#                 print("not row not col")
#                 cost.append(min(matrix[i+1][j], matrix[i][j+1]))
#                 current_row = i+1 if matrix[i+1][j] < matrix[i][j+1] else i 
#                 current_col = j if matrix[i+1][j] < matrix[i][j+1] else j+1
#                 # mcList.append(min(matrix[i+1][j], matrix[i][j+1]))
#     return cost    

# print(min_cost(my_mat))

