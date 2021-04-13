from frameworkAG.geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from frameworkAG.geneticAlgorithm.individual import Individual
from typing import List


class SelectionRanking(SelectionAlgorithm):

    variance: float = 0.2

    def __init__(self, variance):
        self.variance=variance

    def select(self, population: List[Individual])-> List[Individual]:
        population = sorted(
            population, key=lambda individual: individual.fitness)
        population = population[:int(self.variance * len(population))]
        return population
