from modelSemanaEscolar.crossSemanaEscolar.crossSemana import CrossSemana
from modelSemanaEscolar.dia import Dia
from typing import List
import random

class CrossSemanaDiaCompleto(CrossSemana):

    def croosRun(self, semana1:List[Dia], semana2:List[Dia])->List[List[Dia]]:
        diasNuevaSemana1:List[Dia]= list()
        diasNuevaSemana2:List[Dia]= list()
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
   