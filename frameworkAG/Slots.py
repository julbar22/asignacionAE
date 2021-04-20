from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Dict, Generic
from dataclasses import dataclass
from frameworkAG.ScheduleUtils import WeekDay


class Slot(ABC):
    id: str

@dataclass(frozen=True)
class SlotSpace(Slot):
    dimension: str
    available: bool
    longitude: float


@dataclass(frozen=True)
class TimeSlot(Slot):
    week_day: WeekDay
    hour: int

    def __lt__(self, other: TimeSlot):
        return self.comes_before(other)

    def comes_before(self, other_time_slot: TimeSlot) -> bool:
        if self.week_day < other_time_slot.week_day:
            return True
        elif self.week_day == other_time_slot.week_day:
            return self.hour < other_time_slot.hour
        return False

    def comes_after(self, other_time_slot: TimeSlot) -> bool:
        return other_time_slot.comes_before(self)

    def comes_immediately_after(self, other_time_slot: TimeSlot) -> bool:
        if self == TimeSlot(WeekDay.MON, 0) and other_time_slot == TimeSlot(WeekDay.SUN, 23):
            return True
        if not self.comes_after(other_time_slot):
            return False
        if self.week_day == other_time_slot.week_day:
            return self.hour == other_time_slot.hour + 1
        return self.hour == 0 and other_time_slot.hour == 23 and self.week_day == other_time_slot.week_day.next()

    def comes_immediately_before(self, other_time_slot: TimeSlot) -> bool:
        return other_time_slot.comes_immediately_after(self)

    def nextTimeSlot(self) -> TimeSlot:
        if self.hour == 23:
            return TimeSlot(self.week_day.next(), 0)
        return TimeSlot(self.week_day, self.hour + 1)

    def offsetting(self, number_of_timeslots_to_move: int) -> TimeSlot:
        moved_slot = self
        for _ in range(abs(number_of_timeslots_to_move)):
            if number_of_timeslots_to_move > 0:
                moved_slot = moved_slot.nextTimeSlot()
            else:
                moved_slot = moved_slot.previousTimeSlot()
        return moved_slot

    def previousTimeSlot(self) -> TimeSlot:
        if self.hour == 0:
            return TimeSlot(self.week_day.previous(), 23)
        return TimeSlot(self.week_day, self.hour - 1)

    def __eq__(self, other):
        return self.week_day == other.week_day and self.hour == other.hour

    def __repr__(self):
        return str(self.week_day) + "@" + str(self.hour) + ":00"
