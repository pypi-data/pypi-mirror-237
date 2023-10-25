from assertpy import assert_that
from richillcapital_core.value_objects import WorkId


class TestWorkId:

    def test_workid_creation(self):
        work_id = WorkId.create("12345")
        assert_that(work_id).is_instance_of(WorkId)
        assert_that(work_id.value).is_equal_to("12345")

    def test_workid_equality(self):
        work_id1 = WorkId.create("12345")
        work_id2 = WorkId.create("12345")
        work_id3 = WorkId.create("67890")

        assert_that(work_id1).is_equal_to(work_id2)
        assert_that(work_id1).is_not_equal_to(work_id3)

    def test_workid_max_length(self):
        max_length = WorkId.MAX_LENGTH
        work_id = WorkId.create("A" * max_length)
        assert_that(work_id.value).is_length(max_length)

    def test_workid_get_equality_components(self):
        work_id = WorkId.create("12345")
        components = work_id.get_equality_components()
        assert_that(components).is_length(1)
        assert_that(components[0]).is_equal_to(work_id.value)
