from datetime import date
from modelSemanaEscolar.dia import Dia
from modelSemanaEscolar.asignacion import Asignacion
from modelSemanaEscolar.horario import Horario
import datetime
import json
from enums.diaSemana import DiaSemana
from geneticAlgorithm.individual import Individual
import random
from modelSemanaEscolar.escenario import Escenario
from modelSemanaEscolar.cursada import Cursada
from typing import List


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
        #print("---------fin evaluacion---------")
        # self.imprimirIndividuo()

    def evaluarHorasCursada(self, environment: Escenario):
        for cursada in environment.cursada:
            horasSemanales = 0
            for dia in self.cromosoma:
                horasDia = dia.calcularHorasPorCursada(cursada)
                if horasDia > cursada.horasMaximasCons:
                    self.fitness += 1
                    self.errores.append("> horas diarias "+ cursada.materia.nombre+","+cursada.curso.nombre)
                    #print("muchas horas diarias:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)
                horasSemanales += horasDia
            if horasSemanales != cursada.horasSemanales:
                self.fitness += 1
                self.errores.append("> horas semanales "+ cursada.materia.nombre+","+cursada.curso.nombre)
                #print("muchas horas semanales:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)

    def evaluarDisponibilidadProfesores(self, environment: Escenario):
        for dia in self.cromosoma:
            for horario in dia.horarios:
                profesor = horario.asignacion.profesor
                disponibilidad = profesor.disponibilidad[dia.fecha.name]
                if len(disponibilidad) > 0:
                    if not (disponibilidad[0] <= horario.horario[0] and horario.horario[0] <= disponibilidad[1]) or not(disponibilidad[0] <= horario.horario[1] and horario.horario[1] <= disponibilidad[1]):
                        self.fitness += 1
                        self.errores.append("fuera de disponibilidad"+profesor.nombre+","+dia.fecha.name)
                else:
                    self.fitness += 1
                    self.errores.append("fuera de disponibilidad"+profesor.nombre+","+dia.fecha.name)

    def evaluarClasesPorCurso(self, environment: Escenario):
        for curso in environment.cursos:
            for dia in self.cromosoma:
                horariosDia = dia.getHorariosPorCurso(curso.nombre)
                self.horariosCruzados(horariosDia,"Curso")
               

    def evaluarClasesProfesor(self, environment: Escenario):
        for profesor in environment.profesores:
            for dia in self.cromosoma:
                horariosDia = dia.getHorariosByProfesor(profesor.nombre)
                self.horariosCruzados(horariosDia,"Profesor")

                
    
    def horariosCruzados(self,horariosDia:List[Horario],tipo:str):
        horarios: list =list(map(
                    lambda horarioTemp: horarioTemp.horario, horariosDia))
        for index1 in range(0, len(horarios)-1):
            horario1 = horarios[index1]
            for index2 in range((index1+1), len(horarios)-1):
                horario2 = horarios[index2]
                isCruzado=self.sonHorariosCruzados(horario1,horario2)
                isInterno1=self.contieneHorario(horario1,horario2)
                isInterno2=self.contieneHorario(horario2,horario1)
                if isCruzado or isInterno1 or isInterno2:
                    self.fitness+=1
                    self.errores.append("cruce de horarios tipo "+tipo)


    def sonHorariosCruzados(self, horario1: tuple, horario2: tuple)->bool:
        if(horario1[0] <= horario2[0] and horario1[1] >= horario2[0]) or (horario1[0] <= horario2[1] and horario1[1] >= horario2[1]):
            return True
        return False
    
    def contieneHorario(self, horario1:tuple,horario2:tuple)->bool:
        if(horario1[0]<=horario2[0] and horario1[1]>=horario2[1]):
            return True
        return False

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

    def completarCursadas(self, cursadas: List[Cursada], environment: Escenario):
        for cursada in cursadas:
            horasSemanales = cursada.horasSemanales
            horasAsignadas = 0
            copiaCromosoma = self.cromosoma.copy()
            while horasSemanales > horasAsignadas:
                contador = 0
                diaSeleccionado: Dia = random.choice(copiaCromosoma)
                contador = diaSeleccionado.asignarCursada(cursada, environment)
                horasAsignadas += contador
                if contador == 0:
                    indice = copiaCromosoma.index(diaSeleccionado)
                    copiaCromosoma.pop(indice)

    def printSolucion(self):
        solucionToPrint = {}
        for dia in self.cromosoma:
            solucionToPrint[dia.fecha.name] = []
            for horario in dia.horarios:
                asignacionDia = []
                asignacionDia.append(horario.horario)
                asignacionHorario = horario.asignacion
                asignacionDia.append(asignacionHorario.profesor.nombre)
                asignacionDia.append(asignacionHorario.cursada.materia.nombre)
                asignacionDia.append(asignacionHorario.cursada.curso.nombre)
                solucionToPrint[dia.fecha.name].append(asignacionDia)
        return solucionToPrint

    def json_default(self, value):
        if isinstance(value, datetime.date):
            return dict(year=value.year, month=value.month, day=value.day)
        else:
            if isinstance(value, DiaSemana):
                return value.name
            else:
                return value.__dict__

    def imprimirIndividuo(self):
        solucion = self.printSolucion()
        json_data = json.dumps(solucion, skipkeys=True, check_circular=False,
                               default=lambda o: self.json_default(o), indent=4)
        print("--------------------inicio solucion --------------------------")
        print(json_data)
        print("--------------------fin solucion --------------------------")
