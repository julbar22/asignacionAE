from modelSemanaEscolar.curso import Curso
from modelSemanaEscolar.materia import Materia
from modelSemanaEscolar.cursada import Cursada
from modelSemanaEscolar.profesor import Profesor
from enums.diaSemana import DiaSemana
from modelSemanaEscolar.escenarioAbstract import EscenarioAbstract
import json

class Escenario(EscenarioAbstract):

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
        MateSegundoA = self.getCursada("Matematicas", "Segundo A")
        MateSegundoB = self.getCursada("Matematicas", "Segundo B")
        FisicaPrimeroA = self.getCursada("Fisica", "Primero A")
        LengPrimeroA = self.getCursada("Lengua", "Primero A")
        LengPrimeroB = self.getCursada("Lengua", "Primero B")
        LengSegundoA = self.getCursada("Lengua", "Segundo A")
        LengSegundoB = self.getCursada("Lengua", "Segundo B")

        profesorPedro = Profesor("Pedro Gonzales")
        profesorPedro.materias.append(MatePrimeroA)
        profesorPedro.materias.append(MatePrimeroB)
        profesorPedro.materias.append(MateSegundoA)
        profesorPedro.materias.append(MateSegundoB)
        profesorPedro.materias.append(FisicaPrimeroA)        
        profesorPedro.addDisponibilidad(DiaSemana.lunes, (9,  18))
        profesorPedro.addDisponibilidad(DiaSemana.martes, (9,  12))
        profesorPedro.addDisponibilidad(DiaSemana.jueves, (12,  18))
        profesorPedro.addDisponibilidad(DiaSemana.viernes, (9,  18))

        profesorCarla = Profesor("Carla Gomez")
        profesorCarla.materias.append(LengPrimeroA)
        profesorCarla.materias.append(LengPrimeroB)
        profesorCarla.materias.append(LengSegundoA)
        profesorCarla.materias.append(LengSegundoB)
        profesorCarla.addDisponibilidad(DiaSemana.lunes, (9,  18))
        profesorCarla.addDisponibilidad(DiaSemana.martes, (9,  12))
        profesorCarla.addDisponibilidad(DiaSemana.jueves, (12,  18))
        profesorCarla.addDisponibilidad(DiaSemana.viernes, (9,  18))

        self.profesores.append(profesorPedro)
        self.profesores.append(profesorCarla)

