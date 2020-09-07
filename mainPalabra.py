from geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.individual import Individual
from GAPalabra.selectionRanking import SelectionRanking
from GAPalabra.crossSinglePoint import CrossSinglePoint
from GAPalabra.mutateRandomPoints import MutateRandomPoints
from GAPalabra.word import Word

def createReferenceIndividual():
    individual:Individual = Word()
    individual.cromosoma = list("bananaNaranja")
    individual.fitness=0
    return individual

def run2():
    selection :SelectionAlgorithm = SelectionRanking()
    cross: CrossAlgorithm = CrossSinglePoint()
    mutation: MutationAlgorithm = MutateRandomPoints()
    GA = GeneticAlgorithmManager()
    GA.selectionAlgorithm =selection
    GA.crossAlgorithm= cross
    GA.mutationAlgorithm=mutation
    GA.individualReference=createReferenceIndividual()
    GA.run(20,2000)
    


if __name__ == '__main__':
    run2()
