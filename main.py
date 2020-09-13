from geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.individual import Individual
from selectionAlgorithmImpl.selectionRanking import SelectionRanking
from crossAlgorithmImpl.crossSinglePoint import CrossSinglePoint
from crossAlgorithmImpl.crossMultiplePoint import CrossMultiplePoint
from mutateAlgorithmImpl.mutateRandomPoints import MutateRandomPoints
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
    semanaRerence= createReferenceIndividual(escenario)
    selection :SelectionAlgorithm = SelectionRanking()
    cross: CrossAlgorithm = CrossMultiplePoint()
    mutation: MutationAlgorithm = MutateRandomPoints()
    GA = GeneticAlgorithmManager()
    GA.selectionAlgorithm =selection
    GA.crossAlgorithm= cross
    GA.mutationAlgorithm=mutation
    GA.enviroment=escenario
    GA.individualReference=createReferenceIndividual(escenario)
    GA.run(20,10000)
    


if __name__ == '__main__':
    run2()
