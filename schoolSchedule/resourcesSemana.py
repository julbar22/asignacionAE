from frameworkAG.Resources import Resource, ResourceTime

class Subject(Resource):
    weeklyHours = 0
    minConsecutiveHours = 0
    maxConsecutiveHours = 0

    def __init__(self, identifier: str, hsSemanales: int, hsMinCons: int, hsMaxCons: int):
        super(Subject,self).__init__(identifier)
        self.weeklyHours = hsSemanales
        self.minConsecutiveHours = hsMinCons
        self.maxConsecutiveHours = hsMaxCons