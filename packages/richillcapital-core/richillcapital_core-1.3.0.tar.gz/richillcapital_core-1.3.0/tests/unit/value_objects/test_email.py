import pytest
from assertpy import assert_that
from richillcapital_core.value_objects import Email


class TestEmail:

    def test_create_email(self) -> None:
        email = Email.create("user@example.com")
        
        assert_that(email).is_instance_of(Email)
        assert_that(email.value).is_equal_to("user@example.com")

    def test_equality_components(self) -> None:
        email1 = Email.create("user@example.com")
        email2 = Email.create("user@example.com")
        email3 = Email.create("another@example.com")

        assert_that(email1).is_equal_to(email2)  
        assert_that(email1).is_not_equal_to(email3)  

