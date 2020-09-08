from geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.individual import Individual
from GAPalabra.selectionRanking import SelectionRanking
from GAPalabra.crossSinglePoint import CrossSinglePoint
from GAPalabra.crossMultiplePoint import CrossMultiplePoint
from GAPalabra.mutateRandomPointsSemana import MutateRandomPointsSemana
from models.semanaEscolar import SemanaEscolar
from enums.diaSemana import DiaSemana
import json
import datetime
from escenario import Escenario


def createReferenceIndividual(escenario):
    individual:Individual = SemanaEscolar(DiaSemana.lunes,DiaSemana.viernes)
    individual.fitness=0
    return individual

def run2():
    escenario = Escenario()
    semanaRerence= createReferenceIndividual(escenario)
    selection :SelectionAlgorithm = SelectionRanking()
    cross: CrossAlgorithm = CrossMultiplePoint()
    mutation: MutationAlgorithm = MutateRandomPointsSemana()
    GA = GeneticAlgorithmManager()
    GA.selectionAlgorithm =selection
    GA.crossAlgorithm= cross
    GA.mutationAlgorithm=mutation
    GA.enviroment=escenario
    GA.individualReference=createReferenceIndividual(escenario)
    GA.run(20,10000)
    


if __name__ == '__main__':
    run2()
