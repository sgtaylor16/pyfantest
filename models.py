from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, ForeignKey
from typing import Optional, List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = "sqlite:///testdb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass 

class Instro(Base):
    __tablename__ = "instro"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(30))
    dataRange: Mapped[Optional[str]] = mapped_column(String(30)) 
    part: Mapped[str] = mapped_column(String(30))
    masterNumber: Mapped[int] = mapped_column(Integer)
    unit: Mapped[Optional[str]]= mapped_column(String(30))
    r : Mapped[Optional[float]] = mapped_column(Float)
    theta : Mapped[Optional[float]] = mapped_column(Float)
    z : Mapped[Optional[float]] = mapped_column(Float)
    
    instropurpose: Mapped[List["InstroPurpose"]] = relationship(back_populates="instro")
    
class Purpose(Base):
    __tablename__ = "purpose"
    id: Mapped[int] = mapped_column(primary_key=True)
    purpose: Mapped[str] = mapped_column(String(30))
    
    instropurpose: Mapped[List["InstroPurpose"]] = relationship(back_populates="purpose")
    
class InstroPurpose(Base):
    __tablename__ ="InstroPurpose"
    id: Mapped[int] = mapped_column(primary_key=True)
    instroid: Mapped[int] = mapped_column(ForeignKey("instro.id"))
    purposeid: Mapped[int] = mapped_column(ForeignKey("purpose.id"))
    
    instro:Mapped[Instro] = relationship(back_populates="instropurpose")
    purpose:Mapped[Purpose] = relationship(back_populates="instropurpose")
    
""" 
class Setup(Base):
    __tablename__ = "Setup"
    id: Mapped[int] = mapped_column(primary_key=True)
    inlet:Mapped[str] = mapped_column(String(30))
    ct:Mapped[str] = mapped_column(String(30))
    
class Map(Base):
    __tablename__="" """