from Main import main as m
import numpy as np

class individual():

    def __init__(self, length):
        self.__choices = np.zeros(length)

    def getChoices(self):
        return self.__choices

    def getIndividuals(self):
        sum = 0
        list = []
        NUM_SUM = 5000
        while sum < NUM_SUM:
            index = np.random.randint(len(prod_list))
            # print(index, prod_list[index])
            sum += prod_list[index].getProdPrice()
            if sum < NUM_SUM and not (index in list):
                list.append(index)
            # else: continue    
            # sum += item.getProdPrice()
            # if sum < 30000:
            #     list.append(item)
            # else: continue    
            # print(item.getProdSize())    
        return list 
if __name__ == "__main__":
    
    prod_list = m.getData()

    i = individual(len(prod_list))
    
    my_mat = []
    # my_mat = np.array(my_mat)

    for itm in range(10):
        my_mat.append(i.getIndividuals())

    # my_mat = np.array(my_mat)
    print(my_mat)    

    
    # for i in list:
    #     print(prod_list[i])     
    # # print(i.getChoices())

    