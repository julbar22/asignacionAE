class HorarioUtils():

    @staticmethod
    def isCrossPoints(point1: tuple, point2: tuple) -> bool:
        isCruzado: bool = HorarioUtils.sonHorariosCruzados(point1, point2)
        isInterno1: bool = HorarioUtils.contieneHorario(point1, point2)
        isInterno2: bool = HorarioUtils.contieneHorario(point2, point1)
        return isCruzado or isInterno1 or isInterno2

    @staticmethod
    def sonHorariosCruzados(horario1: tuple, horario2: tuple) -> bool:
        if(horario1[0] <= horario2[0] and horario1[1] > horario2[0]) or (horario1[0] < horario2[1] and horario1[1] >= horario2[1]):
            return True
        return False

    @staticmethod
    def contieneHorario(horario1: tuple, horario2: tuple) -> bool:
        if(horario1[0] <= horario2[0] and horario1[1] >= horario2[1]):
            return True
        return False
