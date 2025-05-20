from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Index

class Checklist(Base):
    __tablename__ = "checklists"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    model_id: Mapped[str] = mapped_column(String, nullable=False, unique=True)