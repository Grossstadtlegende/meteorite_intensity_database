__author__ = 'mike'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

def connect_db(db_name='sqlite:///meteorite_intensity.db', echo=True):

    log = logging.getLogger(name='RockPy.database')
    log.info('connecting to database << %s >>' %db_name)
    engine = create_engine(db_name)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session