import pytest
from assertpy import assert_that
from richillcapital_core.value_objects import UserId


class TestUserId():

    def test_create_user_id(self) -> None:
        user_id = UserId.create("user123")
        assert_that(user_id).is_instance_of(UserId)
        assert_that(user_id.value).is_equal_to("user123")

    def test_equality_components(self) -> None:
        user_id1 = UserId.create("user123")
        user_id2 = UserId.create("user123")
        user_id3 = UserId.create("user456")

        assert_that(user_id1).is_equal_to(user_id2)  
        assert_that(user_id1).is_not_equal_to(user_id3)  
