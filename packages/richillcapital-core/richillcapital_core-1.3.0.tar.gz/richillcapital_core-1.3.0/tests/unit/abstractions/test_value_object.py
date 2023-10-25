from assertpy import assert_that
from richillcapital_core.abstractions import ValueObject


class MyValueObject(ValueObject):

    def __init__(self, value: str):
        self.value = value

    def get_equality_components(self):
        return (self.value)


class TestValueObject:

    def test_value_object_equality(self) -> None:
        value = MyValueObject("Test")
        value2 = MyValueObject("Test")
        value3 = None
        value4 = ""

        assert_that(value == value2).is_true()
        assert_that(value == value3).is_false()
        assert_that(value == value4).is_false()

    def test_value_object_inequality(self) -> None:
        value = MyValueObject("Test")
        value2 = MyValueObject("test2")

        assert_that(value != value2).is_true()

    def test_value_object_hash_equality(self) -> None:
        value1 = MyValueObject("1")
        value2 = MyValueObject("1")
        assert_that(hash(value1) == hash(value2)).is_true()