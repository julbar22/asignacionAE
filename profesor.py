from materia import Materia


class Profesor:

    materias = list()
    disponibilidad = list()
    nombre: ""

    def __init__(self, nombre):
        self.nombre = nombre

    def addDisponibilidad(self, horario: tuple):
        pass

    def addMateria(self, materia: Materia):
        self.materias.append(materia)
