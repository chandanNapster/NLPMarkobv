import numpy as np 

word_1 = "Play"
word_2 = "stay"

word_1 = word_1.lower()
word_2 = word_2.lower()


word_1 = " " + word_1
word_2 = " " + word_2

dict_word_1 = dict([(data, index) for index, data in enumerate(word_1)])
dict_word_2 = dict([(data, index) for index, data in enumerate(word_2)])


# print(dict_word_1)
# print(dict_word_2)


row, col = len(word_1), len(word_2)
my_matrix = np.zeros((row, col))

rw = dict_word_1['p']
co = dict_word_2[' ']


# def insert(word, original_letter ,replace_letter, dict):
#     word = list(word)
#     index = dict[original_letter]
#     dict[replace_letter] = dict[original_letter]
#     del dict[original_letter]
#     if index < len(word): word[index] = replace_letter
#     return ''.join(word)

# def delete(word, original_letter , dict):
#     word = list(word)
#     index = dict[original_letter]
#     if index < len(word) and original_letter in word: word[index] = " "
#     del dict[original_letter]
#     return ''.join(word)
    
# def replace(word, original_letter, replace_letter, dict):
#     return ''.join(insert(delete(word, original_letter, dict), original_letter, replace_letter, dict))
    
# print(word_1)

# word_1 = insert(word_1, 'y', 'x', dict=dict_word_1)

# print(word_1)

# word_1 = delete(word_1, 'x', dict = dict_word_1)

# print(word_1)


# word_1 = replace(word_1, 'y', 'z', dict_word_1)

# print(word_1)



# dict_word_1['r'] = dict_word_1['p']
# del dict_word_1['p']

# print(dict_word_1)


# def insert(word, letter,index, dict):
#     word = list(word)
#     if word[index] == " ": word[index] = letter
#     return ''.join(word)


# print(insert(word_1, 'a', dict_word_1))    


print(word_1)
# print(dict_word_1)

def delete(word, letter, dict):
    word = list(word)
    index = dict[letter]
    if letter in word and index < len(word): 
        word[index] = " "
        del dict[letter]

    return ''.join(word)     

def insert(word, letter, dict):
    word = list(word)
    index = dict[' ']

# print(delete(delete(word_1, 'a', dict_word_1), 'p', dict_word_1))
