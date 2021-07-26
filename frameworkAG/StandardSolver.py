from typing import List, Optional, TypeVar, Dict, Generic,Type
from frameworkAG.geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from frameworkAG.Environments import GeneralEnvironment

_T = TypeVar('_T')

class StandardSolver():
    environments: List[GeneralEnvironment]
    iterations: int
    finalFitness: int
    quantityIndividuals: int
    geneticAlgorithm: GeneticAlgorithmManager
    classReference:Type[_T]
    def __init__(self,
                 environments: List[GeneralEnvironment],
                 iterations: int,
                 finalFitness: int,
                 quantityIndividuals: int,
                 geneticAlgorithm: GeneticAlgorithmManager,
                 classReference: Type[_T]):
        self.iterations = iterations
        self.environments = environments
        self.finalFitness = finalFitness
        self.quantityIndividuals = quantityIndividuals
        self.geneticAlgorithm = geneticAlgorithm
        self.classReference = classReference

    def runAlgorithm(self):
        for environment in self.environments:            
            self.geneticAlgorithm.cleanSolution()
            self.geneticAlgorithm.environment = environment
            self.geneticAlgorithm.individualReference = self.classReference(environment)
            self.geneticAlgorithm.run(self.quantityIndividuals, self.iterations)
            environment.updateEnvironment(self.geneticAlgorithm.bestIndividual.environment)
            #self.updateRecursos(self.geneticAlgorithm.bestIndividual.environment, environment)
