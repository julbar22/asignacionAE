from modelSemanaEscolar.semanaEscolar import SemanaEscolar
from datetime import date
import datetime
from modelSemanaEscolar.dia import Dia
from modelSemanaEscolar.asignacion import Asignacion
from modelSemanaEscolar.curso import Curso
from modelSemanaEscolar.materia import Materia
from modelSemanaEscolar.profesor import Profesor
from modelSemanaEscolar.cursada import Cursada
from modelSemanaEscolar.horario import Horario
import json
from enums.diaSemana import DiaSemana
from modelSemanaEscolar.escenario import Escenario


def json_default(value):

    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        if isinstance(value, DiaSemana):
            return value.name
        else:
            return value.__dict__


def printSolucion(solucion: SemanaEscolar):
    solucionToPrint = {}
    for dia in solucion.cromosoma:
        solucionToPrint[dia.fecha.name] = []
        for horario in dia.horarios:
            asignacionDia = []
            asignacionDia.append(horario.horario)
            asignacionHorario = horario.asignacion
            asignacionDia.append(asignacionHorario.profesor.nombre)
            asignacionDia.append(asignacionHorario.cursada.materia.nombre)
            asignacionDia.append(asignacionHorario.cursada.curso.nombre)
            solucionToPrint[dia.fecha.name].append(asignacionDia)

    return solucionToPrint


def run():
    escenario = Escenario()
    escenario.printEscenario()
    cursada = escenario.cursada
    profesorPedro = escenario.getProfesor("Pedro Gonzales")
    asignacionMatPrimeroA = Asignacion(profesorPedro, cursada[0])
    profesorCarla = escenario.getProfesor("Carla Gomez")
    asignacionLenPrimeroB = Asignacion(profesorCarla, cursada[5])

    semana = SemanaEscolar(DiaSemana.lunes, DiaSemana.martes)
    lunes: Dia = semana.getDia(DiaSemana.lunes)
    horarioLunesMatPrimeroA = Horario(asignacionMatPrimeroA, (9,  12))
    lunes.addHorario(horarioLunesMatPrimeroA)
    horarioLunesLenPrimeroA = Horario(asignacionLenPrimeroB, (9,  11))
    lunes.addHorario(horarioLunesLenPrimeroA)

    martes: Dia = semana.getDia(DiaSemana.martes)
    horarioMartesMatPrimeroA = Horario(asignacionMatPrimeroA, (9,  12))
    martes.addHorario(horarioMartesMatPrimeroA)
    horarioMartesLenPrimeroA = Horario(asignacionLenPrimeroB, (9, 11))
    martes.addHorario(horarioMartesLenPrimeroA)
    # semana.solucion()
    solucion = printSolucion(semana)
    json_data = json.dumps(solucion, skipkeys=True, check_circular=False,
                           default=lambda o: json_default(o), indent=4)
    print("--------------------inicio solucion --------------------------")
    print(json_data)
    print("--------------------fin solucion --------------------------")


if __name__ == '__main__':
    run()
