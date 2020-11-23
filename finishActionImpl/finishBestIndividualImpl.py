from geneticAlgorithm.finishAction import FinishAction
from geneticAlgorithm.individual import Individual
from typing import List


class FinishBestIndividualImpl(FinishAction):

    mejorFitness: int

    def __init__(self):
        # TODO cambiar ese numero enviarlo por parametro
        self.mejorFitness = 1000

    def runFinishGenerationBlock(self, population: List[Individual], mejorFitness: int, mejorIndividuo: Individual):
        if self.mejorFitness > mejorFitness:
            self.mejorFitness = mejorFitness      
            print(self.mejorFitness)      
            mejorIndividuo.imprimirErrores()
            print("---------------------------")

    def runFinishRunBlock(self, population: List[Individual], mejorFitness: int, mejorIndividuo: Individual):
        #mejorIndividuo.imprimirIndividuo()
        print(self.mejorFitness)
