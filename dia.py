from horario import Horario
from datetime import date


class Dia:

    fecha: date = None
    horarios = list()

    def __init__(self, fecha: date):
        self.fecha = fecha
        self.horarios = []

    def addHorario(self, horario: Horario):
        self.horarios.append(horario)

