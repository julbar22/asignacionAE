from datetime import date
from dia import Dia
from asignacion import Asignacion
from horario import Horario
import datetime
import json



class SemanaEscolar:

    dias = list()
    nombre = None

    def __init__(self, initDate: date, endDate: date):
        self.nombre = "Semana"
        self.dias=[]
        while endDate >= initDate:
            self.dias.append(Dia(initDate))
            # TODO cambiar forma de sumar dias
            initDate = date(initDate.year, initDate.month, initDate.day+1)

    def getDia(self, dia: date):
        for diaList in self.dias:
            if diaList.fecha == dia:
                return diaList
