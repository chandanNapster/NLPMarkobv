import numpy as np 
import re

# SMOOTHING FACTOR
smooth_by = 1
file = ['D:\\NLPMarkov\\NLPMarkobv\\Gita1.txt']

text = ""
for fl in file:
    with open(fl, 'r', encoding="utf-8") as txt:
        text += txt.readline()

text = re.sub("[^A-z`\n' ]+", "", text).lower()
tokens = text.split()
states = list(set(tokens))
rows, cols = len(states), len(states)
state_matrix = np.zeros((rows, cols))

state_index_list = [(data, index) for (index, data) in enumerate(states)]
state_dict = dict(state_index_list)

for i in range(len(tokens) - 1):
    row = state_dict[tokens[i]]
    col = state_dict[tokens[i+1]]
    state_matrix[row][col] += 1

# SMOOTHING
state_matrix = state_matrix + smooth_by

# CALCULATING PROBABILITIES
for i in range(rows):
    sum = np.sum(state_matrix[i])
    state_matrix[i] = state_matrix[i]/sum



def marMul(matrix, rng):
    for i in range(rng):
        matrix = np.multiply(matrix,matrix)
    return matrix


# print(marMul(state_matrix, 52))

var = marMul(state_matrix, 3)

print(var)
print(np.sum(var[0]))






