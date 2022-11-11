from Population import Population
from Fitness import Fitness
    

if __name__ == "__main__":
    p_Obj = Population(20)
    population = p_Obj.population

    for individual in population:
        print(individual)

    p_Obj.get_fit_population()    

    print("******************")
    population = p_Obj.population

    for i in population:
        print(i)    

    f = Fitness(population)

    fit_population = f.getFitness()

    print("###################")
    for indi in fit_population:
        print(indi)





