from modelSemanaEscolar.resourcesSemana import Materia
from frameworkAG.Horarios import WeekDay

class ErrorSemana():

    tipoError:int
    profesor:str
    dia:WeekDay
    horasSemanales:int
    horasAsignadas:int
    cursada:Materia

    def __init__(self, tipoError:int, cursada: Materia):
        self.tipoError = tipoError
        self.profesor=""
        self.cursada=cursada
        self.horasSemanales=0
        self.horasAsignadas=0
        self.dia = WeekDay.SUN
       

    def printError(self):
        errorCompleto=" tipoError:"+str(self.tipoError)
        errorCompleto+=" materia:"+self.cursada.identificador
        errorCompleto+=" profesor:"+self.profesor
        errorCompleto+=" dia:"+self.dia.name
        errorCompleto+=" horasMaximas:"+str(self.horasSemanales)
        errorCompleto+=" horasAsignadas:"+str(self.horasAsignadas)
        print(errorCompleto)