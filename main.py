from geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.individual import Individual
from selectionAlgorithmImpl.selectionRanking import SelectionRanking
from selectionAlgorithmImpl.selectionTorneo import SelectionTorneo
from crossAlgorithmImpl.crossSinglePoint import CrossSinglePoint
from crossAlgorithmImpl.crossMultiplePoint import CrossMultiplePoint
from crossAlgorithmImpl.crossSpecificIndividual import CrossSpecificIndividual
from mutateAlgorithmImpl.mutateRandomPoints import MutateRandomPoints
from mutateAlgorithmImpl.mutateAscendent import MutateAscendent
from modelSemanaEscolar.semanaEscolar import SemanaEscolar
from enums.diaSemana import DiaSemana
import json
import datetime
from modelSemanaEscolar.escenario import Escenario
from modelSemanaEscolar.escenarioCompleto1 import EscenarioCompleto1
from modelSemanaEscolar.escenarioCompleto2 import EscenarioCompleto2
from geneticAlgorithm.finishAction import FinishAction
from finishActionImpl.finishBestIndividualImpl import FinishBestIndividualImpl


def createReferenceIndividual(escenario):
    individual:Individual = SemanaEscolar(DiaSemana.lunes,DiaSemana.viernes)
    individual.fitness=0
    return individual

def run2():
    escenario = EscenarioCompleto2()
    selection :SelectionAlgorithm = SelectionRanking(0.3)
    cross: CrossAlgorithm = CrossSpecificIndividual()
    mutation: MutationAlgorithm = MutateRandomPoints()
    finishAction: FinishAction = FinishBestIndividualImpl()
    GA = GeneticAlgorithmManager()
    GA.selectionAlgorithm =selection
    GA.crossAlgorithm= cross
    GA.mutationAlgorithm=mutation
    GA.environment=escenario
    GA.individualReference=createReferenceIndividual(escenario)
    GA.finishActions = finishAction
    GA.run(20,1000)
    
if __name__ == '__main__':
    run2()
