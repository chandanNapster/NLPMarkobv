from Individual import Individual

class Population():

    GEN_ID = 0

    def __init__(self, size = 5):
        self.population = []
        self.population_size = size
        self.__setPopulation()
        self.generation = 0

    def incrementGeneration(self):
        Population.GEN_ID += 1
        self.generation = Population.GEN_ID

    def presentgeneration(self):
        return self.generation        

    def __setPopulation(self):
        for i in range(self.population_size):
            self.population.append(Individual())    

    def get_fit_population(self):
        for i in range(self.population_size):
            self.population[i] = self.__get_fit_individual()
        return self.population    

    def __get_fit_individual(self):
        space_sum = 0
        individual = None
        while not 2.9 < space_sum < 3.0:
            individual = Individual()
            space_sum = individual.getTotalSpace()
        return individual