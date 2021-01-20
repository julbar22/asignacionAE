from marcoGenerico.Ambiente import AmbienteGeneral, AdminSolucion
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from selectionAlgorithmImpl.selectionRanking import SelectionRanking
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from crossAlgorithmImpl.crossSpecificIndividual import CrossSpecificIndividual
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from mutateAlgorithmImpl.mutateRandomPoints import MutateRandomPoints
from finishActionImpl.finishBestIndividualImpl import FinishBestIndividualImpl
from geneticAlgorithm.finishAction import FinishAction


def run2():
    selection: SelectionAlgorithm = SelectionRanking(0.3)
    cross: CrossAlgorithm = CrossSpecificIndividual()
    mutation: MutationAlgorithm = MutateRandomPoints()
    finishAction: FinishAction = FinishBestIndividualImpl()
    ambiente: AmbienteGeneral = AmbienteGeneral()
    ambientesPorCurso = ambiente.getAbientePorCurso()
    admin: AdminSolucion = AdminSolucion(ambientes=ambientesPorCurso, iteraciones=1000, aptitudFinal=0, cantidadIndividuos=20,
                                         selectionAlgorithm=selection, mutationAlgorithm=mutation, crossAlgorithm=cross, finishAlgorithm=finishAction)
    admin.runAlgotirmo()


if __name__ == '__main__':
    run2()
