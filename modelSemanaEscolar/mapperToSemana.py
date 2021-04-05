import datetime
import json
from modelSemanaEscolar.dia import Dia
from typing import List
from marcoGenerico.Entidades import Asignacion

class MapperToSemana():
    
    @staticmethod
    def mapperSemana(datos):
        solucion = sorted(datos,key=lambda asignacion: (asignacion.espacioTiempo.week_day.value, asignacion.espacioTiempo.hour))
        json_data = json.dumps(solucion, skipkeys=True, check_circular=False,
                               default=lambda o: MapperToSemana.json_default(o), indent=4)
        print("--------------------inicio solucion --------------------------")
        print(json_data)
        print("--------------------fin solucion --------------------------")
    

    @staticmethod
    def json_default(value):
        if isinstance(value, Asignacion):
            return {"dia": value.espacioTiempo.week_day.name,
                    "hora": value.espacioTiempo.hour,
                    "materia": value.listaRecursoId[0],
                    "profesor":value.listaRecursoId[1]
            }
        else:
            return value.__dict__