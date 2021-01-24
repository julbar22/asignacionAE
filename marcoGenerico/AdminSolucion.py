from typing import List, Optional, TypeVar, Dict, Generic
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from geneticAlgorithm.finishAction import FinishAction
from modelSemanaEscolar.semanaEscolar import SemanaEscolar
from marcoGenerico.Ambiente import AmbienteEspecificoTiempo

class AdminSolucion():
    ambientes: List[AmbienteEspecificoTiempo]
    iteraciones: int
    aptitudFinal: int
    cantidadIndividuos: int
    selectionAlgorithm: SelectionAlgorithm
    mutationAlgorithm: MutationAlgorithm
    crossAlgorithm: CrossAlgorithm
    finishAlgorithm: FinishAction

    def __init__(self, ambientes: List[AmbienteEspecificoTiempo],
                 iteraciones: int,
                 aptitudFinal: int,
                 cantidadIndividuos: int,
                 selectionAlgorithm: SelectionAlgorithm,
                 mutationAlgorithm: MutationAlgorithm,
                 crossAlgorithm: CrossAlgorithm,
                 finishAlgorithm:FinishAction):
        self.iteraciones = iteraciones
        self.ambientes = ambientes
        self.aptitudFinal = aptitudFinal
        self.cantidadIndividuos = cantidadIndividuos
        self.selectionAlgorithm = selectionAlgorithm
        self.mutationAlgorithm = mutationAlgorithm
        self.crossAlgorithm = crossAlgorithm
        self.finishAlgorithm = finishAlgorithm
    

    def runAlgotirmo(self):
        for ambiente in self.ambientes:
            GA = GeneticAlgorithmManager()
            GA.selectionAlgorithm =self.selectionAlgorithm
            GA.crossAlgorithm= self.crossAlgorithm
            GA.mutationAlgorithm=self.mutationAlgorithm
            GA.environment=ambiente
            GA.finishActions = self.finishAlgorithm
            GA.individualReference= SemanaEscolar(ambiente)
            GA.run(self.cantidadIndividuos,self.iteraciones)