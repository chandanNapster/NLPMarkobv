from Main import main as m
from IndividualV1 import Individual


class Fitness():

    def __init__(self, prd_list):
        self.__product_list = prd_list
        
    def getProductList(self):
        return self.__product_list

    def getChromosome(self):
        indiv = Individual(self.getProductList())
        return indiv.getChromosome() 

    def getFitness(self, chromosome):
        total_score, space_sum = 0,0
        prod_list = self.getProductList()
        for i in range(len(chromosome)):
            if chromosome[i] == 1:
                total_score += prod_list[i].getProdPrice()
                space_sum += prod_list[i].getProdSize()

        return total_score, space_sum

    def getBestChromosome(self):
        space = 0
        while not 2.99 < space < 3:
            chromo = self.getChromosome()
            total, space = self.getFitness(chromo)

        return chromo, total, space


# if __name__ == "__main__":
#     prod_list = []
#     prd_list = m.getData()
#     fit = Fitness(prd_list)

#     parent_list = []
#     for i in range(2):
#         c,t,s = fit.getBestChromosome()
#         parent_list.append(c)
#         # print(t,s)
#         # print(c)  

#     for item in parent_list:
#         print(item)

        

    