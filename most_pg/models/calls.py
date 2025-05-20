
import datetime
from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, JSON
from .._sql_types import _created_at, _updated_at

class Call(Base):
    __tablename__ = "calls"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    most_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=True)
    source: Mapped[str] = mapped_column(String, nullable=True)
    duration: Mapped[float] = mapped_column(Float, nullable=True)
    additional_information: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    
    results: Mapped[list["Result"]] = relationship(
        back_populates="call", cascade="all, delete-orphan"
    )
    
    transcriptions: Mapped[list["Transcription"]] = relationship(
        back_populates="call", cascade="all, delete-orphan"
    )
    
    created_at: Mapped[_created_at]
    updated_at: Mapped[_updated_at]