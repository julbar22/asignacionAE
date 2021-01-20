from modelSemanaEscolar.curso import Curso
from modelSemanaEscolar.materia import Materia
from modelSemanaEscolar.cursada import Cursada
from modelSemanaEscolar.profesor import Profesor
from enums.diaSemana import DiaSemana
from abc import ABC, abstractmethod
import json


def json_default(value):
    if isinstance(value, DiaSemana):
        return value.name
    else:
        return value.__dict__


class EscenarioAbstract(ABC):

    cursos = []
    materias = []
    cursada = []
    profesores = []

    def __init__(self):
        self.cursos = list()
        self.createMaterias()
        self.createCursos()
        self.createCursada()
        self.createProfesores()

    def createCursos(self):
        raise NotImplementedError

    def createMaterias(self):
        raise NotImplementedError

    def createCursada(self):
        raise NotImplementedError

    def createProfesores(self):
        raise NotImplementedError

    def getMateria(self, nameMateria: str):
        for materia in self.materias:
            if materia.nombre == nameMateria:
                return materia

    def gerCurso(self, nameCurso: str):
        for curso in self.cursos:
            if curso.nombre == nameCurso:
                return curso

    def getCursada(self, nameMateria: str, nameCurso: str):
        for cursada in self.cursada:
            if cursada.materia.nombre == nameMateria and cursada.curso.nombre == nameCurso:
                return cursada

    def getAllCursadaByMateria(self, nameMateria: str):
        cursadas = []
        for cursada in self.cursada:
            if cursada.materia.nombre == nameMateria:
                cursadas.append(cursada)
        return cursadas
    
    def getAllCursadaByCurso(self, nameCurso: str):
        cursadas = []
        for cursada in self.cursada:
            if cursada.curso.nombre == nameCurso:
                cursadas.append(cursada)
        return cursadas

    def getProfesor(self, nameProfesor: str):
        for profesor in self.profesores:
            if profesor.nombre == nameProfesor:
                return profesor

    def createPrintProfesor(self, profesor: Profesor):
        arrayCompleto = profesor.disponibilidad
        arrayMaterias = []
        for cursada in profesor.materias:
            arrayMaterias.append(
                (cursada.curso.nombre, cursada.materia.nombre))
        arrayCompleto["materias"] = arrayMaterias
        return arrayCompleto

    def createPrintMateria(self, materia: Materia):
        cursadas = self.getAllCursadaByMateria(materia.nombre)
        materiaPrint = {materia.nombre: {}}

        for cursada in cursadas:
            materiaPrint[materia.nombre][cursada.curso.nombre] = [
                cursada.horasSemanales, cursada.horasMinimasCons, cursada.horasMaximasCons]

        return materiaPrint

    def printEscenario(self):
        escenarioInicial = {"docentes": [],
                            "materias": []}
        for profesor in self.profesores:
            escenarioInicial["docentes"].append(
                {profesor.nombre: self.createPrintProfesor(profesor)})

        for materia in self.materias:
            escenarioInicial["materias"].append(
                self.createPrintMateria(materia))

        json_data = json.dumps(escenarioInicial, skipkeys=True, check_circular=True,
                               default=lambda o: json_default(o), indent=4)
        print("--------------------inicio escenario --------------------------")
        print(json_data)
        print("--------------------fin escenario --------------------------")

    def getProfesoresByCursada(self, cursada: Cursada):
        profesoresOpcionales = list()
        for profesor in self.profesores:
            cursadaProfesor = profesor.getCursada(
                cursada.materia.nombre, cursada.curso.nombre)
            if cursadaProfesor != None:
                profesoresOpcionales.append(profesor)
        return profesoresOpcionales
