import pytest
from model_empleado import Empleado
from controller_empleado import EmpleadoController

@pytest.mark.parametrize("nombre,cedula,fecha,salario", [
    ("Ana", "A-100", "2024-01-01", 1000000.00),
    ("Luis", "L-200", "2024-02-02", 2000000.00),
    ("Marta", "M-300", "2024-03-03", 3000000.00),
])
def test_insertar_empleados(db_session, nombre, cedula, fecha, salario):
    controller = EmpleadoController(session=db_session)
    empleado = Empleado(nombre=nombre, cedula=cedula, fecha_ingreso=fecha, salario_base=salario)
    inserted = controller.insertar(empleado)
    assert inserted.id is not None

@pytest.mark.parametrize("nombre,cedula,fecha,salario", [
    ("Ana", "A-100", "2024-01-01", 1000000.00),
    ("Luis", "L-200", "2024-02-02", 2000000.00),
    ("Marta", "M-300", "2024-03-03", 3000000.00),
])
def test_buscar_empleados(db_session, nombre, cedula, fecha, salario):
    controller = EmpleadoController(session=db_session)
    # Insertar para asegurar que exista
    emp = Empleado(nombre=nombre, cedula=cedula, fecha_ingreso=fecha, salario_base=salario)
    controller.insertar(emp)
    buscado = controller.buscar_por_cedula(cedula)
    assert buscado is not None
    assert buscado.cedula == cedula

@pytest.mark.parametrize("cedula, nuevo_salario", [
    ("A-100", 1100000.00),
    ("L-200", 2100000.00),
    ("M-300", 3100000.00),
])
def test_modificar_empleados(db_session, cedula, nuevo_salario):
    controller = EmpleadoController(session=db_session)
    # Insertar registro base
    base = Empleado(nombre="Temp", cedula=cedula, fecha_ingreso="2024-01-01", salario_base=1000000.00)
    controller.insertar(base)
    updated = controller.modificar_por_cedula(cedula, salario_base=nuevo_salario)
    assert updated is not None
    assert float(updated.salario_base) == float(nuevo_salario)

def test_borrar_empleado(db_session):
    controller = EmpleadoController(session=db_session)
    emp = Empleado(nombre="Borrar", cedula="BOR-1", fecha_ingreso="2024-01-01", salario_base=500000.00)
    controller.insertar(emp)
    ok = controller.borrar_por_cedula("BOR-1")
    assert ok is True
    assert controller.buscar_por_cedula("BOR-1") is None