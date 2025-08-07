import unittest


def calcular_nomina(salario, dias, extras):
    if salario <= 0 or dias < 0 or dias > 30 or extras < 0:
        return None
    return round((salario / 30 * dias) + (salario / 240 * extras * 1.25), 2)


class TestLiquidadorNomina(unittest.TestCase):
   
    def test_normal_1(self):
        self.assertEqual(calcular_nomina(1500000, 30, 5), 1539062.5)

    def test_normal_2(self):
        self.assertEqual(calcular_nomina(1200000, 20, 0), 800000.0)

    def test_normal_3(self):
        self.assertEqual(calcular_nomina(1000000, 15, 10), 552083.33)

   

if __name__ == "__main__":
    unittest.main()

