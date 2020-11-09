from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List


class SelectionRanking(SelectionAlgorithm):

    varianza: float = 0.2

    def __init__(self, varianza):
        self.varianza=varianza

    def select(self, population: List[Individual])-> List[Individual]:
        population = sorted(
            population, key=lambda individual: individual.fitness)
        population = population[:int(self.varianza * len(population))]
        return population
