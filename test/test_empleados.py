from datetime import date
from src.model.clase_empleado import Empleado
from src.controller.controller_empleado import EmpleadoController

def test_insertar_y_buscar(db_conn):
    controller = EmpleadoController(conn=db_conn)
    emp = Empleado(id=None, nombre="Juan", cedula="J-111", fecha_ingreso=date(2024,1,1), salario_base=1000000.00)
    inserted = controller.insertar(emp)
    assert inserted.id is not None
    found = controller.buscar_por_cedula("J-111")
    assert found is not None
    assert found.cedula == "J-111"
    assert found.is_equal(emp)

def test_modificar_y_buscar(db_conn):
    controller = EmpleadoController(conn=db_conn)
    emp = Empleado(id=None, nombre="Ana", cedula="A-200", fecha_ingreso=date(2024,2,2), salario_base=1200000.00)
    controller.insertar(emp)
    controller.modificar_por_cedula("A-200", salario_base=1300000.00)
    updated = controller.buscar_por_cedula("A-200")
    assert float(updated.salario_base) == 1300000.00

def test_borrar(db_conn):
    controller = EmpleadoController(conn=db_conn)
    emp = Empleado(id=None, nombre="Borrar", cedula="BOR-99", fecha_ingreso=date(2024,3,3), salario_base=500000.00)
    controller.insertar(emp)
    ok = controller.borrar_por_cedula("BOR-99")
    assert ok is True
    assert controller.buscar_por_cedula("BOR-99") is None