from frameworkAG.StandardSolver import StandardSolver
from frameworkAG.evolutionaryAlgorithm.selectionAlgorithm import SelectionAlgorithm
from frameworkAG.evolutionaryAlgorithm.stagesEvolutionaryAlgorithmImpl.selectionAlgorithmImpl.selectionRanking import SelectionRanking
from frameworkAG.evolutionaryAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.evolutionaryAlgorithm.stagesEvolutionaryAlgorithmImpl.crossAlgorithmImpl.crossSpecificIndividual import CrossSpecificIndividual
from frameworkAG.evolutionaryAlgorithm.mutationAlgorithm import MutationAlgorithm
from frameworkAG.evolutionaryAlgorithm.stagesEvolutionaryAlgorithmImpl.mutateAlgorithmImpl.mutateRandomPoints import MutateRandomPoints
from frameworkAG.evolutionaryAlgorithm.stagesEvolutionaryAlgorithmImpl.finishActionImpl.finishBestIndividualImpl import FinishBestIndividualImpl
from frameworkAG.evolutionaryAlgorithm.finishAction import FinishAction
from schoolSchedule.environmentSchool import EnvironmentSchool
from frameworkAG.evolutionaryAlgorithm.evolutionaryAlgorithmManager import EvolutionaryAlgorithmManager
from schoolSchedule.schoolWeek import SchoolWeek


def run2():
    #ranking del 30% de la poblacion
    selection: SelectionAlgorithm = SelectionRanking(0.3)
    cross: CrossAlgorithm = CrossSpecificIndividual()
    mutation: MutationAlgorithm = MutateRandomPoints()
    finishAction: FinishAction = FinishBestIndividualImpl()
    environment: EnvironmentSchool = EnvironmentSchool()
    #Se generan los environments separados por course
    environmentsByCourse = environment.getEnvironmentByCourse()
    GA = EvolutionaryAlgorithmManager()
    GA.selectionAlgorithm = selection
    GA.crossAlgorithm = cross
    GA.mutationAlgorithm = mutation
    GA.finishActions = finishAction
    admin: StandardSolver = StandardSolver(environments=environmentsByCourse,
                                           iterations=1000,
                                           finalFitness=0,
                                           quantityIndividuals=20,
                                           evolutionaryAlgorithm=GA,
                                           classReference=SchoolWeek)
    admin.runAlgorithm()


if __name__ == '__main__':
    run2()
