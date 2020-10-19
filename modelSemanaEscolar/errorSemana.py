from enums.diaSemana import DiaSemana

class ErrorSemana():

    tipoError:int
    materia:str
    curso:str
    profesor:str
    dia:DiaSemana
    horasSemanales:int
    horasAsignadas:int

    def __init__(self, tipoError:int):
        self.tipoError = tipoError
        self.profesor=""

    def printError(self):
        errorCompleto=" tipoError:"+str(self.tipoError)
        errorCompleto+=" materia:"+self.materia
        errorCompleto+=" curso:"+self.curso
        errorCompleto+=" profesor:"+self.profesor
        errorCompleto+=" dia:"+self.dia.name
        errorCompleto+=" horasSemanales:"+str(self.horasSemanales)
        errorCompleto+=" horasAsignadas:"+str(self.horasAsignadas)
        print(errorCompleto)