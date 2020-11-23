from abc import ABC, abstractmethod
from typing import List


class Individual(ABC):

    cromosoma = []
    errores = []
    fitness: int = 0

    def calculateFitness(self, individual, environment):
        raise NotImplementedError

    def createRamdomIndividual(self, individualBase, environment)->ABC:
        raise NotImplementedError

    def mutate(self, index, environment)->ABC:
        raise NotImplementedError

    def cross(self, couple) -> List[ABC]:
        raise NotImplementedError

    def improvement(self, environment) -> List[ABC]:
        raise NotImplementedError

    def imprimirIndividuo(self):
        raise NotImplementedError

    def imprimirErrores(self):
        raise NotImplementedError
