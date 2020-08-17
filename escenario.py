from models.curso import Curso
from models.materia import Materia
from models.cursada import Cursada
from models.profesor import Profesor
from enums.diaSemana import DiaSemana


class Escenario:

    cursos = []
    materias = []
    cursada = []
    profesores = []

    def __init__(self):
        self.cursos = list()
        self.createMaterias()
        self.createCursada()
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

    def createCursada(self):
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

    def createProfesores(self):
        self.profesores = []
        MatePrimeroA = self.getCursada("Matematicas", "Primero A")
        MatePrimeroB = self.getCursada("Matematicas", "Primero B")
        FisicaPrimeroA = self.getCursada("Matematicas", "Primero A")
        LengPrimeroA = self.getCursada("Lengua", "Primero A")
        LengPrimeroB = self.getCursada("Lengua", "Primero B")

        profesorPedro = Profesor("Pedro Gonzales")
        profesorPedro.materias.append(MatePrimeroA)
        profesorPedro.materias.append(MatePrimeroB)
        profesorPedro.materias.append(FisicaPrimeroA)
        profesorPedro.addDisponibilidad(DiaSemana.lunes, (9,  18))
        profesorPedro.addDisponibilidad(DiaSemana.martes, (9,  12))
        profesorPedro.addDisponibilidad(DiaSemana.jueves, (12,  18))
        profesorPedro.addDisponibilidad(DiaSemana.viernes, (9,  18))

        profesorCarla = Profesor("Carla Gomez")
        profesorCarla.materias.append(LengPrimeroA)
        profesorCarla.materias.append(LengPrimeroB)
        profesorCarla.addDisponibilidad(DiaSemana.lunes, (9,  18))
        profesorCarla.addDisponibilidad(DiaSemana.martes, (9,  12))
        profesorCarla.addDisponibilidad(DiaSemana.jueves, (12,  18))
        profesorCarla.addDisponibilidad(DiaSemana.viernes, (9,  18))

        self.profesores.append(profesorPedro)
        self.profesores.append(profesorCarla)

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

    def getProfesor(self, nameProfesor: str):
        for profesor in self.profesores:
            if profesor.nombre == nameProfesor:
                return profesor
