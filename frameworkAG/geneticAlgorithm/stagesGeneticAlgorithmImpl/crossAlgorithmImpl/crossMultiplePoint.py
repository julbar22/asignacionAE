from frameworkAG.geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.geneticAlgorithm.individual import Individual
from typing import List
import random

class CrossMultiplePoint(CrossAlgorithm):
    
    def crossPopulation(self, population:List[Individual], totalPopulation:int,environment)->List[Individual]:
        offspring = []
        for _ in  range(int((totalPopulation - len(population)) / 2)):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1 =  parent1.createRamdomIndividual(parent1,environment)
            child2 =  parent2.createRamdomIndividual(parent2,environment)
            for idx in range(0,len(parent1.cromosoma)):
                if random.uniform(0.0, 1.0) <= 0.5:
                    child1.cromosoma[idx]=parent1.cromosoma[idx]
                    child2.cromosoma[idx]=parent2.cromosoma[idx]
                else:
                    child1.cromosoma[idx]=parent2.cromosoma[idx]
                    child2.cromosoma[idx]=parent1.cromosoma[idx]
            offspring.append(child1)
            offspring.append(child2)

        population.extend(offspring)
        return population


