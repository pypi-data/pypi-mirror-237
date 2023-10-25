from ..abstractions import ValueObject


class Email(ValueObject):
    MAX_LENGTH = 320

    def __init__(self, value: str) -> None:
        self.value = value 
    
    @classmethod
    def create(cls, address: str) -> "Email":
        return Email(address)
    
    def get_equality_components(self) -> tuple[object]:
        return (self.value,)