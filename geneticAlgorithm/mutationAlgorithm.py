from abc import ABC, abstractmethod
from geneticAlgorithm.individual import Individual
from typing import List

class MutationAlgorithm(ABC):
    
    def mutationPopulation(self, poblacion:List[Individual]):
        raise NotImplementedError

    def mutationIndividuo(self, individuo1:Individual, individuo2:Individual):
        raise NotImplementedError

