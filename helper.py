__author__ = 'mike'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

def connect_db(db_name='sqlite:///meteorite_intensity.db', echo=True):

    log = logging.getLogger(name='Meteorite.database')
    log.info('connecting to database << %s >>' %db_name)
    engine = create_engine(db_name)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def add_if_not_exists(session, table, entries, **kwargs):
    '''
    Checks if the name of the entry exists in the model and adds if it does
    :param session:
    :param table:
    :param entries:
    :param kwargs:
    :return:
    '''

    for entry in entries:
        if not session.query(table).filter(table.name == entry.name).count():
            session.add(entry)
        else:
            print('<< {} >> entry already in database {}'.format(entry.name, table.__tablename__))