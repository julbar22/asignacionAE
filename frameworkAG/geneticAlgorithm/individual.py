from abc import ABC, abstractmethod
from typing import List
from frameworkAG.Entities import Schedule
from frameworkAG.Environments import EnvironmentTime


class Individual(ABC):

    mistakes = []
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

    def printIndividual(self):
        raise NotImplementedError

    def printErrors(self):
        raise NotImplementedError


class IndividualTime(Individual):
    timetable:Schedule=None
    environment:EnvironmentTime=None
    
    def __init__(self, environment:EnvironmentTime):
        self.timetable:Schedule = Schedule(environment.timetable)
