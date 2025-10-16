import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.model.excepciones import (
    ErrorSalarioBase,
    ErrorDiasLaborados,
    ErrorHorasExtras,
    ErrorHorasExtrasMaximas
)
from src.model.nomina import LiquidadorNomina

def interfaz_consola():
    print("Liquidador de Nómina")
    try:
        salario_base = float(input("Ingrese salario base: "))
        dias_laborados = int(input("Ingrese días laborados (0-30): "))
        horas_extra_diurnas = int(input("Ingrese horas extras diurnas: "))
        horas_extra_nocturnas = int(input("Ingrese horas extras nocturnas: "))
        bonificacion = float(input("Ingrese valor bonificación (0 si no hay): "))

        liquidador = LiquidadorNomina(
            salario_base,
            dias_laborados,
            horas_extra_diurnas,
            horas_extra_nocturnas,
            bonificacion
        )

        salario_neto = liquidador.liquidar()
        print(f"\n Total a pagar (Salario Neto): ${salario_neto:,.2f}")

    except ValueError:
        print(" Error: Debe ingresar valores numéricos.")
    except (ErrorSalarioBase, ErrorDiasLaborados, ErrorHorasExtras, ErrorHorasExtrasMaximas) as e:
        print(f" {e}")
    except Exception as e:
        print(f" Error inesperado: {e}")
if __name__ == "__main__":
    interfaz_consola()

# Interfaz de consola simple que usa el controller 
from src.controller.controller_empleado import EmpleadoController
from src.model.clase_empleado import Empleado
from datetime import datetime

def main():
    controller = EmpleadoController()
    while True:
        print("\n1) Insertar\n2) Buscar\n3) Modificar\n4) Borrar\n5) Salir")
        op = input("Opción: ").strip()
        if op == "1":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            fecha = input("Fecha de ingreso (YYYY-MM-DD): ")
            salario = input("Salario base: ")
            fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
            emp = Empleado(id=None, nombre=nombre, cedula=cedula, fecha_ingreso=fecha_dt, salario_base=float(salario))
            inserted = controller.insertar(emp)
            print("Insertado:", inserted)
        elif op == "2":
            cedula = input("Cédula: ")
            emp = controller.buscar_por_cedula(cedula)
            print(emp if emp else "No encontrado.")
        elif op == "3":
            cedula = input("Cédula a modificar: ")
            nuevo_salario = input("Nuevo salario (enter para omitir): ").strip()
            nombre = input("Nuevo nombre (enter para omitir): ").strip()
            update_kwargs = {}
            if nuevo_salario:
                update_kwargs['salario_base'] = float(nuevo_salario)
            if nombre:
                update_kwargs['nombre'] = nombre
            emp = controller.modificar_por_cedula(cedula, **update_kwargs)
            print("Modificado:" , emp if emp else "No encontrado o sin cambios.")
        elif op == "4":
            cedula = input("Cédula a borrar: ")
            ok = controller.borrar_por_cedula(cedula)
            print("Borrado." if ok else "No encontrado.")
        elif op == "5":
            break

if __name__ == "__main__":
    main()