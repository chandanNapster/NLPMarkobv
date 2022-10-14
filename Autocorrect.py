import dis
import re


file = ['D:\OneDrive - BENNETT UNIVERSITY\BU\Reserach\Python Dev Work\PythonDataAnalysisWithPandasNumpySeabourn\Gita1.txt']

# file = ['D:\NLPMarkov\NLPMarkobv\Gita1.txt']

text = ""
for fl in file:
    with open(fl, "r",encoding="utf8") as txt:
        text = txt.read()


text = re.sub("[^A-z,`\n' ]+", "", text)
# THIS IS NEEDED FOR TOKENIZING THE PUNCUTATIONS THE \1 is called as the capture syntax and () are put on the re. 
# r is put in front of \1 so that it is interpreted as a raw string
text = re.sub("([.,!?])", r" \1 ", text)
text = text.lower()
tokens = text.split()
distinct_tokens = list(set(tokens))
token_count_dict  = dict([(data, 0) for index, data in enumerate(distinct_tokens)]) 

# print(token_count_dict)



for key1 in tokens:
    for key2 in distinct_tokens:
        if key1 == key2 : 
            token_count_dict[key2] += 1

# print(text)
# print(token_count_dict)     
total_count_of_words = 0

for key in distinct_tokens:
    print(key,token_count_dict[key])
    total_count_of_words += token_count_dict[key] 

for key in distinct_tokens:
    token_count_dict[key] = token_count_dict[key]/total_count_of_words

print(total_count_of_words)
print(token_count_dict)