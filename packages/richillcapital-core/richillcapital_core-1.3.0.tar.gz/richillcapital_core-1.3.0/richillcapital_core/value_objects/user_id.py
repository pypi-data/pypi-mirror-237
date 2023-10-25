from ..abstractions import ValueObject


class UserId(ValueObject):
    MAX_LENGTH = 128
    
    def __init__(self, value: str) -> None:
        self.value = value

    @classmethod
    def create(cls, id: str) -> "UserId":
        return UserId(id)
    
    def get_equality_components(self) -> tuple[object]:
        return (self.value,)