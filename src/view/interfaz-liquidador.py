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
