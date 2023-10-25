from assertpy import assert_that
from richillcapital_core.abstractions import Entity, ValueObject


class MyEntityId(ValueObject):
    def __init__(self, value: str) -> None:
        self.value = value

    def get_equality_components(self):
        return (self.value)

class MyEntity(Entity[MyEntityId]):

    def __init__(self, id: MyEntityId) -> None:
        super().__init__(id)


class TestEntity():


    def test1(self) -> None:
        entity1 = MyEntity(MyEntityId("1"))
        entity2 = MyEntity(MyEntityId("2"))

        result = entity1 != entity2

        assert_that(result).is_true()

    def test2(self) -> None:
        entity1 = MyEntity(MyEntityId("1"))
        entity2 = MyEntity(MyEntityId("1"))

        result = entity1 == entity2

        assert_that(result).is_true()        

    def test2(self) -> None:
        entity1 = MyEntity(MyEntityId("1"))
        entity2 = MyEntity(MyEntityId("1"))

        result = hash(entity1) == hash(entity2)

        assert_that(result).is_true()      

    def test3(self) -> None:
        entity1 = MyEntity(MyEntityId("1"))

        assert_that(entity1).is_not_same_as(None)      
    
    def test4(self) -> None:
        entity1 = MyEntity(MyEntityId("1"))
        entity2 = ""

        result = entity1 != entity2

        assert_that(result).is_true()      
