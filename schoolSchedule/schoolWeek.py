from frameworkAG.geneticAlgorithm.individual import IndividualTime, Individual
import random
from typing import List, Optional, TypeVar, Dict, Generic
from schoolSchedule.mapperToSemana import MapperToSemana
import copy
from schoolSchedule.errorWeek import ErrorWeek
from frameworkAG.Environments import EnvironmentTime
from frameworkAG.Resources import Resource, ResourceTime
from frameworkAG.Entities import Assignment
from frameworkAG.TimeTable import TimeTable
from frameworkAG.Slots import TimeSlot
from schoolSchedule.resourcesSemana import Subject


class SchoolWeek(IndividualTime):

    def __init__(self, environment: EnvironmentTime):
        self.environment: EnvironmentTime = copy.deepcopy(environment)
        self.fitness = 0
        self.mistakes = []
        super(SchoolWeek, self).__init__(self.environment)

    def calculateFitness(self):
        self.fitness = 0
        self.mistakes.clear()
        self.evaluateHoursByCourse()

    def evaluateHoursByCourse(self):
        for subject in self.environment.resources["Subject"]:
            assignments: List[Assignment] = self.timetable.getAssignmentsByResource(
                subject.identifier)
            for day in self.environment.timetable.week_days():
                assignmentByDay = list(filter(
                    lambda assignment: assignment.timeSlot.week_day == day, assignments))
                hoursDay = len(assignmentByDay)
                if hoursDay > subject.maxConsecutiveHours:
                    self.fitness += 1
                    error = ErrorWeek(1, subject)
                    error.day = day
                    error.assignedHours = hoursDay
                    error.weeklyHours = subject.maxConsecutiveHours
                    self.mistakes.append(error)
            if subject.weeklyHours != len(assignments):
                error = ErrorWeek(0, subject)
                error.assignedHours = len(assignments)
                error.weeklyHours = subject.weeklyHours
                self.fitness += abs(subject.weeklyHours-len(assignments))
                self.mistakes.append(error)

    def createRamdomIndividual(self, ambienteNuevo: EnvironmentTime) -> Individual:
        newAux = SchoolWeek(ambienteNuevo)
        newAux.completeCourses(newAux.environment.resources["Subject"])
        return newAux

    def mutate(self, index, environment: EnvironmentTime) -> Individual:
        newAux: IndividualTime = self.createRamdomIndividual(environment)
        indexAssignment: int = random.randint(0, len(self.timetable.data)-1)
        if indexAssignment in newAux.timetable.data:
            newAssignment: Assignment = copy.deepcopy(
                newAux.timetable.data[indexAssignment])
            self.timetable.data[indexAssignment] = newAssignment
            self.timetable.dataByTimeSlot[newAssignment.timeSlot] = newAssignment
        return self

    def improvement(self, environment) -> Individual:
        self.fixRandomErrors(environment)

    def cross(self, couple: IndividualTime, ambienteNuevo: EnvironmentTime) -> List[Individual]:
        newWeek1: SchoolWeek = SchoolWeek(ambienteNuevo)
        newWeek2: SchoolWeek = SchoolWeek(ambienteNuevo)

        for time in self.timetable.dataByTimeSlot:
            if random.uniform(0.0, 1.0) <= 0.5:
                if time in self.timetable.dataByTimeSlot:
                    newAssignment1: Assignment = self.timetable.dataByTimeSlot[time]
                    newWeek1.addCrossAssignment(newAssignment1)
                if time in couple.timetable.dataByTimeSlot:
                    newAssignment2: Assignment = couple.timetable.dataByTimeSlot[time]
                    newWeek2.addCrossAssignment(newAssignment2)
            else:
                if time in self.timetable.dataByTimeSlot:
                    newAssignment2: Assignment = self.timetable.dataByTimeSlot[time]
                    newWeek2.addCrossAssignment(newAssignment2)
                if time in couple.timetable.dataByTimeSlot:
                    newAssignment1: Assignment = couple.timetable.dataByTimeSlot[time]
                    newWeek1.addCrossAssignment(newAssignment1)

        weeks: list = []
        weeks.append(newWeek1)
        weeks.append(newWeek2)
        return weeks

    def addCrossAssignment(self, newAssignment: Assignment):
        self.timetable.addAssignment(
            newAssignment.timeSlot, copy.deepcopy(newAssignment))
        subject: Subject = self.environment.getResourceByTypeAndID(
            "Subject", newAssignment.listResourceId[0])
        teacher: ResourceTime = subject.linkedResources["Profesor"][0]
        teacher.availability._open_slots.remove(
            newAssignment.timeSlot)

    def completeCourses(self, subjects: List[Subject]):
        subjectCounter = 0
        while(subjectCounter < len(subjects)):
            subject: Subject = subjects[subjectCounter]
            subjectCounter += 1
            weeklyHours = subject.weeklyHours
            assignedHours = 0
            while weeklyHours > assignedHours:
                teacher: ResourceTime = subject.linkedResources["Profesor"][0]
                scheduleAvailable: TimeTable = teacher.availability.intersection(
                    self.timetable.timetable)
                time: Optional[TimeSlot] = scheduleAvailable.any_time_slot()
                if time is not None:
                    newAssignment: Assignment = Assignment()
                    newAssignment.timeSlot = time
                    newAssignment.listResourceId.append(
                        subject.identifier)
                    newAssignment.listResourceId.append(
                        teacher .identifier)
                    self.timetable.addAssignment(time, newAssignment)
                    teacher .availability._open_slots.remove(time)
                    assignedHours += 1
                else:
                    break

    def printIndividual(self):
        MapperToSemana.mapperSemana(self.timetable.data)

    def printErrors(self):
        for error in self.mistakes:
            if isinstance(error, ErrorWeek):
                error.printError()
            else:
                print(error)

    def fixRandomErrors(self, environment):
        if len(self.mistakes) > 0:
            error: ErrorWeek = random.choice(self.mistakes)
            if isinstance(error, ErrorWeek):
                if error.typeError == 0:
                    if error.weeklyHours > error.assignedHours:
                        subject: Subject = error.subject
                    else:
                        if error.weeklyHours < error.assignedHours:
                            subject = error.subject
                elif error.typeError == 1:
                    self.dailyAllowance(error, environment)
                elif error.typeError == 2:
                    dayTemp = error.day

    def dailyAllowance(self, error: ErrorWeek, environment):
        subject = error.subject
