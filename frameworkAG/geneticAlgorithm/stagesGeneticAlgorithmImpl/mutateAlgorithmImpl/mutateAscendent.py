from frameworkAG.geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from frameworkAG.geneticAlgorithm.individual import Individual
from typing import List
import random
import string


class MutateAscendent(MutationAlgorithm):

    generation: int = 0
    growthRate:float=0.1
    generationGrowth:int=1000

    def __init__(self):
        self.generation = 0
        self.growthRate=0.1
        self.generationGrowth=800

    def mutationPopulation(self, population: List[Individual], environment)->List[Individual]:
        self.generation+=1
        tasaMutacion=int(self.generation/self.generationGrowth)
        for individual in population:
            if random.uniform(0.0, 1.0) <= (tasaMutacion+1)*0.1:
                individual = individual.mutate(random.randint(0,(len(individual.chromosome)-1)), environment)
        return population
