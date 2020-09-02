from abc import ABC, abstractmethod
class Individual(ABC):
    
    def calculateFitness(self, individual: Individual):
        raise NotImplementedError

    def createRamdomIndividual(self,individualBase: Individual):
        raise NotImplementedError
 