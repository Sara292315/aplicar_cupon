import unittest
from app import (
    CalculadoraFactura,
    DescuentoPorcentual,
    DescuentoPorVolumen,
)


class TestFacturacion(unittest.TestCase):

    # 1. Prueba de regresión: Lógica base sin descuentos
    def test_calculo_sin_descuentos(self):
        calc = CalculadoraFactura()
        items = [{'precio': 100.0, 'cantidad': 2}]
        self.assertEqual(calc.calcular(items), 200.0)

    # 2. Equivalente a tus cupones anteriores (DESC10 y DESC20)
    def test_cupon_desc10(self):
        calc = CalculadoraFactura([DescuentoPorcentual(10)])
        items = [{'precio': 100.0, 'cantidad': 1}]
        self.assertEqual(calc.calcular(items), 90.0)

    def test_cupon_desc20(self):
        calc = CalculadoraFactura([DescuentoPorcentual(20)])
        items = [{'precio': 100.0, 'cantidad': 1}]
        self.assertEqual(calc.calcular(items), 80.0)

    # 3. Validación del nuevo requisito: Descuento por Volumen (> 10 unidades)
    def test_descuento_volumen_aplica(self):
        items = [{'precio': 10.0, 'cantidad': 12}]  # 12 unidades (> 10)
        total_unidades = sum(i['cantidad'] for i in items)
        calc = CalculadoraFactura([DescuentoPorVolumen(total_unidades)])
        # Subtotal: $120.0 -> con 5% desc por volumen: $114.0
        self.assertEqual(calc.calcular(items), 114.0)

    def test_descuento_volumen_no_aplica(self):
        items = [{'precio': 10.0, 'cantidad': 8}]  # 8 unidades (<= 10)
        total_unidades = sum(i['cantidad'] for i in items)
        calc = CalculadoraFactura([DescuentoPorVolumen(total_unidades)])
        self.assertEqual(calc.calcular(items), 80.0)


if __name__ == '__main__':
    unittest.main()