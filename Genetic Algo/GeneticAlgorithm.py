from IndividualV3 import Individual
from Main import main as m
from GeneticOperations import GeneticFunc
import numpy as np

class GeneticAlgorithm():
    def __init__(self, size = 20):
        self.population_size = size
        self.population = []
        self.bestSolution = None

    def __setInitialPopulation(self):
        for i in range(self.population_size):
            self.population.append(Individual())

        return self.population 

    def setPopulation(self):
        for indi in self.__setInitialPopulation():
            indi.fitness()

        for indi in self.population:
            if indi.getTotalSpace() > 3:
                indi.setTotalPrice(1)

        # self.population = sorted(self.population, key = lambda x : x.getTotalPrice(), reverse=True)    
        self.setBestSolution()
        return self.population

    def setBestSolution(self):
        self.bestSolution = self.population[0]    

    def getBestSolution(self):
        return self.bestSolution

    def overall_sum_scores(self):
        sum = 0
        for indi in self.population:
            sum += indi.getTotalPrice()
        return sum    

    def get_chromosome_based_on_prob(self):
        total_sum = self.overall_sum_scores()
        chromosome_prob = []
        for indi in self.population:
            prob = indi.getTotalPrice()/ total_sum
            chromosome_prob.append(prob)

        chromosome = np.random.choice(self.population, p=chromosome_prob) 
        return chromosome
        

    def get_parent(self):
        best_solution = self.getBestSolution()
        chromosome = self.get_chromosome_based_on_prob()
        if best_solution.getTotalPrice() < chromosome.getTotalPrice():
            best_solution = chromosome

        return best_solution    

if __name__ == "__main__":

    ga = GeneticAlgorithm(10)
    population = ga.setPopulation()
    # for indi in ga.setPopulation():
    #     print(indi)

    gf = GeneticFunc()

    for i in range(0, len(population)):
        
        parent_1 = ga.get_parent()
        parent_2 = ga.get_parent()
        # parent_1.setTotalPrice(0)
        # parent_2.setTotalPrice(0)
        # while parent_1.getTotalPrice() == parent_2.getTotalPrice():
        #     parent_1 = ga.get_parent()
        #     parent_2 = ga.get_parent()
        print("parent 1 ", parent_1)
        print("parent 2 ", parent_2)
        child1, child2 = gf.crossOver(parent_1.getChromosome(),parent_2.getChromosome())
        print("child 1 ", child1)
        print("child 2 ", child2)

        child1 = gf.mutation(child1, 0.05)
        child2 = gf.mutation(child2, 0.05)

        print("Mutated child 1 ", child1)
        print("Mutated child 2 ", child2)

        new_c1 = Individual(chromosome=child1)
        new_c2 = Individual(chromosome=child2)

        print("New Gen child 1 ", new_c1)
        print("New Gen child 2 ", new_c2)
        print("################################")

    # print("####################################")
    # parent_1 = ga.get_parent()
    # print('Parent 1')
    # print(parent_1)

    # parent_2 = ga.get_parent()
    # print("parent 2")
    # print(parent_2)

    # gf = GeneticFunc()
    # child1, child2 = gf.crossOver(parent_1.getChromosome(),parent_2.getChromosome())
    child1 = gf.mutation(child1, 0.05)
    child2 = gf.mutation(child2, 0.05)
    # print('child 1')
    # child1 = Individual(chromosome=child1)
    # # child1.setGeneration()
    # print(child1)
    # print('child2')
    # child2 = Individual(chromosome=child2)
    # child2.setSiblingGen(child1.getGeneration())
    # # child2.setGeneration()
    # print(child2)

    # print('best chromosome')
    # print(ga.get_chromosome_based_on_prob())
    # print('best solution')
    # print(ga.get_parent())
    # population = []
    # prod_list = m.getData()

    # for i in range(10):
    #     population.append(Individual(prod_list))

    # for individual in population:
    #     individual.fitness()
        
    # for i in population:
    #     if i.getTotalSpace() > 3:
    #         i.setTotalPrice(1)

    # # HOW TO SORT OBJECTS IN A LIST

    # population = sorted(population, key = lambda x : x.getTotalPrice(), reverse=True)

    # for i in population:
    #     print(i)
    # # price_list = price_list.sort()

    