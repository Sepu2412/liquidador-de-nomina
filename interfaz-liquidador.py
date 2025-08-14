from excepciones import ErrorSalarioBase, ErrorDiasLaborados, ErrorHorasExtras
from nomina import calcular_nomina


def interfaz_consola():
    print("Liquidador de Nómina ")
    try:
        salario_base = float(input("Ingrese salario base: "))
        dias_laborados = int(input("Ingrese días laborados (0-30): "))
        horas_extra_diurnas = int(input("Ingrese horas extras diurnas: "))
        horas_extra_nocturnas = int(input("Ingrese horas extras nocturnas: "))
        bonificacion = float(input("Ingrese valor bonificación (0 si no hay): "))

        total = calcular_nomina(salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion)
        print(f"\n Total a pagar: ${total:,.2f}")

    except ValueError:
        print(" Error: Debe ingresar valores numéricos.")
    except (ErrorSalarioBase, ErrorDiasLaborados, ErrorHorasExtras) as e:
        print(f" {e}")
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    interfaz_consola()