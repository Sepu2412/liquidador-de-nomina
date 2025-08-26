import unittest
from src.model.nomina import LiquidadorNomina
from src.model.excepciones import (
    ErrorSalarioBase,
    ErrorDiasLaborados,
    ErrorHorasExtras,
    ErrorHorasExtrasMaximas
)

class TestLiquidadorNomina(unittest.TestCase):



    def test_normal_1(self):
        liquidador = LiquidadorNomina(1500000, 30, 5, 0)
        self.assertAlmostEqual(liquidador.liquidar(), 1701062.5, places=1)

    def test_normal_2(self):
        liquidador = LiquidadorNomina(1200000, 20, 0, 0)
        self.assertAlmostEqual(liquidador.liquidar(), 908000.0, places=1)

    def test_normal_3(self):
        liquidador = LiquidadorNomina(1000000, 15, 10, 0)
        self.assertAlmostEqual(liquidador.liquidar(), 633083.33, places=1)

    def test_extraordinario_1(self):
        liquidador = LiquidadorNomina(3000000, 30, 24, 24)  # Total 48 horas extra
        self.assertTrue(liquidador.liquidar() > 0)

    def test_extraordinario_2(self):
        liquidador = LiquidadorNomina(1300000, 30, 0, 0, bonificacion=500000)
        self.assertTrue(liquidador.liquidar() > 1800000)

    def test_extraordinario_3(self):
        liquidador = LiquidadorNomina(2600000, 1, 0, 0)
        self.assertAlmostEqual(liquidador.liquidar(), (2600000 / 30) * 0.92, delta=100)


    def test_error_dias_mayores_a_30(self):
        with self.assertRaises(ErrorDiasLaborados):
            LiquidadorNomina(1500000, 31, 0, 0)

    def test_error_horas_negativas(self):
        with self.assertRaises(ErrorHorasExtras):
            LiquidadorNomina(1500000, 30, -1, 0)

    def test_error_horas_extras_mayores_a_48(self):
        with self.assertRaises(ErrorHorasExtrasMaximas):
            LiquidadorNomina(1500000, 30, 25, 24)  # total 49

    def test_error_salario_base_cero(self):
        with self.assertRaises(ErrorSalarioBase):
            LiquidadorNomina(0, 30, 0, 0)



if __name__ == "__main__":
    unittest.main()

