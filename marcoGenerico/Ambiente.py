from typing import List, Optional, TypeVar, Dict, Generic
from marcoGenerico.Recurso import Recurso, RecursoTiempo
from marcoGenerico.Horarios import WeekDay, TimeTable
from marcoGenerico.Entidades import Materia, Asignacion



class AmbienteEspecificoTiempo:
    horario: TimeTable
    recursos: Dict[str, List[Recurso]]
    asignaciones: List[Asignacion]

    def __init__(self):
        self.asignaciones = list()

    def getRecursoPorTipoAndID(self, typeRecursoId:str, recursoId:str):
        for typeRecurso in self.recursos:
            if(typeRecurso == typeRecursoId):
                listaRecusos:List[Recurso] = self.recursos[typeRecurso]
                for recurso in listaRecusos:
                    if recurso.identificador== recursoId:
                        return recurso
         
        


class AmbienteGeneral:
    recursos: Dict[str, List[Recurso]]

    def __init__(self):
        # Profesores
        self.recursos = {}
        juan = RecursoTiempo("Juan")
        juan.disponibilidad = monday_to_friday_from_7_to_13()
        pedro = RecursoTiempo("Pedro")
        pedro.disponibilidad = monday_to_friday_from_7_to_13()
        diana = RecursoTiempo("Diana")
        diana.disponibilidad = monday_to_friday_from_7_to_13()
        lucas = RecursoTiempo("Lucas")
        lucas.disponibilidad = monday_to_friday_from_7_to_13()
        martha = RecursoTiempo("Martha")
        martha.disponibilidad = monday_to_friday_from_7_to_13()
        luis = RecursoTiempo("Luis")
        luis.disponibilidad = monday_to_friday_from_7_to_13()
        nora = RecursoTiempo("Nora")
        nora.disponibilidad = monday_to_friday_from_7_to_13()
        paola = RecursoTiempo("Paola")
        paola.disponibilidad = monday_to_friday_from_7_to_13()

        # MateriasPorCursoyCurso
        edFisica1 = Materia("Ed Fisica1", 2, 1, 2)
        edFisica1.addRecursoVinculado("Profesor", juan)
        mate1 = Materia("Matematicas1", 4, 1, 2)
        mate1.addRecursoVinculado("Profesor", pedro)
        dibujo1 = Materia("Dibujo1", 5, 1, 2)
        dibujo1.addRecursoVinculado("Profesor", diana)
        danza1 = Materia("Danza1", 4, 1, 2)
        danza1.addRecursoVinculado("Profesor", juan)
        ciencias1 = Materia("Ciencias1", 2, 1, 2)
        ciencias1.addRecursoVinculado("Profesor", nora)
        lengua1 = Materia("Lengua1", 3, 1, 2)
        lengua1.addRecursoVinculado("Profesor", lucas)
        sis1 = Materia("Sistemas1", 1, 1, 1)
        sis1.addRecursoVinculado("Profesor", luis)
        musica1 = Materia("Musica1", 3, 1, 2)
        musica1.addRecursoVinculado("Profesor", paola)
        canto1 = Materia("Canto1", 3, 1, 2)
        canto1.addRecursoVinculado("Profesor", paola)
        ingles1 = Materia("Ingles1", 3, 1, 2)
        ingles1.addRecursoVinculado("Profesor", lucas)
        primero = Recurso("1")
        primero.addRecursoVinculado("Materia", edFisica1)
        primero.addRecursoVinculado("Materia", mate1)
        primero.addRecursoVinculado("Materia", dibujo1)
        primero.addRecursoVinculado("Materia", danza1)
        primero.addRecursoVinculado("Materia", ciencias1)
        primero.addRecursoVinculado("Materia", lengua1)
        primero.addRecursoVinculado("Materia", sis1)
        primero.addRecursoVinculado("Materia", musica1)
        primero.addRecursoVinculado("Materia", canto1)
        primero.addRecursoVinculado("Materia", ingles1)

        self.recursos["cursos"] = list()
        self.recursos["cursos"].append(primero)
        #self.recursos["profesores"] = list()

    def getAbientePorCurso(self)-> List[AmbienteEspecificoTiempo]:
        cursos: List[Recurso] = self.recursos["cursos"]
        ambientes: List[AmbienteEspecificoTiempo] =list()
        for curso in cursos:
            ambienteCurso = AmbienteEspecificoTiempo()
            ambienteCurso.recursos = curso.recursosVinculados
            ambienteCurso.horario = monday_to_friday_from_7_to_13()
            ambientes.append(ambienteCurso)
        return ambientes


def day_from_7_to_13(week_day: WeekDay) -> TimeTable:
    return TimeTable.joining([
        TimeTable.week_day_continuous_hours(week_day, 7, 13)
    ])


def monday_to_friday_from_7_to_13() -> TimeTable:
    return TimeTable.joining([
        day_from_7_to_13(WeekDay.MON),
        day_from_7_to_13(WeekDay.TUE),
        day_from_7_to_13(WeekDay.WED),
        day_from_7_to_13(WeekDay.THU),
        day_from_7_to_13(WeekDay.FRI)
    ])
  