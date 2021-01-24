from modelSemanaEscolar.dia import Dia
from modelSemanaEscolar.asignacion import Asignacion
from modelSemanaEscolar.horario import Horario
from enums.diaSemana import DiaSemana
from geneticAlgorithm.individual import IndividuoTiempo, Individual
import random
from modelSemanaEscolar.escenario import Escenario
from modelSemanaEscolar.cursada import Cursada
from typing import List, Optional, TypeVar, Dict, Generic
from utils.horarioUtils import HorarioUtils
from modelSemanaEscolar.mapperToSemana import MapperToSemana
from modelSemanaEscolar.crossSemanaEscolar.factoryCrossSemana import FactoryCrossSemana
from modelSemanaEscolar.crossSemanaEscolar.crossSemanaEnum import CrossSemanaEnum
from modelSemanaEscolar.crossSemanaEscolar.crossSemana import CrossSemana
import copy
from modelSemanaEscolar.errorSemana import ErrorSemana
from modelSemanaEscolar.profesor import Profesor
from marcoGenerico.Ambiente import AmbienteEspecificoTiempo
from marcoGenerico.Recurso import Recurso, RecursoTiempo
from marcoGenerico.Entidades import Materia, Asignacion
from marcoGenerico.Horarios import TimeTable, TimeSlot


class SemanaEscolar(IndividuoTiempo):

    def __init__(self,ambiente:AmbienteEspecificoTiempo):
        self.ambiente:AmbienteEspecificoTiempo= copy.deepcopy(ambiente)
        self.cromosoma = []
        self.fitness = 0
        self.errores = []
        super(SemanaEscolar,self).__init__(self.ambiente)
        

    def getDia(self, dia: DiaSemana):
        for diaList in self.cromosoma:
            if diaList.fecha.value == dia.value:
                return diaList

    def getSiguienteDia(self, dia: DiaSemana):
        proximoDia = dia.value+1
        return DiaSemana(0) if proximoDia > 6 else DiaSemana(proximoDia)

    def calculateFitness(self):
        self.fitness = 0
        self.errores.clear()
        self.evaluarHorasCursada()

    def evaluarHorasCursada(self):
        for cursada in self.ambiente.recursos["Materia"]:
            asignaciones:List[Asignacion]=self.horario.getAsignacionesByRecurso(cursada.identificador)
            for dia in self.ambiente.horario.week_days():
                asinacionByDia=list(filter(lambda asignacion: asignacion.espacioTiempo.week_day==dia,asignaciones))
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

    def evaluarDisponibilidadProfesores(self, environment: Escenario):
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

    def horariosCruzados(self, horariosDia: List[Horario], tipo: str, dia: DiaSemana):
        horarios: list = list(map(
            lambda horarioTemp: horarioTemp.horario, horariosDia))
        for index1 in range(0, len(horarios)):
            horario1 = horarios[index1]
            for index2 in range((index1+1), len(horarios)):
                horario2 = horarios[index2]
                isCruzado = HorarioUtils.isCrossPoints(horario1, horario2)
                if isCruzado:
                    self.fitness += 1
                    if tipo == "Profesor":
                        error = ErrorSemana(
                            2, horariosDia[index1].asignacion.cursada)
                        error.dia = dia
                    else:
                        error = ErrorSemana(
                            3, horariosDia[index1].asignacion.cursada)
                        error.dia = dia
                    self.errores.append(error)

    def createRamdomIndividual(self, ambienteNuevo: AmbienteEspecificoTiempo) -> Individual:
        nuevo = SemanaEscolar(ambienteNuevo)    
        nuevo.completarCursadas(nuevo.ambiente.recursos["Materia"])
        #nuevo.calculateFitness(individualBase, environment)
        # nuevo.imprimirIndividuo()
        return nuevo

    def mutate(self, index, environment:AmbienteEspecificoTiempo) -> Individual:
        nuevo:IndividuoTiempo = self.createRamdomIndividual(environment)
        indexAsignacion:int= random.randint(0,len(self.horario.datos)-1)
        asignacionNueva:Asignacion = copy.deepcopy(nuevo.horario.datos[indexAsignacion])
        self.horario.datos[indexAsignacion]= asignacionNueva
        self.horario.datosPorEspacio[asignacionNueva.espacioTiempo]=asignacionNueva
        return self

    def improvement(self, environment: Escenario) -> Individual:
        self.correccionErroresAleatorios(environment)

    def cross(self, couple: IndividuoTiempo,ambienteNuevo: AmbienteEspecificoTiempo) -> List[Individual]:
        nuevaSemana1: SemanaEscolar = SemanaEscolar(ambienteNuevo)
        nuevaSemana2: SemanaEscolar = SemanaEscolar(ambienteNuevo)

        for time in self.horario.datosPorEspacio:
            if random.uniform(0.0,1.0)<=0.5:
                asignacionNueva1:Asignacion =self.horario.datosPorEspacio[time]
                nuevaSemana1.agregarAsignacionCross(asignacionNueva1)

                asignacionNueva2:Asignacion=couple.horario.datosPorEspacio[time]
                nuevaSemana2.agregarAsignacionCross(asignacionNueva2)
            else:
                asignacionNueva2:Asignacion =self.horario.datosPorEspacio[time]
                nuevaSemana2.agregarAsignacionCross(asignacionNueva2)

                asignacionNueva1:Asignacion=couple.horario.datosPorEspacio[time]
                nuevaSemana1.agregarAsignacionCross(asignacionNueva1)

        semanas: list = []
        semanas.append(nuevaSemana1)
        semanas.append(nuevaSemana2)
        return semanas

    def agregarAsignacionCross(self, asignacionNueva:Asignacion):       
        self.horario.agregarAsignacion(asignacionNueva.espacioTiempo, copy.deepcopy(asignacionNueva))
        materia:Materia= self.ambiente.getRecursoPorTipoAndID("Materia",asignacionNueva.listaRecursoId[0])
        profesor:RecursoTiempo=materia.recursosVinculados["Profesor"][0]
        profesor.disponibilidad._open_slots.remove(asignacionNueva.espacioTiempo)

    def completarCursadas(self, cursadas:List[Materia]):
        #cursadas.sort(key=lambda cursada: cursada.horasSemanales, reverse=True)
        contadorCursada = 0
        while(contadorCursada < len(cursadas)):
            cursada:Materia = cursadas[contadorCursada]
            contadorCursada += 1
            horasSemanales = cursada.horasSemanales
            horasAsignadas = 0
            while horasSemanales > horasAsignadas:
                profesor:RecursoTiempo=cursada.recursosVinculados["Profesor"][0]
                horarioDisponible:TimeTable = profesor.disponibilidad.intersection(self.horario.horario)
                time:Optional[TimeSlot]= horarioDisponible.any_time_slot()
                nuevaAsignacion: Asignacion = Asignacion()
                nuevaAsignacion.espacioTiempo= time
                nuevaAsignacion.listaRecursoId.append(cursada.identificador)
                nuevaAsignacion.listaRecursoId.append(profesor.identificador)
                self.horario.agregarAsignacion(time,nuevaAsignacion)
                profesor.disponibilidad._open_slots.remove(time)
                horasAsignadas+=1

    def imprimirIndividuo(self):
        MapperToSemana.mapperSemana(self.horario.datos)

    def imprimirErrores(self):
        for error in self.errores:
            if isinstance(error, ErrorSemana):
                error.printError()
            else:
                print(error)

    def correccionErroresAleatorios(self, environment: Escenario):
        if len(self.errores) > 0:
            error: ErrorSemana = random.choice(self.errores)
            if isinstance(error, ErrorSemana):
                if error.tipoError == 0:
                    if error.horasSemanales > error.horasAsignadas:
                        cursada:Materia = error.cursada
                    else:
                        if error.horasSemanales < error.horasAsignadas:
                            cursada = error.cursada
                elif error.tipoError == 1:
                    self.asignacionDiaria(error, environment)
                elif error.tipoError == 2:
                    diaTemp = error.dia

    def asignacionDiaria(self, error: ErrorSemana, environment: Escenario):
        cursada = error.cursada
        #profesor:Profesor = environment.getProfesoresByCursada(cursada)[0]
        if error.horasSemanales > error.horasAsignadas:
            dia: Dia = self.getDia(error.dia)
            dia.replaceAleatoriaCursada(cursada, environment)
            error.horasAsignadas += 1
        else:
            if error.horasSemanales < error.horasAsignadas:
                dia: Dia = self.getDia(error.dia)
                dia.removerCursada(cursada, environment)
                error.horasAsignadas -= 1
