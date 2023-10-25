

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .value_object import ValueObject

TEntityIdentifier = TypeVar("TEntityIdentifier", bound=ValueObject)

class Entity(ABC, Generic[TEntityIdentifier]):

    @abstractmethod
    def __init__(self, id: TEntityIdentifier) -> None:
        self.id = id

    def __eq__(self, other: object) -> bool:
        if other is None:
            return False
        
        if not isinstance(other, Entity):  
            return False
        
        return self.id == other.id
    
    def __ne__(self, other: object) -> bool:
        return not self == other 
    
    def __hash__(self) -> int:
        return hash(self.id)