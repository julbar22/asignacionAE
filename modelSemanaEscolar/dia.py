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
from utils.horarioUtils import HorarioUtils


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
                horarioAsignacion: tuple = self.getPosibleHorario(
                    cursada, disponibilidadDia,profesor.nombre)
                cantidadHoras = horarioAsignacion[1]-horarioAsignacion[0]
                horario = Horario(asignacion, horarioAsignacion)
                self.horarios.append(horario)
        return cantidadHoras

    def getPosibleHorario(self, cursada: Cursada, disponibilidadProfesor: tuple,nombreProfesor:str) -> tuple:
        isCross: bool = True
        oportunidades: int = 0
        horariosCurso: List[Horario] = self.getHorariosPorCurso(cursada.curso.nombre)
        horariosProfesor:List[Horario]= self.getHorariosByProfesor(nombreProfesor)
        while isCross:            
            horaInicio = disponibilidadProfesor[0]
            horaInicio+=oportunidades
            oportunidades+=1
            horasDisponibles = disponibilidadProfesor[1]-horaInicio
            if horasDisponibles>0:
                horasMaximas = cursada.horasMaximasCons if cursada.horasMaximasCons <= horasDisponibles else horasDisponibles
                cantidadHoras = random.randint(
                    cursada.horasMinimasCons, horasMaximas)
                horarioPropuesto = tuple((horaInicio, (horaInicio+cantidadHoras)))
                if len(horariosCurso)>0 or len(horariosProfesor)>0:                    
                    crossCurso=self.isCroosHorarios(horariosCurso,horarioPropuesto)
                    crossProfe=self.isCroosHorarios(horariosProfesor,horarioPropuesto)
                    isCross = crossCurso or crossProfe
                else:
                    isCross=False
            else:
                horarioPropuesto=tuple((0,0))
                break

        return horarioPropuesto

    def isCroosHorarios(self, horarios:List[Horario], horarioPropuesto:tuple)->bool:
        isCross=False
        for horario in horarios:
            isCross = HorarioUtils.isCrossPoints(horarioPropuesto, horario.horario)
            if isCross:
                break
        return isCross
    
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
