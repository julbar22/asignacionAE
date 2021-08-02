from abc import ABC, abstractmethod
from frameworkAG.evolutionaryAlgorithm.individual import Individual
from typing import List

class FinishAction(ABC):
    
    def runFinishGenerationBlock(self, population:List[Individual], bestFitness:int,bestIndividual:Individual):
        raise NotImplementedError

    def runFinishRunBlock(self, population:List[Individual], bestFitness:int,bestIndividual:Individual):
        raise NotImplementedError

