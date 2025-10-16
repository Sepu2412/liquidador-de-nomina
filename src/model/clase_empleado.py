
from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Empleado:
    id: Optional[int]
    nombre: str
    cedula: str
    fecha_ingreso: date
    salario_base: float

    @staticmethod
    def from_row(row):
        # row is a tuple or dict-like depending on cursor; here we expect tuple in order
        # If using RealDictCursor, row can be dict-like; handle both.
        if row is None:
            return None
        try:
            # If row supports keys
            return Empleado(
                id=row.get('id'),
                nombre=row.get('nombre'),
                cedula=row.get('cedula'),
                fecha_ingreso=row.get('fecha_ingreso'),
                salario_base=float(row.get('salario_base')),
            )
        except Exception:
            # Fallback for tuple row: (id, nombre, cedula, fecha_ingreso, salario_base)
            return Empleado(
                id=row[0],
                nombre=row[1],
                cedula=row[2],
                fecha_ingreso=row[3],
                salario_base=float(row[4]),
            )

    def is_equal(self, other):
        if other is None:
            return False
        return (
            self.nombre == other.nombre and
            self.cedula == other.cedula and
            self.fecha_ingreso == other.fecha_ingreso and
            float(self.salario_base) == float(other.salario_base)
        )