import re
import numpy as np


file = ['D:\OneDrive - BENNETT UNIVERSITY\BU\Reserach\Python Dev Work\PythonDataAnalysisWithPandasNumpySeabourn\Gita1.txt']

epsilon = 10

text = ""
for fl in file:
    with open(fl, "r",encoding="utf8") as txt:
        text = txt.read()


text = re.sub("[^A-z`\n' ]+", "", text).lower()

tokens = text.split()
distinct_tokens = list(set(tokens))
state_dict = dict([(data, index) for index, data in enumerate(distinct_tokens)])
row, col = len(distinct_tokens), len(distinct_tokens)
my_matrix = np.zeros((row, col))

k = 3
for i in range(len(tokens) - k + 1):
    rw, cl = state_dict[tokens[i]], state_dict[tokens[i+1]]
    my_matrix[rw][cl] += 1


# SMOOTHING
for i in range(row):
    for j in range(col):
        my_matrix[i][j] += epsilon


# CALCULATING THE TRANSITION PROBABILITIES
row_sum = []
for i in range(row):
    sum_val = 0
    for val in my_matrix[i]:
        sum_val += val
    my_matrix[i] = my_matrix[i]/sum_val


matrix = my_matrix
next_matrix = np.dot(matrix,matrix)


print(np.array_equal(next_matrix, matrix))

while(not(np.array_equal(next_matrix, matrix))):
    print("Hello")
    matrix = next_matrix
    next_matrix = np.dot(matrix, next_matrix)


print(next_matrix)
# print('initial')
# print(my_matrix)

# new_mat = np.dot(my_matrix,my_matrix)
# print('1')
# print(new_mat)

# new_mat = np.dot(new_mat, my_matrix)
# print('2')
# print(new_mat)

# new_mat = np.dot(new_mat, my_matrix)
# print('3')
# print(new_mat)

# new_mat = np.dot(new_mat, my_matrix)
# print('4')
# print(new_mat)

# new_mat = np.dot(new_mat, my_matrix)
# print('5')
# print(new_mat)

# new_mat = np.dot(new_mat, my_matrix)
# print('6')
# print(new_mat)

# print(np.array_equal(new_mat, my_matrix))


# sum_of_all_prob = 0
# for i in range(row):
#     for j in range(col):
#         sum_of_all_prob += my_matrix[i][j]

# for i in range(row):
#     for j in range(col):
#         my_matrix[i][j] = my_matrix[i][j]/sum_of_all_prob


# for i in range(row):
#     for j in range(col):
#         if my_matrix[i][j] > 0:
#             print(distinct_tokens[i], distinct_tokens[j], my_matrix[i][j])

# print(my_matrix)
