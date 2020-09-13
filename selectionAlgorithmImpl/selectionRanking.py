from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List


class SelectionRanking(SelectionAlgorithm):

    def __init__(self):
        pass

    def select(self, population: List[Individual]):
        population = sorted(
            population, key=lambda individual: individual.fitness)
        population = population[:int(0.2 * len(population))]
        return population
