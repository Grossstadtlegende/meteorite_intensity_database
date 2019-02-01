from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean

from sqlalchemy import exc
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy import Sequence

Base = declarative_base()
engine = create_engine('sqlite:///meteorite_intensity.db')
# engine = create_engine('sqlite:///:memory:')

class Kingdom(Base):
    __tablename__ = 'kingdom'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    comment = Column(String(250))
    notes = Column(String(250))
    # reference_id = Column(Integer, ForeignKey('reference.id'))
    categories = relationship("Cat", backref=backref("kingdom"))

    def __repr__(self):
        return "<< %s >>" % (self.name)


class Cat(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    comment = Column(String(250))
    notes = Column(String(250))
    kingdom_id = Column(Integer, ForeignKey('kingdom.id'))
    # reference_id = Column(Integer, ForeignKey('reference.id'))
    # orders = relationship("Order", backref="classes", lazy='joined')
    orders = relationship("M_Class", backref=backref('category'))

    def __repr__(self):
        return "<< %s >>" % (self.name)


class M_Class(Base):
    __tablename__ = 'm_class'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    comment = Column(String(250))
    notes = Column(String(250))
    cat_id = Column(Integer, ForeignKey('category.id'))
    clans = relationship("Clan", backref=backref('m_class'))

    # reference_id = Column(Integer, ForeignKey('reference.id'))

    def __repr__(self):
        return "<< %s >>" % (self.name)


class Clan(Base):
    __tablename__ = 'clan'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    m_class_id = Column(Integer, ForeignKey('m_class.id'))
    # reference_id = Column(Integer, ForeignKey('reference.id'))
    groups = relationship("Group", backref=backref('clan'))

    def __repr__(self):
        return "<< %s >>" % (self.name)


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    full_name = Column(String(250))
    comment = Column(String(250))
    notes = Column(String(250))
    clan_id = Column(Integer, ForeignKey('clan.id'))
    m_class_id = Column(Integer, ForeignKey('m_class.id'))
    Ni_min = Column(Float)
    Ni_max = Column(Float)
    Ga_min = Column(Float)
    Ga_max = Column(Float)
    Ge_min = Column(Float)
    Ge_max = Column(Float)
    Ir_min = Column(Float)
    Ir_max = Column(Float)
    Ge_Ni_correlation = Column(String(250))
    meteorites = relationship("Meteorite", backref=backref('group'))

    # 6.4-8.7% Ni, 55-100 ppm Ga, 190-520 ppm Ge, 0.6-5.5 ppm Ir, Ge-Ni correlation negativ.
    # reference_id = Column(Integer, ForeignKey('reference.id'))

    def __repr__(self):
        return "<< %s >>" % (self.name)


class Meteorite(Base):
    __tablename__ = 'meteorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    group_id = Column(Integer, ForeignKey('group.id'))
    # reference_id = Column(Integer, ForeignKey('reference.id'))
    comment = Column(String(250))
    notes = Column(String(250))
    fall = Column(Boolean)
    magnetic_carriers = Column(String(250))
    iron_content = Column(Float)  #
    shock_stage = Column(String(10))
    fall_date = Column(String(250))
    subgroup = Column(String(250))
    meteorites = relationship("Sample", backref=backref('meteorite'))

    def __repr__(self):
        return "<< %s >>" % (self.name)


class Sample(Base):
    __tablename__ = 'samples'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    meteorite_id = Column(Integer, ForeignKey('meteorites.id'))
    # reference_id = Column(Integer, ForeignKey('reference.id'))
    comment = Column(String(250))
    notes = Column(String(250))
    intensity = Column(Float)  # always stored in T
    intensity_error = Column(Float)  # always stored in T
    lab_field = Column(Float)  # always stored in T
    fit_t_min = Column(Float)
    fit_t_max = Column(Float)
    determination_type = Column(String(250))
    citekey = Column(String(250))
    vacuum = Column(String(250))
    inert_gas = Column(String(250))

Base.metadata.create_all(engine)