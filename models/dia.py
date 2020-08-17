from models.horario import Horario
from datetime import date
from enums.diaSemana import DiaSemana


class Dia:

    fecha: DiaSemana  = None
    horarios = list()

    def __init__(self, fecha: DiaSemana):
        self.fecha = fecha
        self.horarios = []

    def addHorario(self, horario: Horario):
        self.horarios.append(horario)

