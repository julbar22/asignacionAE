from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, TypeVar, Dict, Generic
import random
from functools import reduce
import operator
from enum import Enum

class TimeTable:
    _open_slots: List[TimeSlot]

    @staticmethod
    def week_day_continuous_hours(week_day: WeekDay, from_hour: int, to_hour: int) -> TimeTable:
        slots = list(map(lambda hour: TimeSlot(week_day, hour),
                         list(range(from_hour, to_hour))))
        return TimeTable(slots)

    @staticmethod
    def joining(time_tables: List[TimeTable]) -> TimeTable:
        return TimeTable(sorted(reduce(operator.concat, list(map(lambda tt: tt.slots(), time_tables)))))

    def __init__(self, open_slots: List[TimeSlot] = None):
        if open_slots is None:
            open_slots = []
        self._open_slots = []
        self._add(open_slots)

    def _add(self, slots: List[TimeSlot]):
        list_without_duplicates = list(set(slots))
        self._open_slots = sorted(self._open_slots + list_without_duplicates)

    def slots(self) -> List[TimeSlot]:
        return self._open_slots

    def contains(self, time_slot: TimeSlot) -> bool:
        return self._open_slots.__contains__(time_slot)

    def week_days(self) -> List[WeekDay]:
        return sorted(list(set(map(lambda x: x.week_day, self._open_slots))))

    def intersection(self, other_time_table: TimeTable) -> TimeTable:
        return TimeTable(list(set(self._open_slots).intersection(other_time_table._open_slots)))

    def is_empty(self) -> bool:
        return len(self._open_slots) == 0

    def any_time_slot(self) -> Optional[TimeSlot]:
        if len(self._open_slots) == 0:
            return None
        return random.sample(self._open_slots, 1)[0]



@dataclass(frozen=True)
class TimeSlot:
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


@dataclass(frozen=True)
class WeekDay(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    @staticmethod
    def all() -> [WeekDay]:
        return [WeekDay.MON, WeekDay.TUE, WeekDay.WED, WeekDay.THU, WeekDay.FRI, WeekDay.SAT, WeekDay.SUN]

    def next(self) -> WeekDay:
        if self == WeekDay.MON:
            return WeekDay.TUE
        if self == WeekDay.TUE:
            return WeekDay.WED
        if self == WeekDay.WED:
            return WeekDay.THU
        if self == WeekDay.THU:
            return WeekDay.FRI
        if self == WeekDay.FRI:
            return WeekDay.SAT
        if self == WeekDay.SAT:
            return WeekDay.SUN
        if self == WeekDay.SUN:
            return WeekDay.MON

    def previous(self) -> WeekDay:
        if self == WeekDay.MON:
            return WeekDay.SUN
        if self == WeekDay.TUE:
            return WeekDay.MON
        if self == WeekDay.WED:
            return WeekDay.TUE
        if self == WeekDay.THU:
            return WeekDay.WED
        if self == WeekDay.FRI:
            return WeekDay.THU
        if self == WeekDay.SAT:
            return WeekDay.FRI
        if self == WeekDay.SUN:
            return WeekDay.SAT

    def __lt__(self, other: WeekDay):
        return self.value < other.value

    def __eq__(self, other: WeekDay):
        return self.value == other.value

    def __str__(self):
        if self == WeekDay.MON:
            return "MONDAY"
        if self == WeekDay.TUE:
            return "TUESDAY"
        if self == WeekDay.WED:
            return "WEDNESDAY"
        if self == WeekDay.THU:
            return "THURSDAY"
        if self == WeekDay.FRI:
            return "FRIDAY"
        if self == WeekDay.SAT:
            return "SATURDAY"
        if self == WeekDay.SUN:
            return "SUNDAY"

    def __repr__(self):
        return str(self)

