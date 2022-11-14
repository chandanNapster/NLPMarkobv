class Fitness():

    def __init__(self, population):
        self.__population = list(population)
        self.__fitPopulation = []


    def getFitness(self):
        for individual in self.__population:
            if 2.9 < individual.getTotalSpace() < 3.0:
                self.__fitPopulation.append(individual) 
        return self.__fitPopulation       


# if __name__ == "__main__":
    # f = Fitness([1,0,0,1,2])
    # f.getFitness()