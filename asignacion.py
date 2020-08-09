from profesor import Profesor
from cursada import Cursada


class Asignacion:

    profesor = None
    cursada = None

    def __init__(self, profesor: Profesor, cursada: Cursada):
        self.profesor = profesor        
        self.cursada = cursada
        self.profesor.materias.append(self.cursada.materia)
