from frameworkAG.geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.geneticAlgorithm.individual import Individual
from typing import List
import random

class CrossSinglePoint(CrossAlgorithm):
    
    def crossPopulation(self, population:List[Individual], totalPopulation:int,environment)->List[Individual]:
        offspring = []
        for _ in  range(int((totalPopulation - len(population)) / 2)):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1 =  parent1.createRamdomIndividual(parent1,environment)
            child2 =  parent2.createRamdomIndividual(parent2,environment)
            split = random.randint(0, len(parent1.chromosome))
            child1.chromosome = parent1.chromosome[0:split] + parent2.chromosome[split:len(parent1.chromosome)]
            child2.chromosome = parent2.chromosome[0:split] + parent1.chromosome[split:len(parent1.chromosome)]
            offspring.append(child1)
            offspring.append(child2)

        population.extend(offspring)
        return population


