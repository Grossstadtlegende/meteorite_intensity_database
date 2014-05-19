import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import code

Base = declarative_base()

class Kingdom(Base):
    __tablename__ = 'kingdom'
    id = Column(Integer, primary_key=True)
    m_kingdom = Column(String(250))

class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    m_class = Column(String(250))
    kingdom_id = Column(Integer, ForeignKey('kingdom.id'))

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    m_order = Column(String(250))
    class_id = Column(Integer, ForeignKey('class.id'))

class Family(Base):
    __tablename__ = 'family'
    id = Column(Integer, primary_key=True)
    m_family = Column(String(250))
    order_id = Column(Integer, ForeignKey('order.id'))

class Meteorite(Base):
    __tablename__ = 'meteorites'
    id = Column(Integer, primary_key=True)
    meteorite_family = Column(Integer, ForeignKey('family.id'))

class Reference(Base):
    __tablename__ = 'reference'
    id = Column(Integer, primary_key=True)
    reference = Column(String(250))

class Sample(Base):
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    sample_name = Column(String(250), nullable=False)
    meteorite_id = Column(Integer, ForeignKey('meteorites.id'))

class Method(Base):
    __tablename__ = 'method'
    id = Column(Integer, primary_key=True)
    pint_method = Column(String(250), nullable=False)



engine = create_engine('sqlite:///meteorite_intensity.db')
Base.metadata.create_all(engine)