from frameworkAG.evolutionaryAlgorithm.finishAction import FinishAction
from frameworkAG.evolutionaryAlgorithm.individual import Individual
from typing import List


class FinishBestIndividualImpl(FinishAction):

    bestFitness: int

    def __init__(self):
        # TODO cambiar ese numero enviarlo por parametro
        self.bestFitness = 1000

    def runFinishGenerationBlock(self, population: List[Individual], bestFitness: int, bestIndividual: Individual):
        if self.bestFitness > bestFitness:
            self.bestFitness = bestFitness      
            print(self.bestFitness)      
            bestIndividual.printErrors()
            print("---------------------------")

    def runFinishRunBlock(self, population: List[Individual], bestFitness: int, bestIndividual: Individual):
        pass
