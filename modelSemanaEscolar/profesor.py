from modelSemanaEscolar.cursada import Cursada
from enums.diaSemana import DiaSemana


class Profesor:

    materias = list()
    disponibilidad = None
    nombre: ""

    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []
        self.initDisponibilidad()

    def initDisponibilidad(self):
        self.disponibilidad = {
            DiaSemana.lunes.name: [],
            DiaSemana.martes.name: [],
            DiaSemana.miercoles.name: [],
            DiaSemana.jueves.name: [],
            DiaSemana.viernes.name: [],
            # DiaSemana.sabado.name: [],
            #DiaSemana.domingo.name: []
        }

    def addDisponibilidad(self, dia: DiaSemana, horario: tuple):
        for key in self.disponibilidad.keys():
            if key == dia.name:
                self.disponibilidad[key].append(horario[0])
                self.disponibilidad[key].append(horario[1])

    def getCursada(self, materia:str,curso:str):
        for cursada in self.materias:
            if cursada.materia.nombre== materia:
                if cursada.curso.nombre== curso:
                    return cursada
