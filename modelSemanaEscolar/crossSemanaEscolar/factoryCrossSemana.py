from modelSemanaEscolar.crossSemanaEscolar.crossSemanaEnum import CrossSemanaEnum
from modelSemanaEscolar.crossSemanaEscolar.crossSemana import CrossSemana
from modelSemanaEscolar.crossSemanaEscolar.crossSemanaDiaCompleto import CrossSemanaDiaCompleto
from modelSemanaEscolar.crossSemanaEscolar.crossSemanaDiaAndCurso import CrossSemanaDiaAndCurso

class FactoryCrossSemana():
    

    def getCrossSemana(self, crossSemana:CrossSemanaEnum)->CrossSemana:
        if crossSemana.name=='croosDia':
            return CrossSemanaDiaCompleto()
        if crossSemana.name=='croosDiaAndCurso':
            return CrossSemanaDiaAndCurso()