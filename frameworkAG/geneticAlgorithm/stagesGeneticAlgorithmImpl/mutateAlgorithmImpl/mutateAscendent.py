from frameworkAG.geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from frameworkAG.geneticAlgorithm.individual import Individual
from typing import List
import random
import string


class MutateAscendent(MutationAlgorithm):

    generacion: int = 0
    tasaCrecimiento:float=0.1
    generacionCrecimiento:int=1000

    def __init__(self):
        self.generacion = 0
        self.tasaCrecimiento=0.1
        self.generacionCrecimiento=800

    def mutationPopulation(self, population: List[Individual], environment)->List[Individual]:
        self.generacion+=1
        tasaMutacion=int(self.generacion/self.generacionCrecimiento)
        for individual in population:
            if random.uniform(0.0, 1.0) <= (tasaMutacion+1)*0.1:
                individual = individual.mutate(random.randint(0,(len(individual.cromosoma)-1)), environment)
        return population
