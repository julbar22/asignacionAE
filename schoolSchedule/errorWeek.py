from schoolSchedule.resourcesSemana import Subject
from frameworkAG.ScheduleUtils import WeekDay

class ErrorWeek():

    typeError:int
    teacher :str
    day:WeekDay
    weeklyHours:int
    assignedHours:int
    subject:Subject

    def __init__(self, typeError:int, subject: Subject):
        self.typeError = typeError
        self.teacher =""
        self.subject=subject
        self.weeklyHours=0
        self.assignedHours=0
        self.day = WeekDay.SUN
       

    def printError(self):
        completeError=" typeError:"+str(self.typeError)
        completeError+=" subject:"+self.subject.identifier
        completeError+=" teacher :"+self.teacher 
        completeError+=" day:"+self.day.name
        completeError+=" horasMaximas:"+str(self.weeklyHours)
        completeError+=" assignedHours:"+str(self.assignedHours)
        print(completeError)