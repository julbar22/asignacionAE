from frameworkAG.StandardSolver import StandardSolver
from frameworkAG.geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.selectionAlgorithmImpl.selectionRanking import SelectionRanking
from frameworkAG.geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.crossAlgorithmImpl.crossSpecificIndividual import CrossSpecificIndividual
from frameworkAG.geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.mutateAlgorithmImpl.mutateRandomPoints import MutateRandomPoints
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.finishActionImpl.finishBestIndividualImpl import FinishBestIndividualImpl
from frameworkAG.geneticAlgorithm.finishAction import FinishAction
from schoolSchedule.environmentSchool import EnvironmentSchool
from frameworkAG.geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
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
    GA = GeneticAlgorithmManager()
    GA.selectionAlgorithm = selection
    GA.crossAlgorithm = cross
    GA.mutationAlgorithm = mutation
    GA.finishActions = finishAction
    admin: StandardSolver = StandardSolver(environments=environmentsByCourse,
                                           iterations=1000,
                                           finalFitness=0,
                                           quantityIndividuals=20,
                                           geneticAlgorithm=GA,
                                           classReference=SchoolWeek)
    admin.runAlgorithm()


if __name__ == '__main__':
    run2()
