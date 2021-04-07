from typing import List, Optional, TypeVar, Dict, Generic
from frameworkAG.geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from frameworkAG.geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from frameworkAG.geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from frameworkAG.geneticAlgorithm.finishAction import FinishAction
from schoolSchedule.semanaEscolar import SemanaEscolar
from frameworkAG.Ambiente import AmbienteEspecificoTiempo
from frameworkAG.Recurso import RecursoTiempo,Recurso
from frameworkAG.Horarios import TimeTable

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
            self.updateRecursos(GA.mejorIndividuo.ambiente,ambiente)
    
    #TODO: esto se debe sacar porque es especifico de cada problema
    def updateRecursos(self,ambienteNuevo:AmbienteEspecificoTiempo,ambienteOld:AmbienteEspecificoTiempo):
        for materia in ambienteNuevo.recursos["Materia"]:
            profesorNuevo:RecursoTiempo =materia.recursosVinculados["Profesor"][0]
            materiaOld=ambienteOld.getRecursoPorTipoAndID("Materia",materia.identificador)
            profesorViejo:RecursoTiempo =  materiaOld.recursosVinculados["Profesor"][0]
            timeTableNueva=profesorViejo.disponibilidad.intersection(profesorNuevo.disponibilidad)
            profesorViejo.disponibilidad = TimeTable(timeTableNueva._open_slots)

