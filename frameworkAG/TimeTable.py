from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, TypeVar, Dict, Generic
import random
from functools import reduce
import operator
from enum import Enum
from frameworkAG.Slots import TimeSlot
from frameworkAG.ScheduleUtils import WeekDay

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