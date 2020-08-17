from models.curso import Curso
from models.materia import Materia
from models.cursada import Cursada


class Escenario:

    cursos = []
    materias = []
    cursada = []

    def __init__(self):
        self.cursos = list()
        self.createMaterias()
        self.createCursos()

    def createCursos(self):
        self.cursos = []
        self.cursos.append(Curso("Primero A"))
        self.cursos.append(Curso("Primero B"))
        self.cursos.append(Curso("Segundo A"))
        self.cursos.append(Curso("Segundo B"))
        return self.cursos

    def createMaterias(self):
        self.materias = []
        self.materias.append(Materia("Matematicas"))
        self.materias.append(Materia("Lengua"))
        self.materias.append(Materia("Fisica"))
        return self.materias

    def getCursada(self):
        self.cursada = []
        matematicas = self.getMateria("Matematicas")
        primeroA = self.gerCurso("Primero A")
        primeroB = self.gerCurso("Primero B")
        segundoA = self.gerCurso("Segundo A")
        segundoB = self.gerCurso("Segundo B")
        self.cursada.append(Cursada(primeroA, matematicas, 4, 2, 1))
        self.cursada.append(Cursada(primeroB, matematicas, 4, 2, 1))
        self.cursada.append(Cursada(segundoA, matematicas, 3, 3, 1))
        self.cursada.append(Cursada(segundoB, matematicas, 3, 3, 1))
        lengua = self.getMateria("Lengua")
        self.cursada.append(Cursada(primeroA, lengua, 4, 2, 1))
        self.cursada.append(Cursada(primeroB, lengua, 4, 2, 1))
        self.cursada.append(Cursada(segundoA, lengua, 3, 3, 1))
        self.cursada.append(Cursada(segundoB, lengua, 3, 3, 1))
        fisica = self.getMateria("Fisica")
        self.cursada.append(Cursada(primeroA, fisica, 4, 2, 1))
        return self.cursada

    def getMateria(self, nameMateria: str):
        for materia in self.materias:
            if materia.nombre == nameMateria:
                return materia

    def gerCurso(self, nameCurso: str):
        for curso in self.cursos:
            if curso.nombre == nameCurso:
                return curso
