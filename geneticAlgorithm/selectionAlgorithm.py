from abc import ABC, abstractmethod
from geneticAlgorithm.individual import Individual
from typing import List

class SelectionAlgorithm(ABC):
    
    def select(self, poblacion:List[Individual]):
        raise NotImplementedError

