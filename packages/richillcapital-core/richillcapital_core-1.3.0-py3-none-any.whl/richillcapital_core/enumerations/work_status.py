
from ..abstractions import Enumeration


class WorkStatus(Enumeration["WorkStatus"]):
    MAX_LENGTH = 16
    
    Draft: "WorkStatus"
    Opened: "WorkStatus"
    Cancelled: "WorkStatus"
    InProgress: "WorkStatus"
    Closed: "WorkStatus"
    Outdated: "WorkStatus"

    def __init__(self, name: str, value: int) -> None:
        super().__init__(name, value)


WorkStatus.Draft = WorkStatus("Draft", 0)
WorkStatus.Opened = WorkStatus("Opened", 0)
WorkStatus.Cancelled = WorkStatus("Cancelled", 0)
WorkStatus.InProgress = WorkStatus("InProgress", 0)
WorkStatus.InProgress = WorkStatus("InProgress", 0)
WorkStatus.Outdated = WorkStatus("Outdated", 0)
