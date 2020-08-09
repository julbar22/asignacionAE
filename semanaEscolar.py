from datetime import date
from dia import Dia
from asignacion import Asignacion
from horario import Horario
import datetime
import json
from diaSemana import DiaSemana


class SemanaEscolar:

    dias = list()
    nombre = None

    def __init__(self, initDate: DiaSemana, endDate: DiaSemana):
        self.nombre = "Semana"
        self.dias = []
        while endDate.value >= initDate.value:
            self.dias.append(Dia(initDate))
            initDate = self.getSiguienteDia(initDate)

    def getDia(self, dia: DiaSemana):
        for diaList in self.dias:
            if diaList.fecha.value == dia.value:
                return diaList

    def getSiguienteDia(self, dia: DiaSemana):
        proximoDia = dia.value+1
        return DiaSemana(0) if proximoDia > 6 else DiaSemana(proximoDia)
