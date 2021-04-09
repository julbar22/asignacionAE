from frameworkAG.geneticAlgorithm.individual import IndividuoTiempo, Individual
import random
from typing import List, Optional, TypeVar, Dict, Generic
from schoolSchedule.mapperToSemana import MapperToSemana
import copy
from schoolSchedule.errorSemana import ErrorSemana
from schoolSchedule.profesor import Profesor
from frameworkAG.Environments import AmbienteEspecificoTiempo
from frameworkAG.Resources import Recurso, RecursoTiempo
from frameworkAG.Entities import Asignacion
from frameworkAG.ScheduleUtils import TimeTable, TimeSlot
from schoolSchedule.resourcesSemana import Materia


class SemanaEscolar(IndividuoTiempo):

    def __init__(self, environment: AmbienteEspecificoTiempo):
        self.environment: AmbienteEspecificoTiempo = copy.deepcopy(environment)
        self.cromosoma = []
        self.fitness = 0
        self.errores = []
        super(SemanaEscolar, self).__init__(self.environment)

    def calculateFitness(self):
        self.fitness = 0
        self.errores.clear()
        self.evaluarHorasCursada()

    def evaluarHorasCursada(self):
        for cursada in self.environment.recursos["Materia"]:
            asignaciones: List[Asignacion] = self.horario.getAsignacionesByRecurso(
                cursada.identificador)
            for dia in self.environment.horario.week_days():
                asinacionByDia = list(filter(
                    lambda asignacion: asignacion.espacioTiempo.week_day == dia, asignaciones))
                horasDia = len(asinacionByDia)
                if horasDia > cursada.horasMaximasCons:
                    self.fitness += 1
                    error = ErrorSemana(1, cursada)
                    error.dia = dia
                    error.horasAsignadas = horasDia
                    error.horasSemanales = cursada.horasMaximasCons
                    self.errores.append(error)
            if cursada.horasSemanales != len(asignaciones):
                error = ErrorSemana(0, cursada)
                error.horasAsignadas = len(asignaciones)
                error.horasSemanales = cursada.horasSemanales
                self.fitness += abs(cursada.horasSemanales-len(asignaciones))
                self.errores.append(error)

    def evaluarDisponibilidadProfesores(self, environment):
        for dia in self.cromosoma:
            for horario in dia.horarios:
                profesor = horario.asignacion.profesor
                disponibilidad = profesor.disponibilidad[dia.fecha.name]
                if len(disponibilidad) > 0:
                    if not (disponibilidad[0] <= horario.horario[0] and horario.horario[0] <= disponibilidad[1]) or not(disponibilidad[0] <= horario.horario[1] and horario.horario[1] <= disponibilidad[1]):
                        self.fitness += 1
                        self.errores.append(
                            "fuera de disponibilidad"+profesor.nombre+","+dia.fecha.name)
                else:
                    self.fitness += 1
                    self.errores.append(
                        "fuera de disponibilidad"+profesor.nombre+","+dia.fecha.name)

    def createRamdomIndividual(self, ambienteNuevo: AmbienteEspecificoTiempo) -> Individual:
        nuevo = SemanaEscolar(ambienteNuevo)
        nuevo.completarCursadas(nuevo.environment.recursos["Materia"])
        #nuevo.calculateFitness(individualBase, environment)
        # nuevo.printIndividual()
        return nuevo

    def mutate(self, index, environment: AmbienteEspecificoTiempo) -> Individual:
        nuevo: IndividuoTiempo = self.createRamdomIndividual(environment)
        indexAsignacion: int = random.randint(0, len(self.horario.datos)-1)
        if indexAsignacion in nuevo.horario.datos:
            asignacionNueva: Asignacion = copy.deepcopy(
                nuevo.horario.datos[indexAsignacion])
            self.horario.datos[indexAsignacion] = asignacionNueva
            self.horario.datosPorEspacio[asignacionNueva.espacioTiempo] = asignacionNueva
        return self

    def improvement(self, environment) -> Individual:
        self.correccionErroresAleatorios(environment)

    def cross(self, couple: IndividuoTiempo, ambienteNuevo: AmbienteEspecificoTiempo) -> List[Individual]:
        nuevaSemana1: SemanaEscolar = SemanaEscolar(ambienteNuevo)
        nuevaSemana2: SemanaEscolar = SemanaEscolar(ambienteNuevo)

        for time in self.horario.datosPorEspacio:
            if random.uniform(0.0, 1.0) <= 0.5:
                if time in self.horario.datosPorEspacio:
                    asignacionNueva1: Asignacion = self.horario.datosPorEspacio[time]
                    nuevaSemana1.agregarAsignacionCross(asignacionNueva1)
                if time in couple.horario.datosPorEspacio:
                    asignacionNueva2: Asignacion = couple.horario.datosPorEspacio[time]
                    nuevaSemana2.agregarAsignacionCross(asignacionNueva2)
            else:
                if time in self.horario.datosPorEspacio:
                    asignacionNueva2: Asignacion = self.horario.datosPorEspacio[time]
                    nuevaSemana2.agregarAsignacionCross(asignacionNueva2)
                if time in couple.horario.datosPorEspacio:
                    asignacionNueva1: Asignacion = couple.horario.datosPorEspacio[time]
                    nuevaSemana1.agregarAsignacionCross(asignacionNueva1)

        semanas: list = []
        semanas.append(nuevaSemana1)
        semanas.append(nuevaSemana2)
        return semanas

    def agregarAsignacionCross(self, asignacionNueva: Asignacion):
        self.horario.agregarAsignacion(
            asignacionNueva.espacioTiempo, copy.deepcopy(asignacionNueva))
        materia: Materia = self.environment.getRecursoPorTipoAndID(
            "Materia", asignacionNueva.listaRecursoId[0])
        profesor: RecursoTiempo = materia.recursosVinculados["Profesor"][0]
        profesor.disponibilidad._open_slots.remove(
            asignacionNueva.espacioTiempo)

    def completarCursadas(self, cursadas: List[Materia]):
        #cursadas.sort(key=lambda cursada: cursada.horasSemanales, reverse=True)
        contadorCursada = 0
        while(contadorCursada < len(cursadas)):
            cursada: Materia = cursadas[contadorCursada]
            contadorCursada += 1
            horasSemanales = cursada.horasSemanales
            horasAsignadas = 0
            while horasSemanales > horasAsignadas:
                profesor: RecursoTiempo = cursada.recursosVinculados["Profesor"][0]
                horarioDisponible: TimeTable = profesor.disponibilidad.intersection(
                    self.horario.horario)
                time: Optional[TimeSlot] = horarioDisponible.any_time_slot()
                if time is not None:
                    nuevaAsignacion: Asignacion = Asignacion()
                    nuevaAsignacion.espacioTiempo = time
                    nuevaAsignacion.listaRecursoId.append(
                        cursada.identificador)
                    nuevaAsignacion.listaRecursoId.append(
                        profesor.identificador)
                    self.horario.agregarAsignacion(time, nuevaAsignacion)
                    profesor.disponibilidad._open_slots.remove(time)
                    horasAsignadas += 1
                else:
                    break

    def printIndividual(self):
        MapperToSemana.mapperSemana(self.horario.datos)

    def imprimirErrores(self):
        for error in self.errores:
            if isinstance(error, ErrorSemana):
                error.printError()
            else:
                print(error)

    def correccionErroresAleatorios(self, environment):
        if len(self.errores) > 0:
            error: ErrorSemana = random.choice(self.errores)
            if isinstance(error, ErrorSemana):
                if error.tipoError == 0:
                    if error.horasSemanales > error.horasAsignadas:
                        cursada: Materia = error.cursada
                    else:
                        if error.horasSemanales < error.horasAsignadas:
                            cursada = error.cursada
                elif error.tipoError == 1:
                    self.asignacionDiaria(error, environment)
                elif error.tipoError == 2:
                    diaTemp = error.dia

    def asignacionDiaria(self, error: ErrorSemana, environment):
        cursada = error.cursada
        #profesor:Profesor = environment.getProfesoresByCursada(cursada)[0]
        # if error.horasSemanales > error.horasAsignadas:
        #     dia: Dia = self.getDia(error.dia)
        #     dia.replaceAleatoriaCursada(cursada, environment)
        #     error.horasAsignadas += 1
        # else:
        #     if error.horasSemanales < error.horasAsignadas:
        #         dia: Dia = self.getDia(error.dia)
        #         dia.removerCursada(cursada, environment)
        #         error.horasAsignadas -= 1
