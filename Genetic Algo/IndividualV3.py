from Main import main as m
import numpy as np


class Individual():
    
    prod_list = m.getData()
    GEN = 0

    def __init__(self, products_list= prod_list, chromosome = None, generation=0 ):
        self.__increment_gen = False if chromosome == None else True 
        self.__products_list = products_list
        self.__generation = generation
        self.__chromosome = np.zeros(len(self.__products_list)) if chromosome == None else chromosome
        _, price, space = self.__cal_total_score_and_space_sum(self.__chromosome)
        self.__total_space = space
        self.__total_price = price
        

        

    def getGeneration(self):
        return self.__generation

    def setGeneration(self, generation):
        self.__generation = generation
        # if self.__increment_gen:
        #     Individual.GEN += 1
        # self.__generation = Individual.GEN 
        # return self.__generation        
    
    def setSiblingGen(self, generation):
        self.__generation = generation

    def setTotalSpace(self, total_space):
        self.__total_space = total_space

    def setTotalPrice(self, total_price):
        self.__total_price = total_price

    def getTotalSpace(self):
        return self.__total_space

    def getTotalPrice(self):
        return self.__total_price            

    def getChromosome(self):
        return self.__chromosome    

    def initializeChromosome(self):
        random = 0
        for i in range(len(self.__chromosome)):
            random = np.random.rand()
            if random > 0.5:
                self.__chromosome[i] = 1
            else:
                self.__chromosome[i] = 0        
        return self.__chromosome        

    def __cal_total_score_and_space_sum(self, chromosome):
        total_score, space_sum = 0,0
        prod_list = self.__products_list
        for i in range(len(chromosome)):
            if chromosome[i] == 1:
                total_score += prod_list[i].getProdPrice()
                space_sum += prod_list[i].getProdSize()

        return chromosome, total_score, space_sum

    def fitness(self):
        space = 0
        while not 2.97 < space < 3.001:
            chromosome,score,space = self.__cal_total_score_and_space_sum(self.initializeChromosome())
        self.setTotalPrice(score)
        self.setTotalSpace(space)    

        return chromosome, score, space

    def __str__(self):
        return "[ Chromosme = {0} | Generation = {1} | Total_Space = {2} | Total_Price = {3}]".format(self.getChromosome(), self.getGeneration(), self.getTotalSpace(), self.getTotalPrice())

if __name__ == "__main__":
    i = Individual()

    
    i.initializeChromosome()
    print(i)
    c,n,s = i.fitness()
    print(i)
    print(c,n,s)
