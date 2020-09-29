from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List
import random


class CrossSpecificIndividual(CrossAlgorithm):

    def crossPopulation(self, population: List[Individual], totalPopulation: int, environment):
        for _ in range(int((totalPopulation - len(population)) / 2)):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            children = parent1.cross(parent2).copy()
            population.extend(children)
        return population
