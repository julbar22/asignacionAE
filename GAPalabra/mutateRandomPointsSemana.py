from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List
import random
import string


class MutateRandomPointsSemana(MutationAlgorithm):

    def mutationPopulation(self, population: List[Individual],environment):
        for individual in population:
            for idx in range(0,len(individual.cromosoma)):
                if random.uniform(0.0, 1.0) <= 0.1:
                    individual= individual.mutate(idx,environment)                    
        return population

