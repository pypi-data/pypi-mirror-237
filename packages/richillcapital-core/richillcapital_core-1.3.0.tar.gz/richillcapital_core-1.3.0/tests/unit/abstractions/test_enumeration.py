from assertpy import assert_that
from richillcapital_core.abstractions import Enumeration


class MyEnum(Enumeration["MyEnum"]):
    One: "MyEnum"
    Two: "MyEnum"

    def __init__(self, name: str, value: int):
        super().__init__(name, value)

class MyEnum2(Enumeration["MyEnum2"]):
    A: "MyEnum2"
    B: "MyEnum2"

    def __init__(self, name: str, value: int):
        super().__init__(name, value)


class OtherType():
    def __init__(self) -> None: ...

MyEnum.One = MyEnum("One", 1)
MyEnum.Two = MyEnum("Two", 2)

MyEnum2.A = MyEnum2("A", 1)
MyEnum2.B = MyEnum2("B", 2)


class TestEnumeration:

    def test_enum_from_name_should_return_correct_enum_instance(self) -> None:
        enum1 = MyEnum.from_name("One")
        
        assert_that(enum1 == OtherType()).is_false()

    def test_enum_from_value_should_return_correct_enum_instance(self) -> None:
        enum1 = MyEnum2.from_value(2)

        assert_that(enum1.value).is_equal_to(2)

    def test_enum_from_name_should_raise_exception_on_invalid_name(self) -> None:
        assert_that(MyEnum.from_name).raises(Exception).when_called_with("invalid_name")    

    def test_enum_from_value_should_raise_exception_on_invalid_value(self) -> None:
        assert_that(MyEnum.from_value).raises(Exception).when_called_with(1000)    

    def test_enum_to_string_should_return_enum_name(self) -> None:
        assert_that(str(MyEnum.One)).is_equal_to('One')
    
    def test_enum_equality_check_should_return_true_for_equal_enums(self) -> None:
        enum1 = MyEnum.from_value(1)
        enum2 = MyEnum2.from_value(1)
        
        result = enum1 != enum2

        assert_that(result).is_true()
