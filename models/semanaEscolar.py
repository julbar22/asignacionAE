from datetime import date
from models.dia import Dia
from models.asignacion import Asignacion
from models.horario import Horario
import datetime
import json
from enums.diaSemana import DiaSemana
from geneticAlgorithm.individual import Individual
import random
from escenario import Escenario
from models.cursada import Cursada
from typing import List


class SemanaEscolar(Individual):

    def __init__(self, initDate: DiaSemana, endDate: DiaSemana):
        self.cromosoma = []
        self.fitness = 0
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

    def calculateFitness(self, individual: Individual, enviroment: Escenario):
        # disponibilidad de los profesores diaria ya
        # cantidad de horas semanales ya
        # cantidad de horas por dia ya
        # 2 clases en el curso al mismo momento
        # 2 clases en el mismo momento para el profesor
        # que falten cursadas en la semana
        self.fitness=0
        #print("---------evaluacion--------")
        for cursada in enviroment.cursada:
            horasSemanales = 0            
            for dia in self.cromosoma:
                horasDia = 0
                for horario in dia.horarios:
                    cursadaTemp = horario.asignacion.cursada
                    if cursadaTemp.curso.nombre == cursada.curso.nombre and cursadaTemp.materia.nombre == cursada.materia.nombre:
                        horasDia += (horario.horario[1]-horario.horario[0])                        
                if horasDia > cursada.horasMaximasCons:
                    self.fitness += 1
                    #print("muchas horas diarias:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)
                horasSemanales += horasDia
            if horasSemanales != cursada.horasSemanales:
                self.fitness += 1
                #print("muchas horas semanales:"+cursada.materia.nombre+" ,"+cursada.curso.nombre)

        for profesor in enviroment.profesores:
            for dia in self.cromosoma:
                for horario in dia.horarios:
                    cursadaTemp = horario.asignacion.cursada
                    if horario.asignacion.profesor.nombre == profesor.nombre:
                        disponibilidad = profesor.disponibilidad[dia.fecha.name]   
                        if len(disponibilidad)>0:                                              
                            if not (disponibilidad[0] <= horario.horario[0] and horario.horario[0] <= disponibilidad[1]) or not(disponibilidad[0] <= horario.horario[1] and horario.horario[1] <= disponibilidad[1]):
                                self.fitness += 1
                                #print("fuera de disponibilidad"+profesor.nombre+","+dia.fecha.name)
                        else: 
                            self.fitness += 1
        #print("fitness:"+str(self.fitness))
        #print("---------fin evaluacion---------")
        #self.imprimirIndividuo()
        
    

    def createRamdomIndividual(self, individualBase: Individual, enviroment: Escenario):
        diaInicial: Dia = individualBase.cromosoma[0]
        longArray = len(individualBase.cromosoma)
        diaFinal: Dia = individualBase.cromosoma[(longArray-1)]
        nuevo = SemanaEscolar(diaInicial.fecha, diaFinal.fecha)
        nuevo.completarCursadas(enviroment.cursada, enviroment)
        nuevo.calculateFitness(individualBase,enviroment)
        #nuevo.imprimirIndividuo()
        return nuevo

    def mutate(self, index,enviroment):
        #diaCompleto:Dia= self.cromosoma[index]
        nuevo =self.createRamdomIndividual(self,enviroment)
        #diaCompleto2:Dia= nuevo.cromosoma[index]
        #diaCompleto.horarios=diaCompleto2.horarios.copy()
        self.cromosoma[index]= nuevo.cromosoma[index]

        return self


    def completarCursadas(self, cursadas: List[Cursada], enviroment: Escenario):
        for cursada in cursadas:
            horasSemanales = cursada.horasSemanales
            horasAsignadas = 0
            copiaCromosoma =self.cromosoma.copy()
            while horasSemanales > horasAsignadas:
                contador = 0
                diaSeleccionado: Dia = random.choice(copiaCromosoma)
                contador = diaSeleccionado.asignarCursada(cursada, enviroment)
                horasAsignadas += contador
                if contador==0:
                    indice=copiaCromosoma.index(diaSeleccionado)
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
