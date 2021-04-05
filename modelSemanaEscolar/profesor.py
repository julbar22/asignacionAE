class Profesor:

    materias = list()
    disponibilidad = None
    nombre: ""

    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []


