import datetime
from enums.diaSemana import DiaSemana
import json
from modelSemanaEscolar.dia import Dia
from typing import List

class MapperToSemana():
    
    @staticmethod
    def mapperSemana(dias:List[Dia]):
        solucion = MapperToSemana.printSolucion(dias)
        json_data = json.dumps(solucion, skipkeys=True, check_circular=False,
                               default=lambda o: MapperToSemana.json_default(o), indent=4)
        print("--------------------inicio solucion --------------------------")
        print(json_data)
        print("--------------------fin solucion --------------------------")
    
    @staticmethod
    def printSolucion(dias:List[Dia]):
        solucionToPrint = {}
        for dia in dias:
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

    @staticmethod
    def json_default(value):
        if isinstance(value, datetime.date):
            return dict(year=value.year, month=value.month, day=value.day)
        else:
            if isinstance(value, DiaSemana):
                return value.name
            else:
                return value.__dict__