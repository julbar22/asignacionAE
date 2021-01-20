from marcoGenerico.Recurso import Recurso, RecursoTiempo
from marcoGenerico.Horarios import TimeSlot, TimeTable
from typing import List, Optional, TypeVar, Dict, Generic


class Materia(Recurso):
    horasSemanales = 0
    horasMinimasCons = 0
    horasMaximasCons = 0

    def __init__(self, identificador: str, hsSemanales: int, hsMinimasCons: int, hsMaximasCons: int):
        super(Materia,self).__init__(identificador)
        self.horasSemanales = hsSemanales
        self.horasMinimasCons = hsMinimasCons
        self.horasMaximasCons = hsMaximasCons


class Asignacion:
    espacioTiempo: TimeSlot
    listaRecursoId: List[str]


class Schedule:
    datos: List[Asignacion]
    datosPorEspacio: Dict[TimeSlot, Asignacion]
    horario: TimeTable
