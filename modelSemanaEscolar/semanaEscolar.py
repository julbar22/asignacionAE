from modelSemanaEscolar.dia import Dia
from modelSemanaEscolar.asignacion import Asignacion
from modelSemanaEscolar.horario import Horario
from enums.diaSemana import DiaSemana
from geneticAlgorithm.individual import Individual
import random
from modelSemanaEscolar.escenario import Escenario
from modelSemanaEscolar.cursada import Cursada
from typing import List
from utils.horarioUtils import HorarioUtils
from modelSemanaEscolar.mapperToSemana import MapperToSemana
from modelSemanaEscolar.crossSemanaEscolar.factoryCrossSemana import FactoryCrossSemana
from modelSemanaEscolar.crossSemanaEscolar.crossSemanaEnum import CrossSemanaEnum
from modelSemanaEscolar.crossSemanaEscolar.crossSemana import CrossSemana
import copy
from modelSemanaEscolar.errorSemana import ErrorSemana
from modelSemanaEscolar.profesor import Profesor


class SemanaEscolar(Individual):

    def __init__(self, initDate: DiaSemana, endDate: DiaSemana):
        self.cromosoma = []
        self.fitness = 0
        self.errores = []
        while endDate.value >= initDate.value:
            self.cromosoma.append(Dia(initDate))
            initDate = self.getSiguienteDia(initDate)

    def getDia(self, dia: DiaSemana):
        for diaList in self.cromosoma:
            if diaList.fecha.value == dia.value:
                return diaList

    def getSiguienteDia(self, dia: DiaSemana):
        proximoDia = dia.value+1
        return DiaSemana(0) if proximoDia > 6 else DiaSemana(proximoDia)

    def calculateFitness(self, individual: Individual, environment: Escenario):
        self.fitness = 0
        self.errores.clear()
        # print("---------evaluacion--------")
        # cantidad de horas semanales y diarias
        self.evaluarHorasCursada(environment)
        # disponibilidad de los profesores diaria
        self.evaluarDisponibilidadProfesores(environment)
        # 2 clases en el curso al mismo momento
        self.evaluarClasesPorCurso(environment)
        # 2 clases en el mismo momento para el profesor
        self.evaluarClasesProfesor(environment)
        # print("fitness:"+str(self.fitness))
        # print("---------fin evaluacion---------")
        # self.imprimirIndividuo()

    def evaluarHorasCursada(self, environment: Escenario):
        for cursada in environment.cursada:
            horasSemanales = 0
            for dia in self.cromosoma:
                horasDia = dia.calcularHorasPorCursada(cursada)
                if horasDia > cursada.horasMaximasCons:
                    self.fitness += 1
                    error = ErrorSemana(1)
                    error.dia = dia.fecha
                    error.horasAsignadas = horasDia
                    error.horasSemanales = cursada.horasMaximasCons
                    error.materia = cursada.materia.nombre
                    error.curso = cursada.curso.nombre
                    self.errores.append(error)
                    # print("muchas horas diarias:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)
                horasSemanales += horasDia
            if horasSemanales != cursada.horasSemanales:
                error = ErrorSemana(0)
                error.dia = dia.fecha
                error.horasAsignadas = horasSemanales
                error.horasSemanales = cursada.horasSemanales
                error.materia = cursada.materia.nombre
                error.curso = cursada.curso.nombre
                self.fitness += abs(cursada.horasSemanales-horasSemanales)
                self.errores.append(error)
                # print("muchas horas semanales:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)

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

    def evaluarClasesPorCurso(self, environment: Escenario):
        for curso in environment.cursos:
            for dia in self.cromosoma:
                horariosDia = dia.getHorariosPorCurso(curso.nombre)
                self.horariosCruzados(
                    horariosDia, "Curso:"+dia.fecha.name+":"+curso.nombre)

    def evaluarClasesProfesor(self, environment: Escenario):
        for profesor in environment.profesores:
            for dia in self.cromosoma:
                horariosDia = dia.getHorariosByProfesor(profesor.nombre)
                self.horariosCruzados(horariosDia, "Profesor")

    def horariosCruzados(self, horariosDia: List[Horario], tipo: str):
        horarios: list = list(map(
            lambda horarioTemp: horarioTemp.horario, horariosDia))
        for index1 in range(0, len(horarios)):
            horario1 = horarios[index1]
            for index2 in range((index1+1), len(horarios)):
                horario2 = horarios[index2]
                isCruzado = HorarioUtils.isCrossPoints(horario1, horario2)
                if isCruzado:
                    self.fitness += 1
                    self.errores.append("cruce de horarios tipo "+tipo)

    def createRamdomIndividual(self, individualBase: Individual, environment: Escenario):
        diaInicial: Dia = individualBase.cromosoma[0]
        longArray = len(individualBase.cromosoma)
        diaFinal: Dia = individualBase.cromosoma[(longArray-1)]
        nuevo = SemanaEscolar(diaInicial.fecha, diaFinal.fecha)
        nuevo.completarCursadas(environment.cursada, environment)
        nuevo.calculateFitness(individualBase, environment)
        # nuevo.imprimirIndividuo()
        return nuevo

    def mutate(self, index, environment):
        self.mutacionErroresAleatorios(environment)
        # nuevo = self.createRamdomIndividual(self, environment)
        # self.cromosoma[index] = nuevo.cromosoma[index]
        return self

    def cross(self, couple: Individual) -> List[Individual]:
        coupleSemana: SemanaEscolar = copy.copy(couple)
        compleSemana2: SemanaEscolar = copy.copy(self)
        initDate = self.cromosoma[0].fecha
        endDate = self.cromosoma[4].fecha
        nuevaSemana1: SemanaEscolar = SemanaEscolar(initDate, endDate)
        nuevaSemana2: SemanaEscolar = SemanaEscolar(initDate, endDate)
        factoryCross: FactoryCrossSemana = FactoryCrossSemana()
        crossSemana: CrossSemana = factoryCross.getCrossSemana(
            CrossSemanaEnum.croosDiaAndCurso)
        diasCruzados: List[List[Dia]] = crossSemana.croosRun(
            compleSemana2.cromosoma.copy(), coupleSemana.cromosoma.copy())
        nuevaSemana1.cromosoma = diasCruzados[0].copy()
        nuevaSemana2.cromosoma = diasCruzados[1].copy()
        semanas: list = []
        semanas.append(nuevaSemana1)
        semanas.append(nuevaSemana2)
        return semanas

    def completarCursadas(self, cursadas: List[Cursada], environment: Escenario):

        cursadas.sort(key=lambda cursada: cursada.horasSemanales, reverse=True)
        contadorCursada =0
        while(contadorCursada<len(cursadas)):            
            cursada = cursadas[contadorCursada]
            contadorCursada+=1
            horasSemanales = cursada.horasSemanales
            horasAsignadas = 0
            copiaCromosoma = self.cromosoma.copy()
            while horasSemanales > horasAsignadas:
                contador = 0
                if len(copiaCromosoma) > 0:
                    diaSeleccionado: Dia = random.choice(copiaCromosoma)
                    contador = diaSeleccionado.asignarCursada(
                        cursada, environment, horasSemanales-horasAsignadas)
                    horasAsignadas += contador
                    if contador == 0:
                        indice = copiaCromosoma.index(diaSeleccionado)
                        copiaCromosoma.pop(indice)
                else:
                    break
            #copiaCursadas.remove(cursada)

    def imprimirIndividuo(self):
        MapperToSemana.mapperSemana(self.cromosoma)

    def imprimirErrores(self):
        for error in self.errores:
            if isinstance(error,ErrorSemana):
                error.printError()
            else:
                print(error)

    def mutacionErroresAleatorios(self, environment: Escenario):
        if len(self.errores)>0:        
            error: ErrorSemana = random.choice(self.errores)
            if isinstance(error,ErrorSemana):
                if error.tipoError == 0:
                    if error.horasSemanales > error.horasAsignadas:
                        cursada = environment.getCursada(error.materia, error.curso)
                        profesor:Profesor = environment.getProfesoresByCursada(cursada)[0]
                        diasPosibles:List[Dia]= list(filter(lambda dia: dia.cursadaIsPosible(cursada,profesor),self.cromosoma)) 
                        if len(diasPosibles)>0:                                         
                            dia: Dia = random.choice(diasPosibles)
                            asignacionOld:Asignacion=dia.replaceCursada(cursada, profesor)
                            if(asignacionOld!=None):
                                for diaAsignacionOld in self.cromosoma:
                                    horasAgregadas:int=diaAsignacionOld.asignarCursada(asignacionOld.cursada,environment,1)
                                    if horasAgregadas>0:
                                        break
                            error.horasAsignadas += 1
                    else:
                        if error.horasSemanales < error.horasAsignadas:
                            cursada = environment.getCursada(
                                error.materia, error.curso)
                            dia: Dia = random.choice(self.cromosoma)
                            dia.removerCursada(cursada, environment)
                            error.horasAsignadas -= 1
                if error.tipoError == 1:
                    self.asignacionDiaria(error,environment)

    def asignacionDiaria(self, error:ErrorSemana, environment: Escenario):
        cursada = environment.getCursada(error.materia, error.curso)
        profesor:Profesor = environment.getProfesoresByCursada(cursada)[0]
        if error.horasSemanales > error.horasAsignadas:            
            dia: Dia = self.getDia(error.dia)
            dia.replaceAleatoriaCursada(cursada, environment)
            error.horasAsignadas += 1
        else:
            if error.horasSemanales < error.horasAsignadas:
                dia: Dia = self.getDia(error.dia)
                dia.removerCursada(cursada, environment)
                error.horasAsignadas -= 1
