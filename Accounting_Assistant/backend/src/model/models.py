from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Float, Integer, ForeignKey, CheckConstraint, UniqueConstraint

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        CheckConstraint("email LIKE '%@%.%'"),
        UniqueConstraint('email'),
        UniqueConstraint('name')
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)


