from models.asignacion import Asignacion


class Horario:

    horario = None
    asignacion = None

    def __init__(self, asignacion: Asignacion, horario: tuple):
        self.asignacion = asignacion
        self.horario = horario
    
    def printHorario(self):
        nombreProfesor=self.asignacion.profesor.nombre
        print(nombreProfesor)

