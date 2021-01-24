from abc import ABC, abstractmethod
from typing import List
from marcoGenerico.Entidades import Schedule
from marcoGenerico.Ambiente import AmbienteEspecificoTiempo


class Individual(ABC):

    cromosoma = []
    errores = []
    fitness: int = 0


    def calculateFitness(self):
        raise NotImplementedError

    def createRamdomIndividual(self, ambienteNuevo)->ABC:
        raise NotImplementedError

    def mutate(self, index)->ABC:
        raise NotImplementedError

    def cross(self, couple,ambienteNuevo) -> List[ABC]:
        raise NotImplementedError

    def improvement(self) -> List[ABC]:
        raise NotImplementedError

    def imprimirIndividuo(self):
        raise NotImplementedError

    def imprimirErrores(self):
        raise NotImplementedError


class IndividuoTiempo(Individual):
    horario:Schedule=None
    ambiente:AmbienteEspecificoTiempo=None
    
    def __init__(self, ambiente:AmbienteEspecificoTiempo):
        self.horario:Schedule = Schedule(ambiente.horario)
