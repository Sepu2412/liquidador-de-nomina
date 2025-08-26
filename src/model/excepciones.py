class ErrorSalarioBase(Exception):
    """Error cuando el salario base es menor o igual a cero"""
    def __init__(self, salario):
        self.salario = salario
        super().__init__(f"Error: El salario base ({salario}) debe ser mayor que cero.")


class ErrorDiasLaborados(Exception):
    """Error cuando los días laborados son inválidos"""
    def __init__(self, dias):
        self.dias = dias
        super().__init__(f"Error: Los días laborados ({dias}) deben estar entre 0 y 30.")


class ErrorHorasExtras(Exception):
    """Error cuando las horas extras son negativas"""
    def __init__(self, horas):
        self.horas = horas
        super().__init__(f"Error: Las horas extras ({horas}) no pueden ser negativas.")


class ErrorHorasExtrasMaximas(Exception):
    def __init__(self, total_horas):
        super().__init__(f"Error: Las horas extras no pueden superar las 48 horas mensuales. Total ingresado: {total_horas}")
