from abc import ABC, abstractmethod
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm


class GeneticAlgorithmManager(ABC):
    selectionAlgorithm: SelectionAlgorithm = None
    mutationAlgorithm: MutationAlgorithm = None
    crossAlgorithm: CrossAlgorithm = None
    aptitudeThreshold = 0
    finishGenerationBlock = None
    finishRunBlock = None

    def createStartingPopulation(self, populationQuantity:int):
        raise NotImplementedError

    def run(self, populationQuantity:int, generations:int):
        raise NotImplementedError
