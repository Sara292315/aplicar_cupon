import pytest
from app import (
    CalculadoraFactura,
    DescuentoPorcentual,
    DescuentoPorVolumen,
)


# 1. Regresión: Lógica base sin descuentos
def test_calculo_sin_descuentos():
    calc = CalculadoraFactura()
    items = [{'precio': 100.0, 'cantidad': 2}]
    assert calc.calcular(items) == 200.0


# 2. Regresión: Cupones porcentuales (10% y 20%)
def test_cupon_desc10():
    calc = CalculadoraFactura([DescuentoPorcentual(10)])
    items = [{'precio': 100.0, 'cantidad': 1}]
    assert calc.calcular(items) == 90.0


def test_cupon_desc20():
    calc = CalculadoraFactura([DescuentoPorcentual(20)])
    items = [{'precio': 100.0, 'cantidad': 1}]
    assert calc.calcular(items) == 80.0


# 3. Mantenimiento Perfectivo: Descuento por Volumen (> 10 unidades)
def test_descuento_volumen_aplica():
    items = [{'precio': 10.0, 'cantidad': 12}]  # 12 unidades (> 10)
    total_unidades = sum(i['cantidad'] for i in items)
    calc = CalculadoraFactura([DescuentoPorVolumen(total_unidades)])
    assert calc.calcular(items) == 114.0


def test_descuento_volumen_no_aplica():
    items = [{'precio': 10.0, 'cantidad': 8}]  # 8 unidades (<= 10)
    total_unidades = sum(i['cantidad'] for i in items)
    calc = CalculadoraFactura([DescuentoPorVolumen(total_unidades)])
    assert calc.calcular(items) == 80.0