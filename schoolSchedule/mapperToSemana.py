import datetime
import json
from typing import List
from frameworkAG.Entities import Assignment

class MapperToSemana():
    
    @staticmethod
    def mapperSemana(data):
        solucion = sorted(data,key=lambda assignment: (assignment.slot.week_day.value, assignment.slot.hour))
        json_data = json.dumps(solucion, skipkeys=True, check_circular=False,
                               default=lambda o: MapperToSemana.json_default(o), indent=4)
        print("--------------------inicio solucion --------------------------")
        print(json_data)
        print("--------------------fin solucion --------------------------")
    

    @staticmethod
    def json_default(value):
        if isinstance(value, Assignment):
            return {"day": value.slot.week_day.name,
                    "hour": value.slot.hour,
                    "subject": value.listResourceId[0],
                    "teacher ":value.listResourceId[1]
            }
        else:
            return value.__dict__