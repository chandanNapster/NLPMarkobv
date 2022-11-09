from Main import main as m
import numpy as np

class individual():

    def __init__(self, length):
        self.__choices = np.zeros(length)

    def getChoices(self):
        return self.__choices

if __name__ == "__main__":
    
    prod_list = m.getData()

    i = individual(len(prod_list))
    sum = 0
    list = []
    while sum < 20000:
        index = np.random.randint(len(prod_list))
        # print(index, prod_list[index])
        sum += prod_list[index].getProdPrice()
        if sum < 20000 and not (index in list):
            list.append(index)
        else: continue    
        # sum += item.getProdPrice()
        # if sum < 30000:
        #     list.append(item)
        # else: continue    
        # print(item.getProdSize())

    for i in list:
        print(i)     
    # print(i.getChoices())

    