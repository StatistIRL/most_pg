from dataclasses import dataclass, field
from typing import List, Optional, Literal
from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class Call(DataClassJsonMixin):
    most_id: str
    url: str
    source: Optional[str] = None
    duration: Optional[float] = None
    additional_information: Optional[dict] = field(default_factory=dict)