from abc import ABC, abstractmethod
from typing import List
from modelSemanaEscolar.dia  import Dia
class CrossSemana(ABC):
    

    def croosRun(self, semana1:List[Dia], semana2:List[Dia])->List[List[Dia]]:
        raise NotImplementedError