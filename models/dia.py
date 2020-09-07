from models.horario import Horario
from datetime import date
from enums.diaSemana import DiaSemana
from escenario import Escenario
import random
from typing import List
from models.materia import Materia
from models.profesor import Profesor
from models.cursada import Cursada
from models.asignacion import Asignacion
from models.horario import Horario


class Dia:

    fecha: DiaSemana = None
    horarios = list()

    def __init__(self, fecha: DiaSemana):
        self.fecha = fecha
        self.horarios = []

    def addHorario(self, horario: Horario):
        self.horarios.append(horario)    

    def getProfesoresByCursada(self, cursada: Cursada, profesores: List[Profesor]):
        profesoresOpcionales = list()
        for profesor in profesores:
            cursadaProfesor=profesor.getCursada(cursada.materia.nombre,cursada.curso.nombre)
            if cursadaProfesor != None:
                profesoresOpcionales.append(profesor) 
        return profesoresOpcionales

    def asignarCursada(self,cursada: Cursada,enviroment: Escenario)->int:
        profesoresOpcionales:List[Profesor]=self.getProfesoresByCursada(cursada, enviroment.profesores)
        cantidadHoras=0
        if len(profesoresOpcionales)>0:
            profesor = random.choice(profesoresOpcionales)
            asignacion = Asignacion(profesor,cursada)
            disponibilidadDia = profesor.disponibilidad[self.fecha.name]            
            if len(disponibilidadDia)>0:
                horaInicio = random.randint(disponibilidadDia[0],disponibilidadDia[1])
                cantidadHoras= random.randint(cursada.horasMinimasCons,cursada.horasMaximasCons)
                horario=Horario(asignacion, (horaInicio, (horaInicio+cantidadHoras)))
                self.horarios.append(horario)
        return cantidadHoras
