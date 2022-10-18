import re
import numpy as np


file = ['D:\OneDrive - BENNETT UNIVERSITY\BU\Reserach\Python Dev Work\PythonDataAnalysisWithPandasNumpySeabourn\Gita1.txt']

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


for i in range(len(tokens) - 1):
    rw, cl = state_dict[tokens[i]], state_dict[tokens[i+1]]
    my_matrix[rw][cl] += 1


sum_of_all_prob = 0
for i in range(row):
    for j in range(col):
        sum_of_all_prob += my_matrix[i][j]

for i in range(row):
    for j in range(col):
        my_matrix[i][j] = my_matrix[i][j]/sum_of_all_prob


# for i in range(row):
#     for j in range(col):
#         if my_matrix[i][j] > 0:
#             print(distinct_tokens[i], distinct_tokens[j], my_matrix[i][j])

print(my_matrix)
