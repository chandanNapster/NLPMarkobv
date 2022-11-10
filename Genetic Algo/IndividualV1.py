from Main import main as m
import numpy as np


class Individual():
    

    def __init__(self, products_list, generation=0):
        self.__products_list = products_list
        self.__generation = generation
        self.__chromosome = np.zeros(len(self.__products_list))
        self.__num_sum = 0

    def setChromosomeV2(self,child):
        self.__chromosome = child

    def setChromosome(self, index):
        self.__chromosome[index] = 1

    def getGeneration(self):
        return self.__generation

    def setGeneration(self):
        self.__generation = self.getGeneration() + 1 

    def getProdList(self):
        return self.__products_list  

    def profit_max(self):
        self.__num_sum = 0
        p_list = self.getProdList()
        for prd in p_list:
            self.__num_sum += prd.getProdPrice()  
        return self.__num_sum          

    def getProductsComb(self):
        sum = 0
        list = []
        upper = self.profit_max()
        prod_list = self.getProdList()

        while sum < upper:
            index = np.random.randint(len(prod_list))
            sum += prod_list[index].getProdPrice()
            if sum < upper and not (index in list):
                list.append(index)     
        return list 

    def getChromosome(self):
        prodComb = self.getProductsComb()
        for index in prodComb:
            self.setChromosome(index)
        return self.__chromosome
                

# if __name__ == "__main__":
    


