

from datetime import datetime

from assertpy import assert_that
from richillcapital_core.entities import Work
from richillcapital_core.value_objects import WorkId


class TestWork:

    def test_work_creation(self):
        work_id = WorkId.create("12345")
        title = "Sample Title"
        specification = "Sample Specification"
        budget = 1000.0
        expire_time = datetime(2023, 10, 31)

        work = Work(work_id, title, specification, budget, expire_time)

        assert_that(work).is_instance_of(Work)
        assert_that(work.id).is_equal_to(work_id)
        assert_that(work.title).is_equal_to(title)
        assert_that(work.specification).is_equal_to(specification)
        assert_that(work.budget).is_equal_to(budget)
        assert_that(work.expire_time).is_equal_to(expire_time)

    def test_work_create_method(self):
        title = "Sample Title"
        specification = "Sample Specification"
        budget = 1000.0
        expire_time = datetime(2023, 10, 31)

        work = Work.create(title, specification, budget, expire_time)

        assert_that(work).is_instance_of(Work)
        assert_that(work.id).is_instance_of(WorkId)
        assert_that(work.title).is_equal_to(title)
        assert_that(work.specification).is_equal_to(specification)
        assert_that(work.budget).is_equal_to(budget)
        assert_that(work.expire_time).is_equal_to(expire_time)
