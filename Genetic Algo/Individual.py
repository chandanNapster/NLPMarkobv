from Main import main 
import numpy as np

class Individual():
    m = main()
    product_list = m.getData()
    
    def __init__(self, chromosome = None):
        if chromosome == None:
            self.chromosome = []
            self.__set_chromosome()
        else: self.chromosome = chromosome

    def __set_chromosome(self):
        for i in range(len(Individual.product_list)):
            random_num = np.random.rand()
            if random_num > 0.5: self.chromosome.append(1)
            else: self.chromosome.append(0)    

    def __str__(self):
        return "[Chromosome: {0} | Total Price: {1} | Total Space: {2}]".format(self.chromosome, self.getTotalPrice(), self.getTotalSpace())  

    def getTotalPrice(self):
        sum = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == 1:
                sum += Individual.product_list[i].getProdPrice()
        return sum 

    def getTotalSpace(self):
        space = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == 1:
                space += Individual.product_list[i].getProdSize()
        return space            

# if __name__ == "__main__":
#     i = Individual()
#     print(i)
