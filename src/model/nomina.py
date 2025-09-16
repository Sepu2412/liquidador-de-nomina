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
        """
    Clase para calcular la nómina de un empleado con base en su salario, 
    días laborados, horas extra y bonificaciones.
    """

    def __init__(self, salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion=0):
        self.salario_base = salario_base
        self.dias_laborados = dias_laborados
        self.horas_extra_diurnas = horas_extra_diurnas
        self.horas_extra_nocturnas = horas_extra_nocturnas
        self.bonificacion = bonificacion
                """
        Inicializa una nueva instancia de LiquidadorNomina.

        Parámetros:
        - salario_base (float): Salario mensual del empleado.
        - dias_laborados (int): Número de días efectivamente laborados.
        - horas_extra_diurnas (int): Total de horas extra diurnas trabajadas.
        - horas_extra_nocturnas (int): Total de horas extra nocturnas trabajadas.
        - bonificacion (float): Bonificación adicional (opcional).
        """

        self._validar_datos()

    def _validar_datos(self):
    """
    Valida los datos de entrada del empleado. 
    Lanza excepciones personalizadas si los valores son inválidos.
    
    Errores posibles:
    - ErrorSalarioBase: Si el salario base es menor o igual a 0.
    - ErrorDiasLaborados: Si los días laborados no están entre 0 y 30.
    - ErrorHorasExtras: Si las horas extras son negativas.
    - ErrorHorasExtrasMaximas: Si la suma de horas extras excede el máximo permitido.
    """
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
            """
    Calcula el salario proporcional al número de días laborados.
    
    Retorna:
    - float: Salario base proporcional.
    """
        return (self.salario_base / 30) * self.dias_laborados

    def _calcular_auxilio_transporte(self):
             """
    Calcula el auxilio de transporte si aplica, de acuerdo con el salario base y días trabajados.

    Retorna:
    - float: Valor del auxilio de transporte.
    """
        if self.salario_base < 2 * SALARIO_MINIMO and self.dias_laborados > 0:
            return (AUXILIO_TRANSPORTE / 30) * self.dias_laborados
        return 0

    def _calcular_valor_hora(self):
            """
    Calcula el valor de una hora laboral según el salario base mensual.

    Retorna:
    - float: Valor por hora de trabajo.
    """
        return self.salario_base / HORAS_MES

    def _calcular_horas_extras(self):
            """
    Calcula el valor total de las horas extra diurnas y nocturnas.

    Retorna:
    - tuple(float, float): Valor total por horas extra diurnas y nocturnas.
    """
        valor_hora = self._calcular_valor_hora()
        diurnas = self.horas_extra_diurnas * valor_hora * 1.25
        nocturnas = self.horas_extra_nocturnas * valor_hora * 1.75
        return diurnas, nocturnas
    # hora_diurna_recargo == 1.25
    # hora_diurna_recargo == 1.75




    def _calcular_deducciones(self, total_devengado):
    """
    Calcula las deducciones por salud y pensión sobre el total devengado.

    Parámetros:
    - total_devengado (float): Suma total antes de deducciones.

    Retorna:
    - tuple(float, float): Deducción por salud y por pensión.
    """
        salud = total_devengado * 0.04
        pension = total_devengado * 0.04
        return salud, pension

    def liquidar(self):
            """
    Realiza el proceso completo de liquidación de nómina, incluyendo salario, 
    auxilio, horas extras, bonificaciones y deducciones.

    Retorna:
    - dict: Contiene salario base, auxilio, horas extras, bonificación, deducciones y salario neto.
    """
        salario = self._calcular_salario_base()
        auxilio = self._calcular_auxilio_transporte()
        extras_diurnas, extras_nocturnas = self._calcular_horas_extras()

        total_devengado = salario + auxilio + extras_diurnas + extras_nocturnas + self.bonificacion
        deduccion_salud, deduccion_pension = self._calcular_deducciones(total_devengado)
        total_deducciones = deduccion_salud + deduccion_pension
        salario_neto = total_devengado - total_deducciones

        return salario_neto
