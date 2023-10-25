from abc import ABC, abstractmethod


class ValueObject(ABC):

    def __eq__(self, other: object):
        if other is None:
            return False

        if not isinstance(other, ValueObject):
            return False

        return self.get_equality_components() == other.get_equality_components()

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @abstractmethod
    def get_equality_components(self) -> tuple[object]: ...

    def __hash__(self):
        return hash(self.get_equality_components())