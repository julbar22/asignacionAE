from models.semanaEscolar import SemanaEscolar
from datetime import date
import datetime
from models.dia import Dia
from models.asignacion import Asignacion
from models.curso import Curso
from models.materia import Materia
from models.profesor import Profesor
from models.cursada import Cursada
from models.horario import Horario
import json
from enums.diaSemana import DiaSemana
from escenario import Escenario


def json_default(value):

    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        if isinstance(value, DiaSemana):
            return value.name
        else:
            return value.__dict__

def run():
    escenario = Escenario()
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
    json_data = json.dumps(semana, skipkeys=True, check_circular=False,
                           default=lambda o: json_default(o), indent=4)
    print(json_data)


if __name__ == '__main__':
    run()
