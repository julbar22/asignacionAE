from abc import ABC, abstractmethod
from geneticAlgorithm.individual import Individual
from typing import List

class MutationAlgorithm(ABC):
    
    def mutationPopulation(self, population:List[Individual]):
        raise NotImplementedError

