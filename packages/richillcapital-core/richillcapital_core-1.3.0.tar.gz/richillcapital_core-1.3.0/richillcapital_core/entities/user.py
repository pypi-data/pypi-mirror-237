from uuid import uuid4

from ..abstractions import Entity
from ..value_objects import Email, UserId


class User(Entity[UserId]):

    def __init__(self, id: UserId, email: Email, name: str) -> None:
        super().__init__(id)
        self.email = email
        self.name = name

    @classmethod
    def create(cls, email: Email, name: str) -> "User":
        return User(UserId.create(str(uuid4())), email, name)