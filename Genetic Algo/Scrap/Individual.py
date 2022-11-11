from Main import main as m
import numpy as np

class individuals():

    def __init__(self, length):
        self.__choices = np.zeros(length)
        self.__generation = 0

    def setChoices(self, index):
        self.__choices[index] = 1

    def getChoices(self):
        return self.__choices

    def getGeneration(self):
        return self.__generation

    def setGeneration(self):
        self.__generation = self.getGeneration() + 1        

    def getIndividual(self):
        sum = 0
        list = []
        NUM_SUM = 12000
        upper = NUM_SUM

        while sum < upper:
            index = np.random.randint(len(prod_list))
            sum += prod_list[index].getProdPrice()
            if sum < NUM_SUM and not (index in list):
                list.append(index)     
        return list 

    def fitness(self, chromosome):
        total_score, space_sum = 0,0
        for i in range(len(chromosome)):
            if chromosome[i] == 1:
                total_score += prod_list[i].getProdPrice()
                space_sum += prod_list[i].getProdSize()
        return total_score, space_sum

    def getMaxSpace(self, chromosome):
        print(chromosome)
        # sum, space = self.fitness(chromosome)
        # print(sum, space)


    def genChromosome(self, i):
    
    
    
        my_mat = []
        # my_mat = np.array(my_mat)

        for itm in range(10):
            my_mat.append(i.getIndividual())

        ind_list = []

        # my_mat = np.array(my_mat)
        for arr in my_mat:
            ind = individuals(len(prod_list))    
            for item in arr:
                # print(prod_list[item], item)
                ind.setChoices(item)
            ind_list.append(ind)

        # print("################")


        selection = np.random.randint(len(ind_list))
        print(selection)
        chromosome = []
        count = 0
        for item in ind_list:
            if count == selection:
                chromosome = item.getChoices()
            count += 1    


        return chromosome    
        # print(item.getChoices())
        # for i in list:
        #     print(prod_list[i])     
        # # print(i.getChoices())
        # sum, space = 0,0
        # count = 0
        # while space_size < 2.9:
        #     print(count)
        #     sum, space_size = i.fitness(chromosome)
        #     count += 1
        #     print(sum, space_size)
    
        # print(sum,space_size)
        # for it in range(5):
        #     i.getMaxSpace(chromosome)

        # for it in range(10):
        #     sum, space = i.fitness(chromosome)
        #     print(sum, space)
        # print(chromosome)
        
        

        # for i in range(len(chromosome)):
        #     if chromosome[i] == 1:
        #         print(prod_list[i])

if __name__ == "__main__":
    
    prod_list = m.getData()
    i = individuals(len(prod_list))
    print(i.genChromosome(i))   