from datetime import datetime

from .calls import Call
from ..base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from .._sql_types import _created_at, _updated_at

class Result(Base):
    __tablename__ = "results"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    checklist_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("checklists.id"), nullable=False
    )
    
    call_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls.id", ondelete="cascade"), nullable=False)
    call: Mapped["Call"] = relationship(
        back_populates="results"
    )
    
    ratings: Mapped[list["Rating"]] = relationship(
        back_populates="result", cascade="all, delete-orphan"
    )
    
    audio_upload_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    model_applied_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    created_at: Mapped[_created_at]
    updated_at: Mapped[_updated_at]
    
    __table_args__ = (
        UniqueConstraint("call_id", "checklist_id", "model_applied_at", name="uix_call_id_checklist_id_model_applied_at"),
    )