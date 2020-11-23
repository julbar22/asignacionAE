from abc import ABC, abstractmethod
from geneticAlgorithm.individual import Individual
from typing import List

class CrossAlgorithm(ABC):
    
    def crossPopulation(self, population:List[Individual], totalPopulation:int)->List[Individual]:
        raise NotImplementedError

