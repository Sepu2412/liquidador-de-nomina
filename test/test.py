import unittest
from src.model.nomina import calcular_nomina
import unittest
import sys
sys.path.append("src")

from model.calcular_nomina import nomina
from model.excepciones import *

from src.model.excepciones import ErrorSalarioBase, ErrorDiasLaborados, ErrorHorasExtras


class TestLiquidadorNomina(unittest.TestCase):

    def test_normal_1(self):
        self.assertEqual(calcular_nomina(1500000, 30, 5,0,), 1701062.5)

    def test_normal_2(self):
        self.assertEqual(calcular_nomina(1200000, 20, 0,0), 908000.0)

    def test_normal_3(self):
        self.assertEqual(calcular_nomina(1000000, 15, 10,0), 633083.33)

    """
    def test_error_1(self):
        self.assertIsNone(calcular_nomina(1500000, 37, 5))

    def test_error_2(self):
        salario_base = 1500000
        horas_extras = 5
        dias_laborados = 10

        with self.assertRaises(ErrorDiasLaborados):
            nomina = calcular_nomina(salario_base, dias_laborados, horas_extras)

    def test_caso_normal_1(self):
        salario_base = 1500000
        horas_extras = 5
        dias_laborados = 30
        salario_esperado = 1539062.5

        nomina = calcular_nomina(salario_base, dias_laborados, horas_extras)

        self.assertAlmostEqual(salario_esperado, nomina, 2)

    def prueba_extraordinaria_1(self):
        salario = 10000000
        dias = 30
        horas = 50
        resultado = calcular_nomina(salario, dias, horas)
        esperado = 11354166.67"""


if __name__ == "__main__":
    unittest.main()

