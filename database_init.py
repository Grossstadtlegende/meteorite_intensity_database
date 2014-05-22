import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy import Sequence
import code
import helper

Base = declarative_base()


class Kingdom(Base):
    __tablename__ = 'kingdom'
    id = Column(Integer, primary_key=True, autoincrement=True)
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


    #6.4-8.7% Ni, 55-100 ppm Ga, 190-520 ppm Ge, 0.6-5.5 ppm Ir, Ge-Ni correlation negativ.
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
    def __repr__(self):
        return "<< %s >>" % (self.name)

class Sample(Base):
    __tablename__ = 'samples'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    group_id = Column(Integer, ForeignKey('group.id'))
    # reference_id = Column(Integer, ForeignKey('reference.id'))
    comment = Column(String(250))
    notes = Column(String(250))
    fall = Column(Boolean)

engine = create_engine('sqlite:///meteorite_intensity.db')
# engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

session = helper.connect_db()

''' Kingdoms '''
diff = Kingdom(name='differentiated')
undiff = Kingdom(name='undifferentiated')
general = Kingdom(name='no kingdom')
map(session.add, [diff, undiff, general])
session.commit()
''' Categories '''
chondr = Cat(name='chondrites', kingdom_id=undiff.id)
primitive_achondr = Cat(name='primitive achondrites', kingdom_id=diff.id)
achondr = Cat(name='achondrites', kingdom_id=general.id)

map(session.add, [chondr, achondr, primitive_achondr])
session.commit()
session.flush()

''' Classes '''
''' chondrites '''
carbonaceous_ch = M_Class(name='carbonacious chondrite', cat_id=chondr.id)
ordinary_ch = M_Class(name='ordinary chondrite', cat_id=chondr.id)
enstatite_ch = M_Class(name='enstatite chondrite', cat_id=chondr.id)

kakangari_ch = M_Class(name='kakangari chondrite', cat_id=chondr.id)
rumuruti_ch = M_Class(name='rumuruti chondrite', cat_id=chondr.id)

''' achondrites '''
primitive_ach = M_Class(name='primitive', cat_id=primitive_achondr.id)
achondrites = M_Class(name='primitive', cat_id=achondr.id)

map(session.add,
    [carbonaceous_ch, ordinary_ch, enstatite_ch, kakangari_ch, rumuruti_ch, primitive_ach, achondrites])
session.commit()
session.flush()

''' CLANS '''
CI_clan = Clan(name='CI', m_class_id=carbonaceous_ch.id)
CM_CO_clan = Clan(name='CM-CO', m_class_id=carbonaceous_ch.id)
CV_CK_clan = Clan(name='CV-CK', m_class_id=carbonaceous_ch.id)
CR_clan = Clan(name='CR', m_class_id=carbonaceous_ch.id)
H_L_LL_clan = Clan(name='H-L-LL', m_class_id=ordinary_ch.id)
EH_EL_clan = Clan(name='EH-EL', m_class_id=enstatite_ch.id)
R_clan = Clan(name='R', m_class_id=rumuruti_ch.id)
K_clan = Clan(name='K', m_class_id=kakangari_ch.id)

ureilites_clan = Clan(name='ureilites', m_class_id=primitive_ach.id)
brachinites_clan = Clan(name='brachinites', m_class_id=primitive_ach.id)
ACA_LOD_clan = Clan(name='ACA_LOD', m_class_id=primitive_ach.id)
WIN_IAB_IICD_clan = Clan(name='WIN-IAB-IICD', m_class_id=primitive_ach.id)

angrites_clan = Clan(name='angrites', m_class_id=achondrites.id)
aubrites_clan = Clan(name='aubrites', m_class_id=achondrites.id)
mesosiderites_clan = Clan(name='mesosiderites', m_class_id=achondrites.id)
pallasites_clan = Clan(name='pallasites', m_class_id=achondrites.id)
iron_clan = Clan(name='iron', m_class_id=achondrites.id)
vesta_clan = Clan(name='vesta', m_class_id=achondrites.id)
moon_clan = Clan(name='moon', m_class_id=achondrites.id)
mars_clan = Clan(name='mars', m_class_id=achondrites.id)

map(session.add, [CI_clan, CM_CO_clan, CV_CK_clan, CR_clan, H_L_LL_clan, EH_EL_clan, R_clan, K_clan,
                  ureilites_clan, brachinites_clan, ACA_LOD_clan, WIN_IAB_IICD_clan,
                  angrites_clan, aubrites_clan, mesosiderites_clan, pallasites_clan, iron_clan, vesta_clan, moon_clan,
                  mars_clan])
session.commit()
session.flush()

''' Groups '''

CI = Group(name='CI', clan_id=CI_clan.id)

CM = Group(name='CM', clan_id=CM_CO_clan.id)
CO = Group(name='CO', clan_id=CM_CO_clan.id)

CV = Group(name='CV', clan_id=CV_CK_clan.id)
CK = Group(name='CV', clan_id=CV_CK_clan.id)

CR = Group(name='CR', clan_id=CR_clan.id)
CH = Group(name='CH', clan_id=CR_clan.id)
CB = Group(name='CB', clan_id=CR_clan.id)

H = Group(name='H', clan_id=H_L_LL_clan.id)
L = Group(name='L', clan_id=H_L_LL_clan.id)
LL = Group(name='LL', clan_id=H_L_LL_clan.id)

EH = Group(name='EH', clan_id=EH_EL_clan.id)
EL = Group(name='EL', clan_id=EH_EL_clan.id)

R = Group(name='rumuruti', clan_id=R_clan.id)
K = Group(name='kakangari', clan_id=K_clan.id)

map(session.add, [CI, CM, CO, CV, CK, CR, CH, CB, H, L, LL, EH, EL, R, K])

URE = Group(name='ureilites', clan_id=ureilites_clan.id)
BRA = Group(name='brachinites', clan_id=brachinites_clan.id)

ACA = Group(name='acapulcoites', clan_id=ACA_LOD_clan.id)
LOD = Group(name='lodranite', clan_id=ACA_LOD_clan.id)

WIN = Group(name='winonaite', clan_id=WIN_IAB_IICD_clan.id)
IAB = Group(name='IAB', clan_id=WIN_IAB_IICD_clan.id,
            Ni_min=6.4e-2, Ni_max=25e-2, Ga_min=11e-6, Ga_max=100e-6,
            Ge_min=25e-6, Ge_max=520e-6, Ir_min=0.3e-6, Ir_max=5.5e-6,
            Ge_Ni_correlation='negative')
# IA: Medium and coarse octahedrites, 6.4-8.7% Ni, 55-100 ppm Ga, 190-520 ppm Ge, 0.6-5.5 ppm Ir, Ge-Ni correlation negativ.
# IB: Ataxites and medium octahedrites, 8.7-25% Ni, 11-55 ppm Ga, 25-190 ppm Ge, 0.3-2 ppm Ir, Ge-Ni correlation negativ.
IICD = Group(name='IICD', clan_id=WIN_IAB_IICD_clan.id,
            Ni_min=10e-2, Ni_max=23e-2,
            Ga_min=1.5e-6, Ga_max=27e-6,
            Ge_min=1.4e-6, Ge_max=70e-6,
            Ir_min=0.02e-6, Ir_max=0.55e-6,
            )
#IIICD: Ataxites to fine octahedrites, 10-23% Ni, 1.5-27 ppm Ga, 1.4-70 ppm Ge, 0.02-0.55 ppm Ir

map(session.add, [URE, BRA, ACA, LOD, WIN, IAB, IICD])

ANG = Group(name='angrites', clan_id=angrites_clan.id)
AUB = Group(name='angrites', clan_id=aubrites_clan.id)

EUC = Group(name='EUC', full_name='eucrite', clan_id=vesta_clan.id)
DIO = Group(name='DIO', full_name='diagonite', clan_id=vesta_clan.id)
HOW = Group(name='HOW', full_name='howardite', clan_id=vesta_clan.id)

MES = Group(name='mesosiderite', clan_id=mesosiderites_clan.id)

MGPAL = Group(name='main-group pallasite', clan_id=pallasites_clan.id)
ESPAL = Group(name='eagle station pallasite', clan_id=pallasites_clan.id)
PPPAL = Group(name='pyroxene pallasite', clan_id=pallasites_clan.id)

IC = Group(name='IC', clan_id=iron_clan.id)
IIAB = Group(name='IIAB', clan_id=iron_clan.id,
             Ni_min=5.3e-2, Ni_max=6.4e-2,
             Ge_min=107e-6, Ge_max=183e-6,
             Ir_min=0.01e-6, Ir_max=60e-6,
             Ge_Ni_correlation='negative')
#IIA: Hexahedrites, 5.3-5.7% Ni, 57-62 ppm Ga, 170-185 ppm Ge, 2-60ppm Ir.
#IIB: Coarsest octahedrites, 5.7-6.4% Ni, 446-59 pm Ga, 107-183 ppm Ge, 0.01-0.5 ppm Ir, Ge-Ni correlation negativ.

IIC = Group(name='IIC', full_name='IIC: plessitic octahedrites', clan_id=iron_clan.id,
            Ni_min=9.3e-2, Ni_max=11.5e-2,
            Ga_min=37e-6, Ga_max=39e-6,
            Ge_min=88e-6, Ge_max=114e-6,
            Ir_min=4e-6, Ir_max=11e-6,
            Ge_Ni_correlation='positive')
#IIC: Plessitic octahedrites, 9.3-11.5% Ni, 37-39 ppm Ga, 88-114 ppm Ge, 4-11 ppm Ir, Ge-Ni correlation positiv

IID = Group(name='IID', full_name='IID: fine to medium octahedrites', clan_id=iron_clan.id,
            Ni_min=9.8e-2, Ni_max=11.3e-2,
            Ga_min=70e-6, Ga_max=83e-6,
            Ge_min=82e-6, Ge_max=98e-6,
            Ir_min=3.5e-6, Ir_max=18e-6,
            Ge_Ni_correlation='positive')
#IID: Fine to medium octahedrites, 9.8-11.3%Ni, 70-83 ppm Ga, 82-98 ppm Ge, 3.5-18 ppm Ir, Ge-Ni correlation positiv

IIE = Group(name='IIE', full_name='IIE: octahedrites of various coarseness', clan_id=iron_clan.id,
            Ni_min=7.5e-2, Ni_max=9.7e-2,
            )
#IIE: octahedrites of various coarseness, 7.5-9.7% Ni, 21-28 ppm Ga, 60-75 ppm Ge, 1-8 ppm Ir, Ge-Ni correlation absent
IIIAB = Group(name='IIIAB', full_name='IIIAB: Medium octahedrites', clan_id=iron_clan.id,
               Ni_min=7.1e-2, Ni_max=10.5e-2,
            )
#IIIAB: Medium octahedrites, 7.1-10.5% Ni, 16-23 ppm Ga, 27-47 ppm Ge, 0.01-19 ppm Ir


IIIE = Group(name= 'IIIE', full_name='IIIE: Coarse octahedrites', clan_id=iron_clan.id,
               Ni_min=8.2e-2, Ni_max=9.0e-2,
            )
#IIIE: Coarse octahedrites, 8.2-9.0% Ni, 17-19 ppm Ga, 3-37 ppm Ge, 0.05-6 ppm Ir, Ge-Ni correlation absent
IIIF = Group(name='IIIF', full_name='IIIF: Medium to coarse octahedrites', clan_id=iron_clan.id,
               Ni_min=6.8e-2, Ni_max=7.8e-2,
            )
#IIIF: Medium to coarse octahedrites, 6.8-7.8% Ni,6.3-7.2 ppm Ga, 0.7-1.1 ppm Ge, 1.3-7.9 ppm Ir, Ge-Ni correlation absent
IVA = Group(name='IVA', full_name='IVA: Fine octahedrites', clan_id=iron_clan.id,
               Ni_min=7.4e-2, Ni_max=9.4e-2,
            )
#IVA: Fine octahedrites, 7.4-9.4% Ni, 1.6-2.4 ppm Ga, 0.09-0.14 ppm Ge, 0.4-4 ppm Ir, Ge-Ni correlation positiv

IVB = Group(name='IVB', full_name='IVB: Ataxites', clan_id=iron_clan.id,
               Ni_min=16e-2, Ni_max=26e-2,
            )
#IVB: Ataxites, 16-26% Ni, 0.17-0.27 ppm Ga, 0,03-0,07 ppm Ge, 13-38 ppm Ir, Ge-Ni correlation positiv

map(session.add, [ANG, AUB,
                  EUC, DIO, HOW,
                  MES,
                  MGPAL, ESPAL, PPPAL,
                  IC, IIAB, IIC, IID, IIE, IIIAB, IIIE, IIIF, IVA, IVB])

session.commit()
session.flush()


# print  CI.name, CI.m_class, CI.m_class.category, CI.m_class.category.kingdom