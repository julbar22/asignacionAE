from enums.diaSemana import DiaSemana
from modelSemanaEscolar.cursada import Cursada

class ErrorSemana():

    tipoError:int
    profesor:str
    dia:DiaSemana
    horasSemanales:int
    horasAsignadas:int
    cursada:Cursada

    def __init__(self, tipoError:int, cursada: Cursada):
        self.tipoError = tipoError
        self.profesor=""
        self.cursada=cursada

    def printError(self):
        errorCompleto=" tipoError:"+str(self.tipoError)
        errorCompleto+=" materia:"+self.cursada.materia.nombre
        errorCompleto+=" curso:"+self.cursada.curso.nombre
        errorCompleto+=" profesor:"+self.profesor
        errorCompleto+=" dia:"+self.dia.name
        errorCompleto+=" horasMaximas:"+str(self.horasSemanales)
        errorCompleto+=" horasAsignadas:"+str(self.horasAsignadas)
        print(errorCompleto)