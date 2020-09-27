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
        # self.evaluarClasesProfesor(environment)
        # print("fitness:"+str(self.fitness))
        #print("---------fin evaluacion---------")
        # self.imprimirIndividuo()

    def evaluarHorasCursada(self, environment: Escenario):
        for cursada in environment.cursada:
            horasSemanales = 0
            for dia in self.cromosoma:
                horasDia = dia.calcularHorasPorCursada(cursada)
                if horasDia > cursada.horasMaximasCons:
                    self.fitness += 1
                    self.errores.append(
                        "> horas diarias " + cursada.materia.nombre+","+cursada.curso.nombre)
                    #print("muchas horas diarias:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)
                horasSemanales += horasDia
            if horasSemanales != cursada.horasSemanales:
                self.fitness += abs(cursada.horasSemanales-horasSemanales)
                self.errores.append("> horas semanales " + cursada.materia.nombre+"," +
                                    cursada.curso.nombre+" "+str(horasSemanales)+"-"+str(cursada.horasSemanales))
                #print("muchas horas semanales:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)

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
                self.horariosCruzados(horariosDia, "Curso:"+dia.fecha.name+":"+curso.nombre)

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
                isCruzado=HorarioUtils.isCrossPoints(horario1,horario2)
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
        #diaCompleto:Dia= self.cromosoma[index]
        nuevo = self.createRamdomIndividual(self, environment)
        #diaCompleto2:Dia= nuevo.cromosoma[index]
        # diaCompleto.horarios=diaCompleto2.horarios.copy()
        self.cromosoma[index] = nuevo.cromosoma[index]

        return self

    def cross(self, couple: Individual) -> List[Individual]:
        coupleSemana: SemanaEscolar = couple
        initDate = self.cromosoma[0].fecha
        endDate = self.cromosoma[4].fecha
        nuevaSemana1: SemanaEscolar = SemanaEscolar(initDate, endDate)
        nuevaSemana2: SemanaEscolar = SemanaEscolar(initDate, endDate)
        for index in range(len(self.cromosoma)):
            dia1: Dia = coupleSemana.cromosoma[index]
            dia2: Dia = self.cromosoma[index]
            dias: list = self.crossDia(dia1, dia2).copy()
            nuevaSemana1.cromosoma[index] = dias[0]
            nuevaSemana2.cromosoma[index] = dias[1]

        semanas: list = []
        semanas.append(nuevaSemana1)
        semanas.append(nuevaSemana2)
        return semanas

    def crossDia(self, dia1: Dia, dia2: Dia) -> List[Dia]:
        diasCruzados = []
        lenDia1 = len(dia1.horarios)
        lenDia2 = len(dia2.horarios)
        diaNuevo1 = Dia(dia1.fecha)
        diaNuevo2 = Dia(dia2.fecha)
        maxHorarios = lenDia1 if lenDia1 >= lenDia2 else lenDia2
        for index in range(maxHorarios):
            if random.uniform(0, 1) >= 0.5:
                if lenDia1 > index:
                    diaNuevo1.addHorario(dia1.horarios[index])
                if lenDia2 > index:
                    diaNuevo2.addHorario(dia2.horarios[index])
            else:
                if lenDia2 > index:
                    diaNuevo1.addHorario(dia2.horarios[index])
                if lenDia1 > index:
                    diaNuevo2.addHorario(dia1.horarios[index])
        diasCruzados.append(diaNuevo1)
        diasCruzados.append(diaNuevo2)
        return diasCruzados

    def completarCursadas(self, cursadas: List[Cursada], environment: Escenario):
        for cursada in cursadas:
            horasSemanales = cursada.horasSemanales
            horasAsignadas = 0
            copiaCromosoma = self.cromosoma.copy()
            while horasSemanales > horasAsignadas:
                contador = 0
                if len(copiaCromosoma)>0:
                    diaSeleccionado: Dia = random.choice(copiaCromosoma)
                    contador = diaSeleccionado.asignarCursada(cursada, environment)
                    horasAsignadas += contador
                    if contador == 0:
                        indice = copiaCromosoma.index(diaSeleccionado)
                        copiaCromosoma.pop(indice)
                else:
                    break

    def imprimirIndividuo(self):
        MapperToSemana.mapperSemana(self.cromosoma)
