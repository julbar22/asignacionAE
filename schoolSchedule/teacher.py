class Profesor:

    materias = list()
    availability = None
    nombre: ""

    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []


