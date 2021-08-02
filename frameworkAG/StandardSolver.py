from typing import List, Optional, TypeVar, Dict, Generic,Type
from frameworkAG.evolutionaryAlgorithm.evolutionaryAlgorithmManager import EvolutionaryAlgorithmManager
from frameworkAG.Environments import GeneralEnvironment

_T = TypeVar('_T')

class StandardSolver():
    environments: List[GeneralEnvironment]
    iterations: int
    finalFitness: int
    quantityIndividuals: int
    evolutionaryAlgorithm: EvolutionaryAlgorithmManager
    classReference:Type[_T]
    def __init__(self,
                 environments: List[GeneralEnvironment],
                 iterations: int,
                 finalFitness: int,
                 quantityIndividuals: int,
                 evolutionaryAlgorithm: EvolutionaryAlgorithmManager,
                 classReference: Type[_T]):
        self.iterations = iterations
        self.environments = environments
        self.finalFitness = finalFitness
        self.quantityIndividuals = quantityIndividuals
        self.evolutionaryAlgorithm = evolutionaryAlgorithm
        self.classReference = classReference

    def runAlgorithm(self):
        for environment in self.environments:            
            self.evolutionaryAlgorithm.cleanSolution()
            self.evolutionaryAlgorithm.environment = environment
            self.evolutionaryAlgorithm.individualReference = self.classReference(environment)
            self.evolutionaryAlgorithm.run(self.quantityIndividuals, self.iterations)
            environment.updateEnvironment(self.evolutionaryAlgorithm.bestIndividual.environment)
            #self.updateRecursos(self.evolutionaryAlgorithm.bestIndividual.environment, environment)
