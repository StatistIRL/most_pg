from .results import Result
from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, Text, String
from .._sql_types import _created_at, _updated_at
from sqlalchemy.orm import relationship

class Rating(Base):
    __tablename__ = "ratings"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    stage: Mapped[str] = mapped_column(String, nullable=True)
    criterion: Mapped[str] = mapped_column(String, nullable=True)
    score: Mapped[int] = mapped_column(Integer, nullable=True)
    score_modified: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    criterion_number: Mapped[int] = mapped_column(Integer, nullable=True)

    result_id: Mapped[int] = mapped_column(Integer, ForeignKey("results.id", ondelete="cascade"), nullable=False)
    result: Mapped["Result"] = relationship(
        back_populates="ratings"
    )
    
    created_at: Mapped[_created_at]
    updated_at: Mapped[_updated_at]