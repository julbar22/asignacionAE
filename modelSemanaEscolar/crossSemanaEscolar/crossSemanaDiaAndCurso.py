from modelSemanaEscolar.crossSemanaEscolar.crossSemana import CrossSemana
from modelSemanaEscolar.dia import Dia
from typing import List
import random
from modelSemanaEscolar.horario import Horario


class CrossSemanaDiaAndCurso(CrossSemana):

    def croosRun(self, semana1: List[Dia], semana2: List[Dia]) -> List[List[Dia]]:
        diasNuevaSemana1: List[Dia] = list()
        diasNuevaSemana2: List[Dia] = list()
        for index in range(len(semana1)):
            dia1: Dia = semana1[index]
            dia2: Dia = semana2[index]
            dias: list = self.crossDia(dia1, dia2).copy()
            diasNuevaSemana1.append(dias[0])
            diasNuevaSemana2.append(dias[1])
        semanas: List[List[Dia]] = list()
        semanas.append(diasNuevaSemana1)
        semanas.append(diasNuevaSemana2)
        return semanas

    def crossDia(self, dia1: Dia, dia2: Dia) -> List[List[Dia]]:
        dias =[]
        dia1Curso = dia1.getDiaByCurso()
        dia2Curso = dia2.getDiaByCurso()
        newHorariosDia1 = list()
        newHorariosDia2 = list()
        keys = list()
        for key in dia1Curso:
            if not key in keys:
                keys.append(key)
        for key in dia2Curso:
            if not key in keys:
                keys.append(key)

        for key in keys:
            horario1Temp = [] if not key in dia1Curso else dia1Curso[key]
            horario2Temp = [] if not key in dia2Curso else dia2Curso[key]
            horariosTemp = self.crossHorarios(horario1Temp, horario2Temp)
            newHorariosDia1.extend(horariosTemp[0])
            newHorariosDia2.extend(horariosTemp[1])
        diaNuevo1 = Dia(dia1.fecha)
        diaNuevo1.horarios = newHorariosDia1.copy()
        diaNuevo2= Dia(dia2.fecha)
        diaNuevo2.horarios = newHorariosDia2.copy()
        dias.append(diaNuevo1)
        dias.append(diaNuevo2)
        return dias


    def crossHorarios(self, horario1: List[Horario], horario2: List[Horario]) -> List[List[Horario]]:
        #TODO las horas no deben estar fijas
        horarioInicio: int = 7
        horarioFinal: int = 13
        horarioSemana1 = list()
        horarioSemana2 = list()

        while(horarioInicio < horarioFinal):
            posibleHorario1 = self.buscarHorarioHoraInicio(
                horario1, horarioInicio)
            posibleHorario2 = self.buscarHorarioHoraInicio(
                horario2, horarioInicio)
            horarioInicio+=1
            if random.uniform(0, 1) >= 0.5:
                if(posibleHorario1 != None):
                    horarioSemana1.append(posibleHorario1)
                if(posibleHorario2 != None):
                    horarioSemana2.append(posibleHorario2)
            else:
                if(posibleHorario1 != None):
                    horarioSemana2.append(posibleHorario1)
                if(posibleHorario2 != None):
                    horarioSemana1.append(posibleHorario2)

        horariosCompletos = list()
        horariosCompletos.append(horarioSemana1)
        horariosCompletos.append(horarioSemana2)
        return horariosCompletos

    def buscarHorarioHoraInicio(self, horarios: List[Horario], horaInicio: int) -> Horario:
        horariosNuevos= list(filter(lambda horarioAsignado: horarioAsignado.horario[0] == horaInicio, horarios))
        return None if len(horariosNuevos)<=0 else horariosNuevos[0]


