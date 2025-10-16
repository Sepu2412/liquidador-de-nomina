import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import secret_config
from model_empleado import Base, Empleado

TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL', secret_config.TEST_DATABASE_URL)

@pytest.fixture(scope='session')
def engine():
    eng = create_engine(TEST_DATABASE_URL)
    return eng

@pytest.fixture(scope='session')
def tables(engine):
    # Crear las tablas al inicio de la sesión de tests
    Base.metadata.create_all(engine)
    yield
    # Borrar las tablas al final si se desea
    Base.metadata.drop_all(engine)

@pytest.fixture()
def db_session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()