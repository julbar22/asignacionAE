from frameworkAG.AdminSolucion import AdminSolucion
from frameworkAG.geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.selectionAlgorithmImpl.selectionRanking import SelectionRanking
from frameworkAG.geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.crossAlgorithmImpl.crossSpecificIndividual import CrossSpecificIndividual
from frameworkAG.geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.mutateAlgorithmImpl.mutateRandomPoints import MutateRandomPoints
from frameworkAG.geneticAlgorithm.stagesGeneticAlgorithmImpl.finishActionImpl.finishBestIndividualImpl import FinishBestIndividualImpl
from frameworkAG.geneticAlgorithm.finishAction import FinishAction
from schoolSchedule.environmentSchool import EnvironmentSchool


def run2():
    selection: SelectionAlgorithm = SelectionRanking(0.3)
    cross: CrossAlgorithm = CrossSpecificIndividual()
    mutation: MutationAlgorithm = MutateRandomPoints()
    finishAction: FinishAction = FinishBestIndividualImpl()
    ambiente: EnvironmentSchool = EnvironmentSchool()
    ambientesPorCurso = ambiente.getAbientePorCurso()
    admin: AdminSolucion = AdminSolucion(ambientes=ambientesPorCurso, iteraciones=1000, aptitudFinal=0, cantidadIndividuos=20,
                                         selectionAlgorithm=selection, mutationAlgorithm=mutation, crossAlgorithm=cross, finishAlgorithm=finishAction)
    admin.runAlgotirmo()


if __name__ == '__main__':
    run2()
