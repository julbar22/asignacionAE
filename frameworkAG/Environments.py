from typing import List, Optional, TypeVar, Dict, Generic
from frameworkAG.Resources import Resource
from frameworkAG.ScheduleUtils import WeekDay
from frameworkAG.Entities import Assignment
from frameworkAG.TimeTable import TimeTable


class GeneralEnvironment():
    resources: Dict[str, List[Resource]]
    assignments: List[Assignment]

    def __init__(self):
        self.assignments = list()
        self.resources = {}

    def getResourceByTypeAndID(self, typeResourceId: str, resourceId: str) -> Resource:
        for typeResource in self.resources:
            if(typeResource == typeResourceId):
                resourcesList: List[Resource] = self.resources[typeResource]
                for resource in resourcesList:
                    if resource.identifier == resourceId:
                        return resource

    def updateEnvironment(self, newEnvironment):
        pass


class EnvironmentTime(GeneralEnvironment):
    timetable: TimeTable

    def __init__(self):
        super(EnvironmentTime, self).__init__()


class EnvironmentSpace(GeneralEnvironment):
    initialSpace: str
