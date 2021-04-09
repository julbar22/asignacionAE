from typing import List, Optional, TypeVar, Dict, Generic,Type
from frameworkAG.geneticAlgorithm.geneticAlgorithmManager import GeneticAlgorithmManager
from frameworkAG.Environments import AmbienteGeneral

_T = TypeVar('_T')

class StandardSolver():
    ambientes: List[AmbienteGeneral]
    iteraciones: int
    aptitudFinal: int
    cantidadIndividuos: int
    geneticAlgorithm: GeneticAlgorithmManager
    classReference:Type[_T]
    def __init__(self,
                 ambientes: List[AmbienteGeneral],
                 iteraciones: int,
                 aptitudFinal: int,
                 cantidadIndividuos: int,
                 geneticAlgorithm: GeneticAlgorithmManager,
                 classReference: Type[_T]):
        self.iteraciones = iteraciones
        self.ambientes = ambientes
        self.aptitudFinal = aptitudFinal
        self.cantidadIndividuos = cantidadIndividuos
        self.geneticAlgorithm = geneticAlgorithm
        self.classReference = classReference

    def runAlgotirmo(self):
        for ambiente in self.ambientes:            
            self.geneticAlgorithm.cleanSolution()
            self.geneticAlgorithm.environment = ambiente
            self.geneticAlgorithm.individualReference = self.classReference(ambiente)
            self.geneticAlgorithm.run(self.cantidadIndividuos, self.iteraciones)
            ambiente.updateEnvironment(self.geneticAlgorithm.mejorIndividuo.ambiente)
            #self.updateRecursos(self.geneticAlgorithm.mejorIndividuo.ambiente, ambiente)
