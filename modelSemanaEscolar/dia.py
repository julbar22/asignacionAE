from modelSemanaEscolar.horario import Horario
from datetime import date
from enums.diaSemana import DiaSemana
from modelSemanaEscolar.escenario import Escenario
import random
from typing import List
from modelSemanaEscolar.materia import Materia
from modelSemanaEscolar.profesor import Profesor
from modelSemanaEscolar.cursada import Cursada
from modelSemanaEscolar.asignacion import Asignacion
from modelSemanaEscolar.horario import Horario


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
            cursadaProfesor = profesor.getCursada(
                cursada.materia.nombre, cursada.curso.nombre)
            if cursadaProfesor != None:
                profesoresOpcionales.append(profesor)
        return profesoresOpcionales

    def asignarCursada(self, cursada: Cursada, environment: Escenario) -> int:
        profesoresOpcionales: List[Profesor] = self.getProfesoresByCursada(
            cursada, environment.profesores)
        cantidadHoras = 0
        if len(profesoresOpcionales) > 0 and not self.cursadaAsignada(cursada):
            profesor = random.choice(profesoresOpcionales)
            asignacion = Asignacion(profesor, cursada)
            disponibilidadDia = profesor.disponibilidad[self.fecha.name]
            if len(disponibilidadDia) > 0:
                horaInicio = random.randint(
                    disponibilidadDia[0], (disponibilidadDia[1]-1))
                horasDisponibles = disponibilidadDia[1]-horaInicio
                horasMaximas = cursada.horasMaximasCons if cursada.horasMaximasCons <= horasDisponibles else horasDisponibles
                cantidadHoras = random.randint(
                    cursada.horasMinimasCons, horasMaximas)
                horario = Horario(
                    asignacion, (horaInicio, (horaInicio+cantidadHoras)))
                self.horarios.append(horario)
        return cantidadHoras

    def calcularHorasPorCursada(self, cursada: Cursada) -> int:
        horasDia: int = 0
        for horario in self.horarios:
            cursadaTemp = horario.asignacion.cursada
            if cursadaTemp.curso.nombre == cursada.curso.nombre and cursadaTemp.materia.nombre == cursada.materia.nombre:
                horasDia += (horario.horario[1]-horario.horario[0])
        return horasDia

    def getHorariosPorCurso(self, nombreCurso: str) -> List[Horario]:
        horarios = []
        for horario in self.horarios:
            cursadaTemp: Cursada = horario.asignacion.cursada
            if cursadaTemp.curso.nombre == nombreCurso:
                horarios.append(horario)
        return horarios

    def getHorariosByProfesor(self, nombreProfesor: str) -> List[Horario]:
        horarios = []
        for horario in self.horarios:
            profesorTemp: Profesor = horario.asignacion.profesor
            if profesorTemp.nombre == nombreProfesor:
                horarios.append(horario)
        return horarios

    def cursadaAsignada(self, cursada: Cursada) -> bool:
        for horario in self.horarios:
            cursadaTemp: Cursada = horario.asignacion.cursada
            if cursadaTemp.curso == cursada.curso and cursadaTemp.materia == cursada.materia:
                return True
        return False
