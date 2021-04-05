from modelSemanaEscolar.cursada import Cursada


class Profesor:

    materias = list()
    disponibilidad = None
    nombre: ""

    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []


    def getCursada(self, materia:str,curso:str):
        for cursada in self.materias:
            if cursada.materia.nombre== materia:
                if cursada.curso.nombre== curso:
                    return cursada
