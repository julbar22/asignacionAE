from frameworkAG.Resources import Resource, ResourceTime

class Subject(Resource):
    weeklyHours = 0
    horasMinimasCons = 0
    maxConsecutiveHours = 0

    def __init__(self, identifier: str, hsSemanales: int, hsMinimasCons: int, hsMaximasCons: int):
        super(Subject,self).__init__(identifier)
        self.weeklyHours = hsSemanales
        self.horasMinimasCons = hsMinimasCons
        self.maxConsecutiveHours = hsMaximasCons