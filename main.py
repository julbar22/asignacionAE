from geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.individual import Individual
from selectionAlgorithmImpl.selectionRanking import SelectionRanking
from selectionAlgorithmImpl.selectionTorneo import SelectionTorneo
from crossAlgorithmImpl.crossSinglePoint import CrossSinglePoint
from crossAlgorithmImpl.crossMultiplePoint import CrossMultiplePoint
from mutateAlgorithmImpl.mutateRandomPoints import MutateRandomPoints
from mutateAlgorithmImpl.mutateAscendent import MutateAscendent
from modelSemanaEscolar.semanaEscolar import SemanaEscolar
from enums.diaSemana import DiaSemana
import json
import datetime
from modelSemanaEscolar.escenario import Escenario


def createReferenceIndividual(escenario):
    individual:Individual = SemanaEscolar(DiaSemana.lunes,DiaSemana.viernes)
    individual.fitness=0
    return individual

def run2():
    escenario = Escenario()
    #TODO esta referencia me servira cuando tenga clases asignadas
    selection :SelectionAlgorithm = SelectionRanking(0.2)
    #selection :SelectionAlgorithm = SelectionTorneo(10)
    cross: CrossAlgorithm = CrossMultiplePoint()
    #mutation: MutationAlgorithm = MutateRandomPoints()
    mutation: MutationAlgorithm = MutateAscendent()
    GA = GeneticAlgorithmManager()
    GA.selectionAlgorithm =selection
    GA.crossAlgorithm= cross
    GA.mutationAlgorithm=mutation
    GA.environment=escenario
    GA.individualReference=createReferenceIndividual(escenario)
    GA.run(20,5000)
    


if __name__ == '__main__':
    run2()
