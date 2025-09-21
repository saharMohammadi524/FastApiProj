
from uuid import UUID, uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from .engine import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    username: Mapped[str]= mapped_column(String(50),unique=True, nullable=True)
    password: Mapped[str]=mapped_column(String(100),nullable=False)
    
