from models.cursada import Cursada
from enums.diaSemana import DiaSemana


class Profesor:

    materias = list()
    disponibilidad = None
    nombre: ""

    def __init__(self, nombre):
        self.nombre = nombre
        self.initDisponibilidad()

    def initDisponibilidad(self):
        self.disponibilidad = {
            DiaSemana.lunes: [],
            DiaSemana.martes: [],
            DiaSemana.miercoles: [],
            DiaSemana.jueves: [],
            DiaSemana.viernes: [],
            DiaSemana.sabado: [],
            DiaSemana.domingo: []
        }

    def addDisponibilidad(self, dia:DiaSemana,horario:tuple):
        for key in self.disponibilidad.keys():
            if key == dia:
                self.disponibilidad[key].append(horario)
