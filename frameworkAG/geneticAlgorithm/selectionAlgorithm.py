from abc import ABC, abstractmethod
from frameworkAG.geneticAlgorithm.individual import Individual
from typing import List

class SelectionAlgorithm(ABC):
    
    def select(self, population:List[Individual])-> List[Individual]:
        raise NotImplementedError

