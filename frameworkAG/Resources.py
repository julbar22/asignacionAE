from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, TypeVar, Dict, Generic
from frameworkAG.TimeTable import TimeTable
from frameworkAG.Slots import SlotSpace


class Resource():
    linkedResources: Dict[str, List[Resource]]
    identifier: str

    def __init__(self, identifier: str):
        self.identifier = identifier
        self.linkedResources = {}

    def addTypeResourcesLinked(self, typeResource: str):
        if typeResource not in self.linkedResources:
            self.linkedResources[typeResource] = list()

    def addResourceLinked(self, typeResource: str, resource: Resource):
        self.addTypeResourcesLinked(typeResource)
        self.linkedResources[typeResource].append(resource)


class ResourceTime(Resource):
    availability: TimeTable


class SpaceResource(Resource):
    dimensions: str
    space: List[SlotSpace]
    spaceAvailable: List[SlotSpace]
