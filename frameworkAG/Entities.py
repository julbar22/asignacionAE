from frameworkAG.Resources import Recurso, RecursoTiempo
from frameworkAG.ScheduleUtils import TimeSlot, TimeTable
from typing import List, Optional, TypeVar, Dict, Generic

class Asignacion:
    espacioTiempo: TimeSlot
    listaRecursoId: List[str]

    def __init__(self):
        self.listaRecursoId= list()
    
    def containRecurso(self, recursoId:str)-> bool:
        return True if recursoId in self.listaRecursoId else False


class Schedule:
    datos: List[Asignacion]
    datosPorEspacio: Dict[TimeSlot, Asignacion]
    horario: TimeTable

    def __init__(self, horario:TimeTable):
        #Revisar si necesito un copy
        self.datos= list()
        self.datosPorEspacio={}
        self.horario = TimeTable(horario._open_slots)

    def agregarAsignacion(self, timeSlot:TimeSlot,asignacion: Asignacion):
        self.datos.append(asignacion)
        self.datosPorEspacio[timeSlot]=asignacion
        self.horario._open_slots.remove(timeSlot)
        
    def getAsignacionesByRecurso(self,recursoId)->List[Asignacion]:
        return list(filter(lambda asignacion: asignacion.containRecurso(recursoId),self.datos))
