from frameworkAG.Recurso import Recurso, RecursoTiempo

class Materia(Recurso):
    horasSemanales = 0
    horasMinimasCons = 0
    horasMaximasCons = 0

    def __init__(self, identificador: str, hsSemanales: int, hsMinimasCons: int, hsMaximasCons: int):
        super(Materia,self).__init__(identificador)
        self.horasSemanales = hsSemanales
        self.horasMinimasCons = hsMinimasCons
        self.horasMaximasCons = hsMaximasCons