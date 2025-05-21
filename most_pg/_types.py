from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import DataClassJsonMixin, dataclass_json
from typing import TypedDict

@dataclass_json
@dataclass
class Call(DataClassJsonMixin):
    most_id: str
    url: str
    source: Optional[str] = None
    duration: Optional[float] = None
    additional_information: Optional[dict] = field(default_factory=dict)
    

class CallUpdateDict(TypedDict, total=False):
    most_id: str
    url: str | None
    source: str | None
    duration: float | None
    additional_information: dict
