from abc import ABC, abstractmethod
from geneticAlgorithm.individual import Individual
from typing import List

class FinishAction(ABC):
    
    def runFinishGenerationBlock(self, population:List[Individual], mejorFitness:int,mejorIndividuo:Individual):
        raise NotImplementedError

    def runFinishRunBlock(self, population:List[Individual], mejorFitness:int,mejorIndividuo:Individual):
        raise NotImplementedError

