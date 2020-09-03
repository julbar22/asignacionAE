from abc import ABC, abstractmethod
from typing import List
class Individual(ABC):

    cromosoma = []
    fitness: int = 0

    def calculateFitness(self, individual):
        raise NotImplementedError

    def createRamdomIndividual(self, individualBase):
        raise NotImplementedError

    def mutate(self):
        raise NotImplementedError

