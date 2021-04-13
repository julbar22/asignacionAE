from frameworkAG.Resources import Resource, ResourceTime
from frameworkAG.ScheduleUtils import TimeSlot, TimeTable
from typing import List, Optional, TypeVar, Dict, Generic

class Assignment:
    timeSlot: TimeSlot
    listResourceId: List[str]

    def __init__(self):
        self.listResourceId= list()
    
    def containResource(self, resourceId:str)-> bool:
        return True if resourceId in self.listResourceId else False


class Schedule:
    data: List[Assignment]
    dataByTimeSlot: Dict[TimeSlot, Assignment]
    timetable: TimeTable

    def __init__(self, timetable:TimeTable):
        #Revisar si necesito un copy
        self.data= list()
        self.dataByTimeSlot={}
        self.timetable = TimeTable(timetable._open_slots)

    def addAssignment(self, timeSlot:TimeSlot,assignment: Assignment):
        self.data.append(assignment)
        self.dataByTimeSlot[timeSlot]=assignment
        self.timetable._open_slots.remove(timeSlot)
        
    def getAssignmentsByResource(self,resourceId)->List[Assignment]:
        return list(filter(lambda assignment: assignment.containResource(resourceId),self.data))
