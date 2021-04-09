from typing import List, Optional, TypeVar, Dict, Generic
from frameworkAG.Resources import Recurso, RecursoTiempo
from frameworkAG.ScheduleUtils import WeekDay, TimeTable
from frameworkAG.Entities import Asignacion
from schoolSchedule.resourcesSemana import Materia


class AmbienteGeneral():
    recursos: Dict[str, List[Recurso]]
    asignaciones: List[Asignacion]

    def __init__(self):
        self.asignaciones = list()
        self.recursos = {}
    
    def getRecursoPorTipoAndID(self, typeRecursoId: str, recursoId: str) -> Recurso:
        for typeRecurso in self.recursos:
            if(typeRecurso == typeRecursoId):
                listaRecusos: List[Recurso] = self.recursos[typeRecurso]
                for recurso in listaRecusos:
                    if recurso.identificador == recursoId:
                        return recurso

    def updateEnvironment(self,newEnvironment):
        pass


class AmbienteEspecificoTiempo(AmbienteGeneral):
    horario: TimeTable
    recursos: Dict[str, List[Recurso]]

    def __init__(self):
        super(AmbienteEspecificoTiempo,self).__init__()

