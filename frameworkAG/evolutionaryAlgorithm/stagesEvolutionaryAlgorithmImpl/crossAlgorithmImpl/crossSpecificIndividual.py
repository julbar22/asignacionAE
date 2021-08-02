from frameworkAG.evolutionaryAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.evolutionaryAlgorithm.individual import Individual
from typing import List
import random
import copy


class CrossSpecificIndividual(CrossAlgorithm):

    def crossPopulation(self, population: List[Individual], totalPopulation: int, environment)->List[Individual]:
        populationCopy = population.copy()
        for _ in range(int((totalPopulation - len(population)) / 2)):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            children = parent1.cross(parent2,environment).copy()
            populationCopy.extend(children)
        return populationCopy
