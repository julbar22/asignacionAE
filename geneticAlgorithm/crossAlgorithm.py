from abc import ABC, abstractmethod
from geneticAlgorithm.individual import Individual
from typing import List

class CrossAlgorithm(ABC):
    
    def crossPopulation(self, poblacion:List[Individual]):
        raise NotImplementedError

    def crossIndividuo(self, individuo1:Individual, individuo2:Individual):
        raise NotImplementedError

