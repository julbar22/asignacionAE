from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, TypeVar, Dict, Generic
from frameworkAG.ScheduleUtils import TimeTable

class Recurso():
    recursosVinculados:Dict[str,List[Recurso]]
    identificador:str

    def __init__(self, identificador:str):
        self.identificador=identificador
        self.recursosVinculados = {}

    def addTipoRecursosVinculados(self, tipoRecurso:str):
        if tipoRecurso not in self.recursosVinculados:
            self.recursosVinculados[tipoRecurso]=list()
    
    def addRecursoVinculado(self, tipoRecurso:str, recurso: Recurso):
        self.addTipoRecursosVinculados(tipoRecurso)
        self.recursosVinculados[tipoRecurso].append(recurso)

class RecursoTiempo(Recurso):
    disponibilidad:TimeTable
        

