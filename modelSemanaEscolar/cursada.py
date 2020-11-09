
from modelSemanaEscolar.materia import Materia
from modelSemanaEscolar.curso import Curso


class Cursada:

    materia = None
    curso = None
    horasSemanales = 0
    horasMinimasCons = 0
    horasMaximasCons = 0

    def __init__(self, curso: Curso, materia: Materia, horasSemanales: int, horasMaximas: int, horasMinimas: int):
        self.materia = materia
        self.curso = curso
        self.horasSemanales = horasSemanales
        self.horasMaximasCons = horasMaximas
        self.horasMinimasCons = horasMinimas

    def __eq__(self, other):
        if other !=None:
            return self.materia.nombre == other.materia.nombre and self.curso.nombre == other.curso.nombre
        else:
            return False
