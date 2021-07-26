from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, TypeVar, Dict, Generic
import random
from functools import reduce
import operator
from enum import Enum


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

