from Fitness import Fitness
from IndividualV1 import Individual
import numpy as np

class GeneticFunc():

    def __init__(self):
        self.__crossover = 0

    def crossOver(self, parent1, parent2):
        cutoff = self.getcutoff(parent1, parent2)
    
        parent_1_part_1 = parent1[:cutoff]
        parent_1_part_2 = parent1[cutoff:]
        parent_2_part_1 = parent2[:cutoff]
        parent_2_part_2 = parent2[cutoff:]

        child1 = self.createChild(parent_1_part_1, parent_2_part_2)
        child2 = self.createChild(parent_2_part_1, parent_1_part_2)

        return child1, child2 

    def createChild(self,list1, list2):
        list1 = list(list1)
        list2 = list(list2)

        list1 = self.convert2int(list1)
        list2 = self.convert2int(list2)

        for i in range(len(list2)):
            list1.append(list2[i])
        return list1

    def convert2int(self,lista):
        listint = []
        for i in range(len(lista)):
            listint.append(int(lista[i]))
        return listint

    def getcutoff(self,parent1, parent2):
        parent1 = list(parent1)
        parent2 = list(parent2)
        if len(parent1) == len(parent2):
            max_length = len(parent1)
            cutoff = np.random.randint(max_length)
        return cutoff

    def mutation(self, chromosome, rate):
        index = 0
        for gene in chromosome:
            rndm = np.random.rand()
            if rate > rndm:
                if gene == 1:
                    chromosome[index] = 0
                else:
                    chromosome[index] = 1    
            index += 1
        return chromosome


# if __name__ == "__main__":
#     c = Crossover()

#     sum_1 = 0
#     sum_2 = 0
#     while not (2.9 < sum_1 < 3) and not (2.9 < sum_2 < 3):
#         child1, child2 = c.getChild()
#         sum_1 = c.bestChromosomeChild(child1)
#         sum_2 = c.bestChromosomeChild(child2)
    
#     # print(child1)

#     # print(c.bestChromosomeChild(child1))
#     # print(c.bestChromosomeChild(child2))
#     print(child1)
#     mutated_child1 = c.mutation(child1, 0.03)
#     print(mutated_child1)

    # for i in range(100):
    #     print(np.random.rand())
    
    # print(mutated_child1)

    # prod_list = c.prd_list

    # sum_space = 0
    # for i in range(len(child1)):
    #     if (child1[i] == 1):
    #         sum_space += prod_list[i].getProdSize()
    #         print(prod_list[i])
    # print(sum_space)