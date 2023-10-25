
from datetime import datetime
from uuid import uuid4

from ..abstractions import Entity
from ..value_objects import WorkId


class Work(Entity[WorkId]):
    
    def __init__(self, id: WorkId, title: str, specification: str, budget: float, expire_time: datetime) -> None:
        super().__init__(id)
        self.title = title
        self.specification = specification
        self.budget = budget
        self.expire_time = expire_time

    @classmethod
    def create(cls, title: str, specification: str, budget: float, expire_time: datetime) -> "Work":
        return Work(WorkId.create(str(uuid4())), title, specification, budget, expire_time)
