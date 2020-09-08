from abc import ABC, abstractmethod
from typing import List
class Individual(ABC):

    cromosoma = []
    fitness: int = 0

    def calculateFitness(self, individual,enviroment):
        raise NotImplementedError

    def createRamdomIndividual(self, individualBase,enviroment):
        raise NotImplementedError

    def mutate(self,index,enviroment):
        raise NotImplementedError



