from frameworkAG.Environments import GeneralEnvironment, EnvironmentTime
from typing import List, Optional, TypeVar, Dict, Generic
from frameworkAG.Resources import Resource, ResourceTime
from frameworkAG.ScheduleUtils import WeekDay
from schoolSchedule.resourcesSemana import Subject
from frameworkAG.TimeTable import TimeTable

class EnvironmentSchool(GeneralEnvironment):
    
    def __init__(self):
        super(EnvironmentSchool,self).__init__()
        juan = ResourceTime("Juan")
        juan.availability = monday_to_friday_from_7_to_13()
        pedro = ResourceTime("Pedro")
        pedro.availability = monday_to_friday_from_7_to_13()
        diana = ResourceTime("Diana")
        diana.availability = monday_to_friday_from_7_to_13()
        lucas = ResourceTime("Lucas")
        lucas.availability = monday_to_friday_from_7_to_13()
        martha = ResourceTime("Martha")
        martha.availability = monday_to_friday_from_7_to_13()
        luis = ResourceTime("Luis")
        luis.availability = monday_to_friday_from_7_to_13()
        nora = ResourceTime("Nora")
        nora.availability = monday_to_friday_from_7_to_13()
        paola = ResourceTime("Paola")
        paola.availability = monday_to_friday_from_7_to_13()

        # MateriasPorCursoyCurso
        # Primero
        edFisica1 = Subject("Ed Fisica1", 2, 1, 2)
        edFisica1.addResourceLinked("Teacher", juan)
        mate1 = Subject("Matematicas1", 4, 1, 2)
        mate1.addResourceLinked("Teacher", pedro)
        dibujo1 = Subject("Dibujo1", 5, 1, 2)
        dibujo1.addResourceLinked("Teacher", diana)
        danza1 = Subject("Danza1", 4, 1, 2)
        danza1.addResourceLinked("Teacher", juan)
        ciencias1 = Subject("Ciencias1", 2, 1, 2)
        ciencias1.addResourceLinked("Teacher", nora)
        lengua1 = Subject("Lengua1", 3, 1, 2)
        lengua1.addResourceLinked("Teacher", lucas)
        sis1 = Subject("Sistemas1", 1, 1, 1)
        sis1.addResourceLinked("Teacher", luis)
        musica1 = Subject("Musica1", 3, 1, 2)
        musica1.addResourceLinked("Teacher", paola)
        canto1 = Subject("Canto1", 3, 1, 2)
        canto1.addResourceLinked("Teacher", paola)
        ingles1 = Subject("Ingles1", 3, 1, 2)
        ingles1.addResourceLinked("Teacher", lucas)
        primero = Resource("1")
        primero.addResourceLinked("Subject", edFisica1)
        primero.addResourceLinked("Subject", mate1)
        primero.addResourceLinked("Subject", dibujo1)
        primero.addResourceLinked("Subject", danza1)
        primero.addResourceLinked("Subject", ciencias1)
        primero.addResourceLinked("Subject", lengua1)
        primero.addResourceLinked("Subject", sis1)
        primero.addResourceLinked("Subject", musica1)
        primero.addResourceLinked("Subject", canto1)
        primero.addResourceLinked("Subject", ingles1)

        # segundo
        edFisica2 = Subject("Ed Fisica2", 2, 1, 2)
        edFisica2.addResourceLinked("Teacher", juan)
        mate2 = Subject("Matematicas2", 4, 1, 2)
        mate2.addResourceLinked("Teacher", pedro)
        dibujo2 = Subject("Dibujo2", 5, 1, 2)
        dibujo2.addResourceLinked("Teacher", diana)
        danza2 = Subject("Danza2", 3, 1, 2)
        danza2.addResourceLinked("Teacher", juan)
        ciencias2 = Subject("Ciencias2", 2, 1, 2)
        ciencias2.addResourceLinked("Teacher", nora)
        lengua2 = Subject("Lengua2", 3, 1, 2)
        lengua2.addResourceLinked("Teacher", lucas)
        sis2 = Subject("Sistemas2", 2, 1, 2)
        sis2.addResourceLinked("Teacher", luis)
        musica2 = Subject("Musica2", 4, 1, 2)
        musica2.addResourceLinked("Teacher", paola)
        canto2 = Subject("Canto2", 2, 1, 2)
        canto2.addResourceLinked("Teacher", paola)
        ingles2 = Subject("Ingles2", 3, 1, 2)
        ingles2.addResourceLinked("Teacher", lucas)
        segundo = Resource("2")
        segundo.addResourceLinked("Subject", edFisica2)
        segundo.addResourceLinked("Subject", mate2)
        segundo.addResourceLinked("Subject", dibujo2)
        segundo.addResourceLinked("Subject", danza2)
        segundo.addResourceLinked("Subject", ciencias2)
        segundo.addResourceLinked("Subject", lengua2)
        segundo.addResourceLinked("Subject", sis2)
        segundo.addResourceLinked("Subject", musica2)
        segundo.addResourceLinked("Subject", canto2)
        segundo.addResourceLinked("Subject", ingles2)

        # tercero
        edFisica3 = Subject("Ed Fisica3", 2, 1, 2)
        edFisica3.addResourceLinked("Teacher", juan)
        mate3 = Subject("Matematicas3", 5, 1, 2)
        mate3.addResourceLinked("Teacher", pedro)
        fis3 = Subject("Fisica3", 1, 1, 1)
        fis3.addResourceLinked("Teacher", pedro)
        dibujo3 = Subject("Dibujo3", 4, 1, 2)
        dibujo3.addResourceLinked("Teacher", diana)
        danza3 = Subject("Danza3", 2, 1, 2)
        danza3.addResourceLinked("Teacher", juan)
        ciencias3 = Subject("Ciencias3", 3, 1, 2)
        ciencias3.addResourceLinked("Teacher", nora)
        quimica3 = Subject("Quimica3", 1, 1, 1)
        quimica3.addResourceLinked("Teacher", nora)
        lengua3 = Subject("Lengua3", 3, 1, 2)
        lengua3.addResourceLinked("Teacher", lucas)
        sis3 = Subject("Sistemas3", 3, 1, 2)
        sis3.addResourceLinked("Teacher", luis)
        canto3 = Subject("Canto3", 3, 1, 2)
        canto3.addResourceLinked("Teacher", paola)
        ingles3 = Subject("Ingles3", 3, 1, 2)
        ingles3.addResourceLinked("Teacher", lucas)
        tercero = Resource("3")
        tercero.addResourceLinked("Subject", edFisica3)
        tercero.addResourceLinked("Subject", mate3)
        tercero.addResourceLinked("Subject", fis3)
        tercero.addResourceLinked("Subject", dibujo3)
        tercero.addResourceLinked("Subject", danza3)
        tercero.addResourceLinked("Subject", ciencias3)
        tercero.addResourceLinked("Subject", quimica3)
        tercero.addResourceLinked("Subject", lengua3)
        tercero.addResourceLinked("Subject", sis3)
        tercero.addResourceLinked("Subject", canto3)
        tercero.addResourceLinked("Subject", ingles3)

        # cuarto
        edFisica4 = Subject("Ed Fisica4", 2, 1, 2)
        edFisica4.addResourceLinked("Teacher", juan)
        mate4 = Subject("Matematicas4", 5, 1, 2)
        mate4.addResourceLinked("Teacher", pedro)
        fis4 = Subject("Fisica4", 2, 1, 1)
        fis4.addResourceLinked("Teacher", pedro)
        dibujo4 = Subject("Dibujo4", 2, 1, 2)
        dibujo4.addResourceLinked("Teacher", diana)
        danza4 = Subject("Danza4", 2, 1, 2)
        danza4.addResourceLinked("Teacher", juan)
        ciencias4 = Subject("Ciencias4", 3, 1, 2)
        ciencias4.addResourceLinked("Teacher", nora)
        quimica4 = Subject("Quimica4", 1, 1, 1)
        quimica4.addResourceLinked("Teacher", nora)
        lengua4 = Subject("Lengua4", 6, 1, 2)
        lengua4.addResourceLinked("Teacher", lucas)
        sis4 = Subject("Sistemas4", 3, 1, 2)
        sis4.addResourceLinked("Teacher", luis)
        ingles4 = Subject("Ingles4", 4, 1, 2)
        ingles4.addResourceLinked("Teacher", martha)
        cuarto = Resource("4")
        cuarto.addResourceLinked("Subject", edFisica4)
        cuarto.addResourceLinked("Subject", mate4)
        cuarto.addResourceLinked("Subject", fis4)
        cuarto.addResourceLinked("Subject", dibujo4)
        cuarto.addResourceLinked("Subject", danza4)
        cuarto.addResourceLinked("Subject", ciencias4)
        cuarto.addResourceLinked("Subject", quimica4)
        cuarto.addResourceLinked("Subject", lengua4)
        cuarto.addResourceLinked("Subject", sis4)
        cuarto.addResourceLinked("Subject", ingles4)

        # quinto
        edFisica5 = Subject("Ed Fisica5", 2, 1, 2)
        edFisica5.addResourceLinked("Teacher", juan)
        mate5 = Subject("Matematicas5", 5, 1, 2)
        mate5.addResourceLinked("Teacher", pedro)
        fis5 = Subject("Fisica4", 3, 1, 2)
        fis5.addResourceLinked("Teacher", pedro)
        dibujo5 = Subject("Dibujo5", 2, 1, 2)
        dibujo5.addResourceLinked("Teacher", diana)
        danza5 = Subject("Danza5", 2, 1, 2)
        danza5.addResourceLinked("Teacher", juan)
        ciencias5 = Subject("Ciencias5", 3, 1, 2)
        ciencias5.addResourceLinked("Teacher", nora)
        quimica5 = Subject("Quimica4", 1, 1, 1)
        quimica5.addResourceLinked("Teacher", nora)
        lengua5 = Subject("Lengua5", 5, 1, 2)
        lengua5.addResourceLinked("Teacher", lucas)
        sis5 = Subject("Sistemas5", 3, 1, 2)
        sis5.addResourceLinked("Teacher", luis)
        ingles5 = Subject("Ingles4", 4, 1, 2)
        ingles5.addResourceLinked("Teacher", martha)
        quinto = Resource("5")
        quinto.addResourceLinked("Subject", edFisica5)
        quinto.addResourceLinked("Subject", mate5)
        quinto.addResourceLinked("Subject", fis5)
        quinto.addResourceLinked("Subject", dibujo5)
        quinto.addResourceLinked("Subject", danza5)
        quinto.addResourceLinked("Subject", ciencias5)
        quinto.addResourceLinked("Subject", quimica5)
        quinto.addResourceLinked("Subject", lengua5)
        quinto.addResourceLinked("Subject", sis5)
        quinto.addResourceLinked("Subject", ingles5)

        self.resources["courses"] = list()
        self.resources["courses"].append(primero)
        self.resources["courses"].append(segundo)
        self.resources["courses"].append(tercero)
        self.resources["courses"].append(cuarto)
        self.resources["courses"].append(quinto)
        #self.resources["profesores"] = list()

    def getEnvironmentByCourse(self) -> List[EnvironmentTime]:
        courses: List[Resource] = self.resources["courses"]
        environments: List[EnvironmentTime] = list()
        for course in courses:
            environmentByCourse = EnvironmentTime()
            environmentByCourse.resources = course.linkedResources
            environmentByCourse.timetable = monday_to_friday_from_7_to_13()
            environments.append(environmentByCourse)
        return environments

    def updateEnvironment(self,newEnvironment:GeneralEnvironment):
        for subject in newEnvironment.resources["Subject"]:
            newTeacher: ResourceTime = subject.linkedResources["Teacher"][0]
            subjectOld = self.getResourceByTypeAndID(
                "Subject", subject.identifier)
            oldTeacher: ResourceTime = subjectOld.linkedResources["Teacher"][0]
            newTimeTable = oldTeacher.availability.intersection(
                newTeacher.availability)
            oldTeacher.availability = TimeTable(
                newTimeTable._open_slots)


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