import numpy as np

class MEDV2:

    del_cost = 1
    inrt_cost = 1
    rep_cost = 2

    def __init__(self, src, trg):
        self.__SOURCE_WORD = " "+src
        self.__TARGET_WORD = " "+ trg
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

    def get_my_matrix(self):
        return self.build_my_mat(self.__my_mat)

    def delete(self, letter):
        self.get_my_matrix    

    def build_my_mat(self, my_mat=get_my_matrix):
        source = list(self.__SOURCE_WORD)
        target = list(self.__TARGET_WORD)

        my_mat[0] = [k for k in range(len(target))] 
        my_mat[:, 0] = [k for k in range(len(source))]

        for i in range(1,len(source)):
            for j in range(1, len(target)):
                if source[i] != target[j]:
                    my_mat[i][j] = min(my_mat[i-1][j], my_mat[i][j-1]) + 1
                else:
                    my_mat[i][j] = my_mat[i-1][j-1]    

        self.__my_mat = my_mat
        return self.__my_mat   



if __name__ == "__main__":
    source = "sitting"
    target = "kitten"
    m = MEDV2(source,target)
    print(m.get_my_matrix())
    