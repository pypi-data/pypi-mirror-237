from assertpy import assert_that
from richillcapital_core.entities import User
from richillcapital_core.value_objects import Email, UserId


class TestUser:
    def test_create_user(self) -> None:
        email = Email.create("user@example.com")
        user = User.create(email, "John Doe")

        assert_that(user).is_instance_of(User)
        assert_that(user.id).is_instance_of(UserId)
        assert_that(user.email).is_instance_of(Email)
        assert_that(user.name).is_equal_to("John Doe")


