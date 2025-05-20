import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column

_created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())"), nullable=False),
]

_updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        nullable=False,
        onupdate=datetime.datetime.utcnow(),
    ),
]