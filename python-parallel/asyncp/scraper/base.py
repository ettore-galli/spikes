from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


class IssueType(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class Issue:
    message: str
    data: Optional[Union[int, str]] = None
    issue_type: List[IssueType] = field(default_factory=list)
