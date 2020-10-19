from modelSemanaEscolar.curso import Curso
from modelSemanaEscolar.materia import Materia
from modelSemanaEscolar.cursada import Cursada
from modelSemanaEscolar.profesor import Profesor
from enums.diaSemana import DiaSemana
from modelSemanaEscolar.escenarioAbstract import EscenarioAbstract
import json


class EscenarioCompleto1(EscenarioAbstract):

    def createCursos(self):
        self.cursos = []
        self.cursos.append(Curso("1"))
        self.cursos.append(Curso("2"))
        self.cursos.append(Curso("3"))
        self.cursos.append(Curso("4"))
        self.cursos.append(Curso("5"))

        return self.cursos

    def createMaterias(self):
        self.materias = []
        self.materias.append(Materia("Ed. Fisica"))
        self.materias.append(Materia("Matematicas"))
        self.materias.append(Materia("Dibujo"))
        self.materias.append(Materia("Danza"))
        self.materias.append(Materia("C. Naturales"))
        self.materias.append(Materia("Lengua"))
        self.materias.append(Materia("Sistemas"))
        self.materias.append(Materia("Musica"))
        self.materias.append(Materia("Canto"))
        self.materias.append(Materia("Ingles"))
        self.materias.append(Materia("Quimica"))
        self.materias.append(Materia("Fisica"))
        return self.materias

    def createCursada(self):
        self.cursada = []
        primero = self.gerCurso("1")
        segundo = self.gerCurso("2")
        tercero = self.gerCurso("3")
        cuarto = self.gerCurso("4")
        quinto = self.gerCurso("5")
        edFisica = self.getMateria("Ed. Fisica")
        self.cursada.append(Cursada(primero, edFisica, 2, 2, 1))
        self.cursada.append(Cursada(segundo, edFisica, 2, 2, 1))
        self.cursada.append(Cursada(tercero, edFisica, 2, 2, 1))
        self.cursada.append(Cursada(cuarto, edFisica, 2, 2, 1))
        self.cursada.append(Cursada(quinto, edFisica, 2, 2, 1))
        matematicas = self.getMateria("Matematicas")
        self.cursada.append(Cursada(primero, matematicas, 4, 2, 1))
        self.cursada.append(Cursada(segundo, matematicas, 4, 2, 1))
        self.cursada.append(Cursada(tercero, matematicas, 5, 2, 1))
        self.cursada.append(Cursada(cuarto, matematicas, 5, 2, 1))
        self.cursada.append(Cursada(quinto, matematicas, 5, 2, 1))
        dibujo = self.getMateria("Dibujo")
        self.cursada.append(Cursada(primero, dibujo, 5, 2, 1))
        self.cursada.append(Cursada(segundo, dibujo, 5, 2, 1))
        self.cursada.append(Cursada(tercero, dibujo, 4, 2, 1))
        self.cursada.append(Cursada(cuarto, dibujo, 2, 2, 1))
        self.cursada.append(Cursada(quinto, dibujo, 2, 2, 1))
        danza = self.getMateria("Danza")
        self.cursada.append(Cursada(primero, danza, 4, 2, 1))
        self.cursada.append(Cursada(segundo, danza, 3, 2, 1))
        self.cursada.append(Cursada(tercero, danza, 2, 2, 1))
        self.cursada.append(Cursada(cuarto, danza, 2, 2, 1))
        self.cursada.append(Cursada(quinto, danza, 2, 2, 1))
        cNaturales = self.getMateria("C. Naturales")
        self.cursada.append(Cursada(primero, cNaturales, 2, 2, 1))
        self.cursada.append(Cursada(segundo, cNaturales, 2, 2, 1))
        self.cursada.append(Cursada(tercero, cNaturales, 3, 2, 1))
        self.cursada.append(Cursada(cuarto, cNaturales, 3, 2, 1))
        self.cursada.append(Cursada(quinto, cNaturales, 3, 2, 1))
        lengua = self.getMateria("Lengua")
        self.cursada.append(Cursada(primero, lengua, 3, 2, 1))
        self.cursada.append(Cursada(segundo, lengua, 3, 2, 1))
        self.cursada.append(Cursada(tercero, lengua, 3, 2, 1))
        self.cursada.append(Cursada(cuarto, lengua, 6, 2, 1))
        self.cursada.append(Cursada(quinto, lengua, 5, 2, 1))
        sistemas = self.getMateria("Sistemas")
        self.cursada.append(Cursada(primero, sistemas, 1, 1, 1))
        self.cursada.append(Cursada(segundo, sistemas, 2, 2, 1))
        self.cursada.append(Cursada(tercero, sistemas, 3, 2, 1))
        self.cursada.append(Cursada(cuarto, sistemas, 3, 2, 1))
        self.cursada.append(Cursada(quinto, sistemas, 3, 2, 1))
        musica = self.getMateria("Musica")
        self.cursada.append(Cursada(primero, musica, 3, 2, 1))
        self.cursada.append(Cursada(segundo, musica, 4, 2, 1))
        canto = self.getMateria("Canto")
        self.cursada.append(Cursada(primero, canto, 3, 2, 1))
        self.cursada.append(Cursada(segundo, canto, 2, 2, 1))
        self.cursada.append(Cursada(tercero, canto, 3, 2, 1))
        ingles = self.getMateria("Ingles")
        self.cursada.append(Cursada(primero, ingles, 2, 2, 1))
        self.cursada.append(Cursada(segundo, ingles, 3, 2, 1))
        self.cursada.append(Cursada(tercero, ingles, 3, 2, 1))
        self.cursada.append(Cursada(cuarto, ingles, 4, 2, 1))
        self.cursada.append(Cursada(quinto, ingles, 4, 2, 1))
        quimica = self.getMateria("Quimica")
        self.cursada.append(Cursada(tercero, quimica, 1, 1, 1))
        self.cursada.append(Cursada(cuarto, quimica, 1, 1, 1))
        self.cursada.append(Cursada(quinto, quimica, 1, 1, 1))
        edFisica = self.getMateria("Fisica")
        self.cursada.append(Cursada(tercero, edFisica, 1, 1, 1))
        self.cursada.append(Cursada(cuarto, edFisica, 1, 1, 1))
        self.cursada.append(Cursada(quinto, edFisica, 2, 2, 1))

    def createProfesores(self):
        self.profesores = []
        edFisica1 = self.getCursada("Ed. Fisica", "1")
        edFisica2 = self.getCursada("Ed. Fisica", "2")
        edFisica3 = self.getCursada("Ed. Fisica", "3")
        edFisica4 = self.getCursada("Ed. Fisica", "4")
        edFisica5 = self.getCursada("Ed. Fisica", "5")
        mate1 = self.getCursada("Matematicas", "1")
        mate2 = self.getCursada("Matematicas", "2")
        mate3 = self.getCursada("Matematicas", "3")
        mate4 = self.getCursada("Matematicas", "4")
        mate5 = self.getCursada("Matematicas", "5")
        dibujo1 = self.getCursada("Dibujo", "1")
        dibujo2 = self.getCursada("Dibujo", "2")
        dibujo3 = self.getCursada("Dibujo", "3")
        dibujo4 = self.getCursada("Dibujo", "4")
        dibujo5 = self.getCursada("Dibujo", "5")
        danza1 = self.getCursada("Danza", "1")
        danza2 = self.getCursada("Danza", "2")
        danza3 = self.getCursada("Danza", "3")
        danza4 = self.getCursada("Danza", "4")
        danza5 = self.getCursada("Danza", "5")
        cNaturales1 = self.getCursada("C. Naturales", "1")
        cNaturales2 = self.getCursada("C. Naturales", "2")
        cNaturales3 = self.getCursada("C. Naturales", "3")
        cNaturales4 = self.getCursada("C. Naturales", "4")
        cNaturales5 = self.getCursada("C. Naturales", "5")
        lengua1 = self.getCursada("Lengua", "1")
        lengua2 = self.getCursada("Lengua", "2")
        lengua3 = self.getCursada("Lengua", "3")
        lengua4 = self.getCursada("Lengua", "4")
        lengua5 = self.getCursada("Lengua", "5")
        sistemas1 = self.getCursada("Sistemas", "1")
        sistemas2 = self.getCursada("Sistemas", "2")
        sistemas3 = self.getCursada("Sistemas", "3")
        sistemas4 = self.getCursada("Sistemas", "4")
        sistemas5 = self.getCursada("Sistemas", "5")
        musica1 = self.getCursada("Musica", "1")
        musica2 = self.getCursada("Musica", "2")
        canto1 = self.getCursada("Canto", "1")
        canto2 = self.getCursada("Canto", "2")
        canto3 = self.getCursada("Canto", "3")
        ingles1 = self.getCursada("Ingles", "1")
        ingles2 = self.getCursada("Ingles", "2")
        ingles3 = self.getCursada("Ingles", "3")
        ingles4 = self.getCursada("Ingles", "4")
        ingles5 = self.getCursada("Ingles", "5")
        quimica3 = self.getCursada("Quimica", "3")
        quimica4 = self.getCursada("Quimica", "4")
        quimica5 = self.getCursada("Quimica", "5")
        fisica3 = self.getCursada("Fisica", "3")
        fisica4 = self.getCursada("Fisica", "4")
        fisica5 = self.getCursada("Fisica", "5")

        profesor1 = Profesor("Juan")
        profesor1.materias.append(edFisica1)
        profesor1.materias.append(edFisica2)
        profesor1.materias.append(edFisica3)
        profesor1.materias.append(edFisica4)
        profesor1.materias.append(edFisica5)
        profesor1.materias.append(danza1)
        profesor1.materias.append(danza2)
        profesor1.materias.append(danza3)
        profesor1.materias.append(danza4)
        profesor1.materias.append(danza5)
        profesor1.addDisponibilidad(DiaSemana.lunes, (7,  13))
        profesor1.addDisponibilidad(DiaSemana.martes, (7,  13))
        profesor1.addDisponibilidad(DiaSemana.miercoles, (7,  13))
        profesor1.addDisponibilidad(DiaSemana.viernes, (7,  13))
        self.profesores.append(profesor1)

        profesor2 = Profesor("Pedro")
        profesor2.materias.append(mate1)
        profesor2.materias.append(mate2)
        profesor2.materias.append(mate3)
        profesor2.materias.append(mate4)
        profesor2.materias.append(mate5)
        profesor2.materias.append(fisica3)
        profesor2.materias.append(fisica4)
        profesor2.materias.append(fisica5)
        profesor2.addDisponibilidad(DiaSemana.lunes, (7,  13))
        profesor2.addDisponibilidad(DiaSemana.martes, (7,  13))
        profesor2.addDisponibilidad(DiaSemana.miercoles, (7,  13))
        profesor2.addDisponibilidad(DiaSemana.jueves, (7,  13))
        profesor2.addDisponibilidad(DiaSemana.viernes, (7,  13))
        self.profesores.append(profesor2)

        profesor3 = Profesor("Diana")
        profesor3.materias.append(dibujo1)
        profesor3.materias.append(dibujo2)
        profesor3.materias.append(dibujo3)
        profesor3.materias.append(dibujo4)
        profesor3.materias.append(dibujo5)
        profesor3.addDisponibilidad(DiaSemana.lunes, (7,  13))
        profesor3.addDisponibilidad(DiaSemana.martes, (7,  13))
        profesor3.addDisponibilidad(DiaSemana.miercoles, (7,  13))
        profesor3.addDisponibilidad(DiaSemana.jueves, (7,  13))
        self.profesores.append(profesor3)

        profesor4 = Profesor("Lucas")
        profesor4.materias.append(lengua1)
        profesor4.materias.append(lengua2)
        profesor4.materias.append(lengua3)
        profesor4.materias.append(lengua4)
        profesor4.materias.append(lengua5)
        profesor4.materias.append(ingles1)
        profesor4.materias.append(ingles2)
        profesor4.materias.append(ingles3)
        profesor4.addDisponibilidad(DiaSemana.lunes, (7,  13))
        profesor4.addDisponibilidad(DiaSemana.martes, (7,  13))
        profesor4.addDisponibilidad(DiaSemana.miercoles, (7,  13))
        profesor4.addDisponibilidad(DiaSemana.jueves, (7,  13))
        profesor4.addDisponibilidad(DiaSemana.viernes, (7,  13))
        self.profesores.append(profesor4)

        profesor5 = Profesor("Martha")
        profesor5.materias.append(ingles4)
        profesor5.materias.append(ingles5)
        profesor5.addDisponibilidad(DiaSemana.miercoles, (7,  13))
        profesor5.addDisponibilidad(DiaSemana.viernes, (7,  13))
        self.profesores.append(profesor5)

        profesor6 = Profesor("Luis")
        profesor6.materias.append(sistemas1)
        profesor6.materias.append(sistemas2)
        profesor6.materias.append(sistemas3)
        profesor6.materias.append(sistemas4)
        profesor6.materias.append(sistemas5)
        profesor6.addDisponibilidad(DiaSemana.martes, (7,  13))
        profesor6.addDisponibilidad(DiaSemana.jueves, (7,  13))
        profesor6.addDisponibilidad(DiaSemana.viernes, (7,  13))
        self.profesores.append(profesor6)

        profesor7 = Profesor("Nora")
        profesor7.materias.append(cNaturales1)
        profesor7.materias.append(cNaturales2)
        profesor7.materias.append(cNaturales3)
        profesor7.materias.append(cNaturales4)
        profesor7.materias.append(cNaturales5)
        profesor7.materias.append(quimica3)
        profesor7.materias.append(quimica4)
        profesor7.materias.append(quimica5)
        profesor7.addDisponibilidad(DiaSemana.lunes, (7,  13))
        profesor7.addDisponibilidad(DiaSemana.jueves, (7,  13))
        profesor7.addDisponibilidad(DiaSemana.viernes, (7,  13))
        self.profesores.append(profesor7)

        profesor8 = Profesor("Paola")
        profesor8.materias.append(musica1)
        profesor8.materias.append(musica2)
        profesor8.materias.append(canto1)
        profesor8.materias.append(canto2)
        profesor8.materias.append(canto3)
        profesor8.addDisponibilidad(DiaSemana.martes, (7,  13))
        profesor8.addDisponibilidad(DiaSemana.miercoles, (7,  13))
        profesor8.addDisponibilidad(DiaSemana.viernes, (7,  13))
        self.profesores.append(profesor8)
