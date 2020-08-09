from semanaEscolar import SemanaEscolar
from datetime import date
import datetime
from dia import Dia
from asignacion import Asignacion
from curso import Curso
from materia import Materia
from profesor import Profesor
from cursada import Cursada
from horario import Horario
import json

def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__

def ListaCursos():
    cursos = list()
    cursos.append(Curso("Primero A"))
    cursos.append(Curso("Primero B"))
    cursos.append(Curso("Segundo A"))
    cursos.append(Curso("Segundo A"))
    return cursos


def getCursada():
    cursos = ListaCursos()
    cursada = list()
    matematicas = Materia("Matematicas")
    cursada.append(Cursada(cursos[0], matematicas, 4, 2, 1))
    cursada.append(Cursada(cursos[1], matematicas, 4, 2, 1))
    cursada.append(Cursada(cursos[2], matematicas, 3, 3, 1))
    cursada.append(Cursada(cursos[3], matematicas, 3, 3, 1))
    lengua = Materia("Lengua")
    cursada.append(Cursada(cursos[0], lengua, 4, 2, 1))
    cursada.append(Cursada(cursos[1], lengua, 4, 2, 1))
    cursada.append(Cursada(cursos[2], lengua, 3, 3, 1))
    cursada.append(Cursada(cursos[3], lengua, 3, 3, 1))

    return cursada


def getHorario(fecha: date, hora: int):
    return datetime.datetime(fecha.year, fecha.month, fecha.day, hora)


def run():
    cursada = getCursada()
    profesorPedro = Profesor("Pedro Gonzales")
    asignacionMatPrimeroA = Asignacion(profesorPedro, cursada[0])
    # asignacionMatPrimeroB = Asignacion(profesorPedro, cursada[1])
    profesorCarla = Profesor("Carla Gomez")
    # asignacionLenPrimeroA = Asignacion(profesorCarla, cursada[4])
    asignacionLenPrimeroB = Asignacion(profesorCarla, cursada[5])
    inicioSemana = date(2020, 8, 3)
    finSemana = date(2020, 8, 7)
    semana = SemanaEscolar(inicioSemana, finSemana)
    lunes: Dia = semana.getDia(inicioSemana)
    horarioLunesMatPrimeroA = Horario(asignacionMatPrimeroA, (
        getHorario(lunes.fecha, 9), getHorario(lunes.fecha, 12)))
    lunes.addHorario(horarioLunesMatPrimeroA)
    horarioLunesLenPrimeroA = Horario(asignacionLenPrimeroB, (
        getHorario(lunes.fecha, 9), getHorario(lunes.fecha, 11)))
    lunes.addHorario(horarioLunesLenPrimeroA)
  

    martes: Dia = semana.getDia(date(2020, 8, 4))
    horarioMartesMatPrimeroA = Horario(asignacionMatPrimeroA, (
        getHorario(martes.fecha, 9), getHorario(martes.fecha, 12)))
    martes.addHorario(horarioMartesMatPrimeroA)
    horarioMartesLenPrimeroA = Horario(asignacionLenPrimeroB, (
        getHorario(martes.fecha, 9), getHorario(martes.fecha, 11)))
    martes.addHorario(horarioMartesLenPrimeroA)
    # semana.solucion()
    json_data = json.dumps(semana, skipkeys=True,check_circular=False,default=lambda o: json_default(o), indent=4)
    print(json_data)


if __name__ == '__main__':
    run()
