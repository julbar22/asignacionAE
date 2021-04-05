from modelSemanaEscolar.horario import Horario
from datetime import date
import random
from typing import List
from modelSemanaEscolar.materia import Materia
from modelSemanaEscolar.profesor import Profesor
from modelSemanaEscolar.cursada import Cursada
from modelSemanaEscolar.asignacion import Asignacion
from modelSemanaEscolar.horario import Horario
from utils.horarioUtils import HorarioUtils


class Dia:

    horarios: List[Horario] = list()

    def __init__(self):
        self.horarios = []
        self.horasByCursada = {}
        self.horariosByCurso = {}

    def addHorario(self, horario: Horario):
        self.horarios.append(horario)

    def asignarCursada(self, cursada: Cursada, environment, horasCursadaFaltates: int) -> int:
        profesoresOpcionales: List[Profesor] = environment.getProfesoresByCursada(
            cursada)
        cantidadHoras = 0
        if len(profesoresOpcionales) > 0 and not self.cursadaAsignada(cursada):
            profesor = random.choice(profesoresOpcionales)
            asignacion = Asignacion(profesor, cursada)
            disponibilidadDia = profesor.disponibilidad[self.fecha.name]
            if len(disponibilidadDia) > 0:
                horarioAsignacion: tuple = self.getPosibleHorario(
                    asignacion, horasCursadaFaltates)
                cantidadHoras = self.addHorarioAsignado(
                    horarioAsignacion, asignacion)
        return cantidadHoras

    def addHorarioAsignado(self, horarioAsignacion: tuple, asignacion: Asignacion) -> int:
        cantidadHoras = horarioAsignacion[1]-horarioAsignacion[0]
        for contHoras in range(cantidadHoras):
            horarioTemp: tuple = tuple(
                (horarioAsignacion[0]+contHoras, (horarioAsignacion[0]+1)+contHoras))
            horario: Horario = Horario(asignacion, horarioTemp)
            self.horarios.append(horario)
        return cantidadHoras

    def getPosibleHorario(self, asignacion: Asignacion, horasFaltantes: int) -> tuple:
        cursada: Cursada = asignacion.cursada
        disponibilidadProfesor: tuple = asignacion.profesor.disponibilidad[self.fecha.name]
        nombreProfesor: str = asignacion.profesor.nombre
        isCross: bool = True
        contHoras: int = 0
        horariosCurso: List[Horario] = self.getHorariosPorCurso(
            cursada.curso.nombre)
        horariosProfesor: List[Horario] = self.getHorariosByProfesor(
            nombreProfesor)
        while isCross:
            horaInicio = disponibilidadProfesor[0]
            horaInicio += contHoras
            contHoras += 1
            horasDisponibles = disponibilidadProfesor[1]-horaInicio
            if horasDisponibles > 0:
                horasMaximas = HorarioUtils.getMenorValor(
                    cursada.horasMaximasCons, horasDisponibles)
                horasMaximas = HorarioUtils.getMenorValor(
                    horasMaximas, horasFaltantes)
                cantidadHoras = random.randint(
                    cursada.horasMinimasCons, horasMaximas)
                horarioPropuesto = tuple(
                    (horaInicio, (horaInicio+cantidadHoras)))
                if len(horariosCurso) > 0 or len(horariosProfesor) > 0:
                    #isCross = False
                    crossCurso = self.isCroosHorarios(
                        horariosCurso, horarioPropuesto)
                    crossProfe = self.isCroosHorarios(
                        horariosProfesor, horarioPropuesto)
                    isCross = crossCurso or crossProfe
                else:
                    isCross = False
            else:
                horarioPropuesto = tuple((0, 0))
                break

        return horarioPropuesto

    def isCroosHorarios(self, horarios: List[Horario], horarioPropuesto: tuple) -> bool:
        isCross = False
        for horario in horarios:
            isCross = HorarioUtils.isCrossPoints(
                horarioPropuesto, horario.horario)
            if isCross:
                break
        return isCross

    def getHorasPorCursada(self, cursada: Cursada) -> int:
        nombreCursada: str = cursada.curso.nombre+","+cursada.materia.nombre
        if nombreCursada in self.horasByCursada:
            return self.horasByCursada[nombreCursada]
        else:
            return 0

    def calcularHorasPorCursada(self):
        self.horasByCursada = {}
        self.horariosByCurso= {}
        for horario in self.horarios:
            cursadaTemp: Cursada = horario.asignacion.cursada
            nombreCursada: str = cursadaTemp.curso.nombre+","+cursadaTemp.materia.nombre
            if nombreCursada in self.horasByCursada:
                self.horasByCursada[nombreCursada] += 1
            else:
                self.horasByCursada[nombreCursada] = 1

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
        contHoras = 0
        for horario in self.horarios:
            cursadaTemp: Cursada = horario.asignacion.cursada
            if cursadaTemp.curso == cursada.curso and cursadaTemp.materia == cursada.materia:
                contHoras += 1
                if cursada.horasMaximasCons == contHoras:
                    return True
        return False

    def replaceAleatoriaCursada(self, cursada: Cursada, environment) -> Cursada:
        horario: Horario = random.choice(self.horarios)
        profesores = environment.getProfesoresByCursada(cursada)
        newAsignacion: Asignacion = Asignacion(profesores[0], cursada)
        newHorario: Horario = Horario(newAsignacion, tuple(horario.horario))
        self.horarios.remove(horario)
        self.horarios.append(newHorario)
        return horario.asignacion.cursada

    def replaceCursada(self, cursada: Cursada, profesor: Profesor) -> Asignacion:
        newAsignacion: Asignacion = Asignacion(profesor, cursada)
        horarioPosible: tuple = self.getHorarioToReplaceByprofesor(profesor)
        newHorario: Horario = Horario(newAsignacion, horarioPosible)
        horarioOld: Horario = self.getHorarioByHoraAndCurso(
            horarioPosible, cursada.curso.nombre)
        asignacionOld = None
        if isinstance(horarioOld, Horario):
            self.horarios.remove(horarioOld)
            asignacionOld = horarioOld.asignacion
        self.horarios.append(newHorario)
        return asignacionOld

    def getHorarioToReplaceByprofesor(self, profesor: Profesor) -> tuple:
        disponibilidadDia: tuple = profesor.disponibilidad[self.fecha.name]
        horariosProfesor: List[Horario] = self.getHorariosByProfesor(
            profesor.nombre)
        for hora in range(disponibilidadDia[0], disponibilidadDia[1]):
            horarioTemp = list(filter(
                lambda horario: horario.horario[0] == hora, horariosProfesor))
            if len(horarioTemp) == 0:
                return tuple((hora, hora+1))
        return tuple((0, 0))

    def removerCursada(self, cursada: Cursada, environment):
        horarios = self.getHorariosPorCurso(cursada.curso.nombre)
        horarioTemp: Horario = None
        for horario in horarios:
            if horario.asignacion.cursada.materia.nombre == cursada.materia.nombre:
                horarioTemp = horario
                break
        if horarioTemp != None:
            self.horarios.remove(horario)

    def cursadaIsPosible(self, cursada: Cursada, profesor: Profesor):
        horasCursada: int = self.cantidadHorasCursada(cursada)
        disponibilidad: bool = self.tieneDisponibilidadProfesor(profesor)
        return disponibilidad and cursada.horasMaximasCons > horasCursada

    def cantidadHorasCursada(self, cursada) -> int:
        cursadas = list(filter(
            lambda horario: horario.asignacion.cursada.__eq__(cursada), self.horarios))
        return len(cursadas)

    def tieneDisponibilidadProfesor(self, profesor: Profesor) -> bool:
        disponibilidadDia: tuple = profesor.disponibilidad[self.fecha.name]
        if(len(disponibilidadDia) == 0):
            return False
        horariosProfesor: List[Horario] = self.getHorariosByProfesor(
            profesor.nombre)
        for hora in range(disponibilidadDia[0], disponibilidadDia[1]):
            horarioTemp = list(
                filter(lambda horario: horario.horario[0] == hora, horariosProfesor))
            if len(horarioTemp) == 0:
                return True
        return False

    def getHorarioByHoraAndCurso(self, hora: tuple, nombreCurso: str) -> Horario:
        horariosCurso: List[Horario] = self.getHorariosPorCurso(nombreCurso)
        for horario in horariosCurso:
            if horario.horario[0] == hora[0]:
                return horario

    def createDiaByCurso(self):
        self.horarios = self.sortDiaByHorario()
        for horario in self.horarios:
            horarioTemp: Horario = horario
            nombreCurso: str = horarioTemp.asignacion.cursada.curso.nombre
            if nombreCurso in self.horariosByCurso:
                self.horariosByCurso[nombreCurso].append(horario)
            else:
                self.horariosByCurso[nombreCurso] = list()
                self.horariosByCurso[nombreCurso].append(horario)
        return self.horariosByCurso

    def getDiaByCurso(self):
        if len(self.horariosByCurso) > 0:
            return self.horariosByCurso
        else:
            return self.createDiaByCurso()

    def sortDiaByHorario(self):
        if len(self.horarios) > 0 and isinstance(self.horarios[0], Horario):
            self.horarios.sort(
                key=lambda horarioAsignado: horarioAsignado.horario[0])
            return self.horarios.copy()
        else:
            return []
