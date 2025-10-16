import os
import pytest

import SecretConfig

# Construir DSN para pruebas
def build_test_dsn():
    user = getattr(SecretConfig, 'PGUSER', None)
    pwd = getattr(SecretConfig, 'PGPASSWORD', None)
    host = getattr(SecretConfig, 'PGHOST', 'localhost')
    port = getattr(SecretConfig, 'PGPORT', '5432')
    db = os.getenv('TEST_PGDATABASE') or getattr(SecretConfig, 'TEST_PGDATABASE', getattr(SecretConfig, 'PGDATABASE', None))
    if not all([user, pwd, db]):
        raise RuntimeError("Configura SecretConfig.py con PGUSER/PGPASSWORD y TEST_PGDATABASE o setea TEST_PGDATABASE env var")
    return f"dbname={db} user={user} password={pwd} host={host} port={port}"

@pytest.fixture(scope='session')
def test_conn():
    dsn = build_test_dsn()
    conn = psycopg2.connect(dsn)
    conn.autocommit = True
    # Crear tablas a nivel sesión (si no existen)
    sql_filename = os.path.join(os.path.dirname(__file__), '..', 'sql', 'crear-tabla.sql')
    # Fallback si ruta relativa diferente:
    if not os.path.exists(sql_filename):
        # buscar en repo raíz sql/crear-tabla.sql
        sql_filename = os.path.join(os.getcwd(), 'sql', 'crear-tabla.sql')
    with open(sql_filename, 'r', encoding='utf-8') as f:
        sql_text = f.read()
    with conn.cursor() as cur:
        cur.execute(sql_text)
    yield conn
    conn.close()

@pytest.fixture()
def db_conn(test_conn):
    # Para aislamiento: abrir una nueva conexión por test y hacer rollback al final.
    # Usar nueva conexión es más seguro que compartir la sesión.
    dsn = test_conn.dsn
    conn = psycopg2.connect(dsn)
    conn.autocommit = False
    try:
        yield conn
    finally:
        conn.rollback()
        conn.close()