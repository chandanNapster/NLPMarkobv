from Population import Population
from Fitness import Fitness
import numpy as np
from Individual import Individual
from Main import main 

class GeneticAlgorithm():

    def __init__(self, population):
        self.population = population
        self.__parentPopulation = []
        self.__bestSolution = self.population[0]    

    def __get_bestSolution(self):
        return self.__bestSolution    

    def __get_parent(self):    
        chromosome_prob = []
        sum_scores = self.__sum_of_all_scores()
        for individual in self.population:
            prob = individual.getTotalPrice()/sum_scores
            chromosome_prob.append(prob)
        best_solution = self.__get_bestSolution()
        current_best_solution = np.random.choice(self.population, p=chromosome_prob)
        if best_solution.getTotalPrice() > current_best_solution.getTotalPrice() : parent = best_solution
        else : parent = current_best_solution
        return parent 


    def __sum_of_all_scores(self):
        sum_of_all_scores = 0
        for individual in self.population:
            sum_of_all_scores += individual.getTotalPrice()
        return sum_of_all_scores    

    def selectParent(self):
        for i in range(len(self.population)):
            parent_1 = self.__get_parent()
            parent_2 = self.__get_parent()
            self.__parentPopulation.append((parent_1,parent_2))
            # self.__parentPopulation.append(parent_2)
        return self.__parentPopulation  


    def crossOverPopulation(self, parentPopulation):
        crossOverPopulation = []
        for parents in parentPopulation:
            p1, p2 = parents
            # print(p1.chromosome, p2.chromosome)
            p1 = p1.chromosome
            p2 = p2.chromosome
            c1, c2 = self.__crossOver(p1,p2)
            crossOverPopulation.append(c1)
            crossOverPopulation.append(c2)
        return crossOverPopulation    

    def __crossOver(self, parent1, parent2):
        cutoff = self.__getcutoff(parent1, parent2)
    
        parent_1_part_1 = parent1[:cutoff]
        parent_1_part_2 = parent1[cutoff:]
        parent_2_part_1 = parent2[:cutoff]
        parent_2_part_2 = parent2[cutoff:]

        child1 = self.__createChild(parent_1_part_1, parent_2_part_2)
        child2 = self.__createChild(parent_2_part_1, parent_1_part_2)

        return child1, child2 

    def __createChild(self,list1, list2):
        list1 = list(list1)
        list2 = list(list2)

        list1 = self.__convert2int(list1)
        list2 = self.__convert2int(list2)

        for i in range(len(list2)):
            list1.append(list2[i])
        return list1

    def __convert2int(self,lista):
        listint = []
        for i in range(len(lista)):
            listint.append(int(lista[i]))
        return listint

    def __getcutoff(self,parent1, parent2):
        parent1 = list(parent1)
        parent2 = list(parent2)
        if len(parent1) == len(parent2):
            max_length = len(parent1)
            cutoff = np.random.randint(max_length)
        return cutoff

    def offspring_population_mutation(self, offSpring_chromosome_population):
        mutated_offsprings = []
        for chromosome in offSpring_chromosome_population:
            mutated_chromosome = self.__mutationChromosome(chromosome)
            individual = Individual(mutated_chromosome)
            mutated_offsprings.append(individual)
        return mutated_offsprings    


    def __mutationChromosome(self, chromosome, rate = 0.05):
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

    def best_individual_in_gen(self,population, generation):
        sortedIndividual = sorted(population, key = lambda x : x.getTotalPrice(), reverse=True)
        bestIndividual = sortedIndividual[0]
        bestIndividual.generation = generation
        # print('Chromosome-->',bestIndividual.chromosome,'\n', 'Total Price-->', bestIndividual.getTotalPrice(),'\n','Total Space-->',bestIndividual.getTotalSpace(),'\n','Gen -->', generation)         
        return bestIndividual, generation


if __name__ == "__main__":
    p_Obj = Population(10)
    p_Obj.get_fit_population()
    population = p_Obj.population 
    # population = p_Obj.population

    # for individual in population:
    #     print(individual)

    # print("********************************************************************************")
    
    

    # for i in population:
    #     print(i)  

    best_solutions_per_generation = []      

    print("***********************START OF GA*******************************************")
    while not (p_Obj.generation == 25) and len(population) != 0:
        # print("############################ WELCOME GEN {0}#####################################".format(p_Obj.generation))
        ga = GeneticAlgorithm(population)
        parentPopulation = ga.selectParent()
        offspringChromosomes = ga.crossOverPopulation(parentPopulation)
        p_Obj.incrementGeneration()
        mutated_Offsprings_population = ga.offspring_population_mutation(offspringChromosomes)

        # for indi in mutated_Offsprings_population:
        #     print(indi)

        # print("_________________________________________________________________________________")
        fit_population = Fitness(mutated_Offsprings_population).getFitness()
        # for indi in fit_population:
        #     print(indi)   

        population = fit_population
        best_individual, generation = ga.best_individual_in_gen(population, p_Obj.generation)

        best_solutions_per_generation.append(best_individual)

        # print("#######################END OF GEN ={0} THE TOTAL INDIVIDUALS = {1}###############".format(p_Obj.generation, len(population)))
        # print("")


    best_solutions_per_generation = sorted(best_solutions_per_generation, key = lambda x : x.getTotalPrice(), reverse=True)   

    # for individual in best_solutions_per_generation:
    #     print(individual, individual.generation)

    best_solution_after_GA = best_solutions_per_generation[0]

    print(best_solution_after_GA, best_solution_after_GA.generation)

    print("**************** BEST SOLUTION *****************************") 
    product_list = Individual.product_list

    for i in range(len(product_list)):
        if best_solution_after_GA.chromosome[i] == 1:
            print(product_list[i])

    # bestSolution = sorted(population, key = lambda x : x.getTotalPrice(), reverse=True) 

    # for i in bestSolution:
    #     print(i)

    # for parents in parentPopulation:
    #     p1, p2 = parents
    #     print(p1,p2)
    #     print("##########################")

    # for i in range(20):
    #     print("Parent 1 ", ga.get_parent())
    #     print("Parent 2 ", ga.get_parent())
    #     print("################################")

    # f = Fitness(population)

    

    # print("###################")
    # for indi in fit_population:
    #     print(indi)





