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
        errorCompleto=" typeError:"+str(self.typeError)
        errorCompleto+=" subject:"+self.subject.identifier
        errorCompleto+=" teacher :"+self.teacher 
        errorCompleto+=" day:"+self.day.name
        errorCompleto+=" horasMaximas:"+str(self.weeklyHours)
        errorCompleto+=" assignedHours:"+str(self.assignedHours)
        print(errorCompleto)