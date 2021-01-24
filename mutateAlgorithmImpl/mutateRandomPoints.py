from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List
import random
import string


class MutateRandomPoints(MutationAlgorithm):

    def mutationPopulation(self, population: List[Individual],environment)->List[Individual]:
        for individual in population:
            if random.uniform(0.0, 1.0) <= 0.1:
                    individual= individual.mutate(0,environment)                    
        return population

