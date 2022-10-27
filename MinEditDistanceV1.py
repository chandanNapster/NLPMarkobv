import numpy as np

class MED:

    def __init__(self):
        self.__SOURCE_WORD = " "+"play"
        self.__TARGET_WORD = " "+ "stay"
        self.__src_dict = dict([ (data, index) for index, data in enumerate(self.__SOURCE_WORD)])
        self.__trg_dict = dict([ (data, index) for index, data in enumerate(self.__TARGET_WORD)])
        self.__my_mat = np.zeros((len(self.__SOURCE_WORD), len(self.__TARGET_WORD)))

    def get_source_dict(self):
        return self.__src_dict

    def set_source_dict(self, new_list):
        self.__src_dict = dict(new_list)     

    def set_source_word(self, word):
        self.__SOURCE_WORD = word 

    def set_target_word(self, word):
        self.__TARGET_WORD = word       

    def get_target_dict(self):
        return self.__trg_dict

    def get_src_word(self):
        return self.__SOURCE_WORD

    def get_trg_wprd(self):
        return self.__TARGET_WORD            

    def delete(self, letter, first_delete):
        word = list(self.get_src_word())
        dict = self.get_source_dict()
        index = dict[letter]
        if letter in word and first_delete:
            word[index] = "#"
            dict['#'] = dict[letter]
            del dict[letter]

        elif letter in word and not first_delete:
            word[dict[letter]] = word[-1]
            word = word[:-1]
            new_list = [(data, index)for index, data in enumerate(word)]
            self.set_source_dict(new_list)        
        word = ''.join(word)
        self.set_source_word(word)    
           

    def insert(self, letter):
        word = list(self.get_src_word())
        dict = self.get_source_dict()
        if "#" in word:
            word[dict['#']] = letter
            dict[letter] = dict['#']
            del dict['#']
        elif "#" not in word:
            word += letter 
            dict[letter] = len(self.get_src_word())   
        word = ''.join(word)
        self.set_source_word(word)

    def replace(self, original_letter, new_letter, first_delete):
        if first_delete:
            self.delete(original_letter,first_delete)
            self.insert(new_letter)   
        else:
            self.insert(new_letter)
            self.delete(original_letter,first_delete)    

    def get_my_matrix(self):
        return self.__my_mat

if __name__ == "__main__":
    m = MED()
    print(m.get_src_word())
    m.replace('l','a', False)
    print(m.get_src_word())
    print(m.get_source_dict())
    # m.replace('p', 's')
    # m.replace('l','t')
    # print(m.get_src_word())
       