from abc import ABC, abstractmethod
from geneticAlgorithm.individual import Individual
from typing import List

class SelectionAlgorithm(ABC):
    
    def select(self, population:List[Individual]):
        raise NotImplementedError

