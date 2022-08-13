from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from flask_session import Session

curPath = os.path.dirname(__file__)

engine = create_engine(
    'sqlite:///{}/data.db?check_same_thread=False'.format(curPath),
    convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
    print('Already Connected!!!')
