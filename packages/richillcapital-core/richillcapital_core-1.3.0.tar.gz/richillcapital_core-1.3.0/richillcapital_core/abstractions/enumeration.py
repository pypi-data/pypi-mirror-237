from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TEnum = TypeVar("TEnum", bound="Enumeration[TEnum]") 


class Enumeration(ABC, Generic[TEnum]):
    enumerations: dict["Enumeration[TEnum]", int] = {}

    @abstractmethod
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
        self.enumerations[self] = value

    @classmethod
    def from_name(cls, name: str):
        for enum_member, _ in cls.enumerations.items():
            if enum_member.name == name:
                return enum_member
        raise Exception(f"No enumeration with name '{name}' found.")

    @classmethod
    def from_value(cls, value: int):
        for enum_member, enum_value in cls.enumerations.items():
            if type(enum_member) is cls and enum_value == value:
                return enum_member
        raise Exception(f"No enumeration with value '{value}' found.")

    def __str__(self):
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Enumeration) and other.name == self.name and other.value == self.value
    
    def __ne__(self, __value: object) -> bool:
        return super().__ne__(__value)
