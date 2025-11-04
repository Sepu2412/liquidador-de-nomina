import os
from datetime import date


from src.model.clase_empleado import Empleado
import SecretConfig  # usa SecretConfig.py 

def build_conn_from_secretconfig(dbname=None):
    db = dbname or getattr(SecretConfig, 'PGDATABASE', None)
    user = getattr(SecretConfig, 'PGUSER', None)
    pwd = getattr(SecretConfig, 'PGPASSWORD', None)
    host = getattr(SecretConfig, 'PGHOST', 'localhost')
    port = getattr(SecretConfig, 'PGPORT', '5432')
    if not all([db, user, pwd]):
        # también permite cadena en variable de entorno DATABASE_URL
        env = os.getenv('DATABASE_URL')
        if env:
            return psycopg2.connect(env)
        raise RuntimeError("Define SecretConfig.py con PGDATABASE/PGUSER/PGPASSWORD o la var de entorno DATABASE_URL")
    dsn = f"dbname={db} user={user} password={pwd} host={host} port={port}"
    return psycopg2.connect(dsn)

class EmpleadoController:
    def __init__(self, conn=None):
        # conn es una conexión psycopg2. Si no, la creamos desde SecretConfig
        self.conn = conn or build_conn_from_secretconfig()

    def insertar(self, empleado: Empleado) -> Empleado:
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO empleado (nombre, cedula, fecha_ingreso, salario_base)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
                """,
                (empleado.nombre, empleado.cedula, empleado.fecha_ingreso, empleado.salario_base)
            )
            row = cur.fetchone()
            self.conn.commit()
            empleado.id = row['id']
            return empleado

    def buscar_por_cedula(self, cedula: str) -> Empleado:
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT id, nombre, cedula, fecha_ingreso, salario_base FROM empleado WHERE cedula = %s", (cedula,))
            row = cur.fetchone()
            return Empleado.from_row(row)

    def borrar_por_cedula(self, cedula: str) -> bool:
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM empleado WHERE cedula = %s RETURNING id", (cedula,))
            row = cur.fetchone()
            self.conn.commit()
            return row is not None

    def modificar_por_cedula(self, cedula: str, **kwargs) -> Empleado:
        # Permitir modificar solo campos permitidos
        allowed = {'nombre', 'fecha_ingreso', 'salario_base'}
        set_parts = []
        values = []
        for k, v in kwargs.items():
            if k in allowed:
                set_parts.append(f"{k} = %s")
                values.append(v)
        if not set_parts:
            return None
        values.append(cedula)
        sql = f"UPDATE empleado SET {', '.join(set_parts)} WHERE cedula = %s RETURNING id, nombre, cedula, fecha_ingreso, salario_base"
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(sql, tuple(values))
            row = cur.fetchone()
            self.conn.commit()
            return Empleado.from_row(row)
