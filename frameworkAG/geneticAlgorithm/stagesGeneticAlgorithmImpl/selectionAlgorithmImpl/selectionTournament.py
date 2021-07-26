from frameworkAG.geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from frameworkAG.geneticAlgorithm.individual import Individual
from typing import List
import random


class SelectionTournament(SelectionAlgorithm):

    quantityIndividuals: int=10

    def __init__(self, quantityIndividuals):
        self.quantityIndividuals=quantityIndividuals

    def select(self, population: List[Individual])->List[Individual]:
        arraySelect=population.copy()
        while len(arraySelect)>self.quantityIndividuals:
            for index in range(0,int(len(population)/2)):
                if population[index].fitness>population[len(population)-(index+1)].fitness:
                    arraySelect.pop(index)
                else:                    
                    arraySelect.pop((len(population)-(index+1)))
            population= arraySelect.copy()

        return population
