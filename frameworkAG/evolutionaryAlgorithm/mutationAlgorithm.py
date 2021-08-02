from abc import ABC, abstractmethod
from frameworkAG.evolutionaryAlgorithm.individual import Individual
from typing import List

class MutationAlgorithm(ABC):
    
    def mutationPopulation(self, population:List[Individual],environment)->List[Individual]:
        raise NotImplementedError

