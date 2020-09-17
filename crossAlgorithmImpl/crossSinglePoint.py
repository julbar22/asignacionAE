from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List
import random

class CrossSinglePoint(CrossAlgorithm):
    
    def crossPopulation(self, population:List[Individual], totalPopulation:int,environment):
        offspring = []
        for _ in  range(int((totalPopulation - len(population)) / 2)):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1 =  parent1.createRamdomIndividual(parent1,environment)
            child2 =  parent2.createRamdomIndividual(parent2,environment)
            split = random.randint(0, len(parent1.cromosoma))
            child1.cromosoma = parent1.cromosoma[0:split] + parent2.cromosoma[split:len(parent1.cromosoma)]
            child2.cromosoma = parent2.cromosoma[0:split] + parent1.cromosoma[split:len(parent1.cromosoma)]
            offspring.append(child1)
            offspring.append(child2)

        population.extend(offspring)
        return population

    def crossIndividuo(self, individuo1:Individual, individuo2:Individual):
        raise NotImplementedError

