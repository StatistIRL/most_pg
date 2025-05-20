
from .calls import Call
from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, Text
from .._sql_types import _created_at, _updated_at
from sqlalchemy.orm import relationship

class Transcription(Base):
    __tablename__ = "transcriptions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    
    call_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls.id", ondelete="cascade"), nullable=False)
    call: Mapped["Call"] = relationship(
        back_populates="transcriptions"
    )
    
    created_at: Mapped[_created_at]
    updated_at: Mapped[_updated_at]