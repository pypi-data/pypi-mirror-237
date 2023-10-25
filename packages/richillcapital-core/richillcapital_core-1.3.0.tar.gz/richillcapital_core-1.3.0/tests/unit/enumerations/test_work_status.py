from assertpy import assert_that
from richillcapital_core.enumerations import WorkStatus


class TestWorkStatus:

    def test_workstatus_instance(self):
        draft = WorkStatus.Draft
        assert_that(draft).is_instance_of(WorkStatus)
        assert_that(draft.name).is_equal_to("Draft")
        assert_that(draft.value).is_equal_to(0)

    def test_workstatus_equality(self):
        draft1 = WorkStatus.Draft
        draft2 = WorkStatus.Draft
        opened = WorkStatus.Opened

        assert_that(draft1).is_equal_to(draft2)
        assert_that(draft1).is_not_equal_to(opened)