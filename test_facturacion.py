import unittest
from facturacion import aplicar_cupon


class TestAplicarCupon(unittest.TestCase):

    def test_cupon_inexistente(self):
        with self.assertRaises(ValueError):
            aplicar_cupon(100, "DESC30")

    def test_cupon_desc10(self):
        resultado = aplicar_cupon(100, "DESC10")
        self.assertEqual(resultado, 90)

    def test_cupon_desc20(self):
        resultado = aplicar_cupon(100, "DESC20")
        self.assertEqual(resultado, 80)


if __name__ == "__main__":
    unittest.main()