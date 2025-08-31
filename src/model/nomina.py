import sys
sys.path.append("src")
from src.model.excepciones import (
    ErrorSalarioBase,
    ErrorDiasLaborados,
    ErrorHorasExtras,
    ErrorHorasExtrasMaximas
)

SALARIO_MINIMO = 1300000
AUXILIO_TRANSPORTE = 162000
HORAS_MES = 240
HORAS_EXTRAS_MAXIMAS = 48

class LiquidadorNomina:
    def __init__(self, salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion=0):
        self.salario_base = salario_base
        self.dias_laborados = dias_laborados
        self.horas_extra_diurnas = horas_extra_diurnas
        self.horas_extra_nocturnas = horas_extra_nocturnas
        self.bonificacion = bonificacion

        self._validar_datos()

    def _validar_datos(self):
        if self.salario_base <= 0:
            raise ErrorSalarioBase("El salario base debe ser mayor a 0.")
        if not (0 <= self.dias_laborados <= 30):
            raise ErrorDiasLaborados("Los días laborados deben estar entre 0 y 30.")
        if self.horas_extra_diurnas < 0 or self.horas_extra_nocturnas < 0:
            raise ErrorHorasExtras("Las horas extras no pueden ser negativas.")

        total_extras = self.horas_extra_diurnas + self.horas_extra_nocturnas
        if total_extras > HORAS_EXTRAS_MAXIMAS:
            raise ErrorHorasExtrasMaximas(total_extras)

    def _calcular_salario_base(self):
        return (self.salario_base / 30) * self.dias_laborados

    def _calcular_auxilio_transporte(self):
        if self.salario_base < 2 * SALARIO_MINIMO and self.dias_laborados > 0:
            return (AUXILIO_TRANSPORTE / 30) * self.dias_laborados
        return 0

    def _calcular_valor_hora(self):
        return self.salario_base / HORAS_MES

    def _calcular_hora_extras(self):
        valor_hora = self._calcular_valor_hora()
        diurnas = self.horas_extra_diurnas * valor_hora * 1.25
        nocturnas = self.horas_extra_nocturnas * valor_hora * 1.75
        return diurnas, nocturnas
    # hora_diurna_recargo == 1.25
    # hora_diurna_recargo == 1.75




    def _calcular_deducciones(self, total_devengado):
        salud = total_devengado * 0.04
        pension = total_devengado * 0.04
        return salud, pension

    def liquidar(self):
        salario = self._calcular_salario_base()
        auxilio = self._calcular_auxilio_transporte()
        extras_diurnas, extras_nocturnas = self._calcular_extras()

        total_devengado = salario + auxilio + extras_diurnas + extras_nocturnas + self.bonificacion
        deduccion_salud, deduccion_pension = self._calcular_deducciones(total_devengado)
        total_deducciones = deduccion_salud + deduccion_pension
        salario_neto = total_devengado - total_deducciones

        return salario_neto
