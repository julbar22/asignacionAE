from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List
import random


class SelectionTorneo(SelectionAlgorithm):

    cantidadIndividuos: int=10

    def __init__(self, cantidadIndividuos):
        self.cantidadIndividuos=cantidadIndividuos

    def select(self, population: List[Individual]):
        arraySelect=population.copy()
        while len(arraySelect)>self.cantidadIndividuos:
            for index in range(0,int(len(population)/2)):
                #print(index)
                if population[index].fitness>population[len(population)-(index+1)].fitness:
                    arraySelect.pop(index)
                else:                    
                    arraySelect.pop((len(population)-(index+1)))
            population= arraySelect.copy()

        return population
