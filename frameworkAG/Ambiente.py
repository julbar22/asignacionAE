from typing import List, Optional, TypeVar, Dict, Generic
from frameworkAG.Recurso import Recurso, RecursoTiempo
from frameworkAG.Horarios import WeekDay, TimeTable
from frameworkAG.Entidades import Asignacion
from modelSemanaEscolar.resourcesSemana import Materia



class AmbienteEspecificoTiempo:
    horario: TimeTable
    recursos: Dict[str, List[Recurso]]
    asignaciones: List[Asignacion]

    def __init__(self):
        self.asignaciones = list()

    def getRecursoPorTipoAndID(self, typeRecursoId:str, recursoId:str)->Recurso:
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
        #Primero
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

        #segundo
        edFisica2 = Materia("Ed Fisica2", 2, 1, 2)
        edFisica2.addRecursoVinculado("Profesor", juan)
        mate2 = Materia("Matematicas2", 4, 1, 2)
        mate2.addRecursoVinculado("Profesor", pedro)
        dibujo2 = Materia("Dibujo2", 5, 1, 2)
        dibujo2.addRecursoVinculado("Profesor", diana)
        danza2 = Materia("Danza2", 3, 1, 2)
        danza2.addRecursoVinculado("Profesor", juan)
        ciencias2 = Materia("Ciencias2", 2, 1, 2)
        ciencias2.addRecursoVinculado("Profesor", nora)
        lengua2 = Materia("Lengua2", 3, 1, 2)
        lengua2.addRecursoVinculado("Profesor", lucas)
        sis2 = Materia("Sistemas2", 2, 1, 2)
        sis2.addRecursoVinculado("Profesor", luis)
        musica2 = Materia("Musica2", 4, 1, 2)
        musica2.addRecursoVinculado("Profesor", paola)
        canto2 = Materia("Canto2", 2, 1, 2)
        canto2.addRecursoVinculado("Profesor", paola)
        ingles2 = Materia("Ingles2", 3, 1, 2)
        ingles2.addRecursoVinculado("Profesor", lucas)
        segundo = Recurso("2")
        segundo.addRecursoVinculado("Materia", edFisica2)
        segundo.addRecursoVinculado("Materia", mate2)
        segundo.addRecursoVinculado("Materia", dibujo2)
        segundo.addRecursoVinculado("Materia", danza2)
        segundo.addRecursoVinculado("Materia", ciencias2)
        segundo.addRecursoVinculado("Materia", lengua2)
        segundo.addRecursoVinculado("Materia", sis2)
        segundo.addRecursoVinculado("Materia", musica2)
        segundo.addRecursoVinculado("Materia", canto2)
        segundo.addRecursoVinculado("Materia", ingles2)

        #tercero
        edFisica3 = Materia("Ed Fisica3", 2, 1, 2)
        edFisica3.addRecursoVinculado("Profesor", juan)
        mate3 = Materia("Matematicas3", 5, 1, 2)
        mate3.addRecursoVinculado("Profesor", pedro)
        fis3 = Materia("Fisica3", 1, 1, 1)
        fis3.addRecursoVinculado("Profesor", pedro)
        dibujo3 = Materia("Dibujo3", 4, 1, 2)
        dibujo3.addRecursoVinculado("Profesor", diana)
        danza3 = Materia("Danza3", 2, 1, 2)
        danza3.addRecursoVinculado("Profesor", juan)
        ciencias3 = Materia("Ciencias3", 3, 1, 2)
        ciencias3.addRecursoVinculado("Profesor", nora)
        quimica3 = Materia("Quimica3", 1, 1, 1)
        quimica3.addRecursoVinculado("Profesor", nora)
        lengua3 = Materia("Lengua3", 3, 1, 2)
        lengua3.addRecursoVinculado("Profesor", lucas)
        sis3 = Materia("Sistemas3", 3, 1, 2)
        sis3.addRecursoVinculado("Profesor", luis)
        canto3 = Materia("Canto3", 3, 1, 2)
        canto3.addRecursoVinculado("Profesor", paola)
        ingles3 = Materia("Ingles3", 3, 1, 2)
        ingles3.addRecursoVinculado("Profesor", lucas)
        tercero = Recurso("3")
        tercero.addRecursoVinculado("Materia", edFisica3)
        tercero.addRecursoVinculado("Materia", mate3)
        tercero.addRecursoVinculado("Materia", fis3)
        tercero.addRecursoVinculado("Materia", dibujo3)
        tercero.addRecursoVinculado("Materia", danza3)
        tercero.addRecursoVinculado("Materia", ciencias3)
        tercero.addRecursoVinculado("Materia", quimica3)
        tercero.addRecursoVinculado("Materia", lengua3)
        tercero.addRecursoVinculado("Materia", sis3)
        tercero.addRecursoVinculado("Materia", canto3)
        tercero.addRecursoVinculado("Materia", ingles3)

        #cuarto
        edFisica4 = Materia("Ed Fisica4", 2, 1, 2)
        edFisica4.addRecursoVinculado("Profesor", juan)
        mate4 = Materia("Matematicas4", 5, 1, 2)
        mate4.addRecursoVinculado("Profesor", pedro)
        fis4 = Materia("Fisica4", 2, 1, 1)
        fis4.addRecursoVinculado("Profesor", pedro)
        dibujo4 = Materia("Dibujo4", 2, 1, 2)
        dibujo4.addRecursoVinculado("Profesor", diana)
        danza4 = Materia("Danza4", 2, 1, 2)
        danza4.addRecursoVinculado("Profesor", juan)
        ciencias4 = Materia("Ciencias4", 3, 1, 2)
        ciencias4.addRecursoVinculado("Profesor", nora)
        quimica4 = Materia("Quimica4", 1, 1, 1)
        quimica4.addRecursoVinculado("Profesor", nora)
        lengua4 = Materia("Lengua4", 6, 1, 2)
        lengua4.addRecursoVinculado("Profesor", lucas)
        sis4 = Materia("Sistemas4", 3, 1, 2)
        sis4.addRecursoVinculado("Profesor", luis)
        ingles4 = Materia("Ingles4", 4, 1, 2)
        ingles4.addRecursoVinculado("Profesor", martha)
        cuarto = Recurso("4")
        cuarto.addRecursoVinculado("Materia", edFisica4)
        cuarto.addRecursoVinculado("Materia", mate4)
        cuarto.addRecursoVinculado("Materia", fis4)
        cuarto.addRecursoVinculado("Materia", dibujo4)
        cuarto.addRecursoVinculado("Materia", danza4)
        cuarto.addRecursoVinculado("Materia", ciencias4)
        cuarto.addRecursoVinculado("Materia", quimica4)
        cuarto.addRecursoVinculado("Materia", lengua4)
        cuarto.addRecursoVinculado("Materia", sis4)
        cuarto.addRecursoVinculado("Materia", ingles4)

        #quinto
        edFisica5 = Materia("Ed Fisica5", 2, 1, 2)
        edFisica5.addRecursoVinculado("Profesor", juan)
        mate5 = Materia("Matematicas5", 5, 1, 2)
        mate5.addRecursoVinculado("Profesor", pedro)
        fis5 = Materia("Fisica4", 3, 1, 2)
        fis5.addRecursoVinculado("Profesor", pedro)
        dibujo5 = Materia("Dibujo5", 2, 1, 2)
        dibujo5.addRecursoVinculado("Profesor", diana)
        danza5 = Materia("Danza5", 2, 1, 2)
        danza5.addRecursoVinculado("Profesor", juan)
        ciencias5 = Materia("Ciencias5", 3, 1, 2)
        ciencias5.addRecursoVinculado("Profesor", nora)
        quimica5 = Materia("Quimica4", 1, 1, 1)
        quimica5.addRecursoVinculado("Profesor", nora)
        lengua5 = Materia("Lengua5", 5, 1, 2)
        lengua5.addRecursoVinculado("Profesor", lucas)
        sis5 = Materia("Sistemas5", 3, 1, 2)
        sis5.addRecursoVinculado("Profesor", luis)
        ingles5 = Materia("Ingles4", 4, 1, 2)
        ingles5.addRecursoVinculado("Profesor", martha)
        quinto = Recurso("5")
        quinto.addRecursoVinculado("Materia", edFisica5)
        quinto.addRecursoVinculado("Materia", mate5)
        quinto.addRecursoVinculado("Materia", fis5)
        quinto.addRecursoVinculado("Materia", dibujo5)
        quinto.addRecursoVinculado("Materia", danza5)
        quinto.addRecursoVinculado("Materia", ciencias5)
        quinto.addRecursoVinculado("Materia", quimica5)
        quinto.addRecursoVinculado("Materia", lengua5)
        quinto.addRecursoVinculado("Materia", sis5)
        quinto.addRecursoVinculado("Materia", ingles5)

        self.recursos["cursos"] = list()
        self.recursos["cursos"].append(primero)
        self.recursos["cursos"].append(segundo)
        self.recursos["cursos"].append(tercero)
        self.recursos["cursos"].append(cuarto)
        self.recursos["cursos"].append(quinto)
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
  