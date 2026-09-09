# facturacion.py
def calcular_total(items, descuento=None):
    """
    items: lista de dicts {'nombre': str, 'precio': float, 'cantidad': int}
    descuento: porcentaje (0-100) o None
    """
    subtotal = sum(item['precio'] * item['cantidad'] for item in items)
    if descuento:
        subtotal = subtotal - (subtotal * descuento / 100)
    return round(subtotal, 2)
 
def aplicar_cupon(total, cupon):
    cupones = {"DESC10": 10, "DESC20": 20}
    descuento = cupones[cupon]  # <-- Falla: KeyError si el cupón no existe
    return calcular_total([{'nombre': 'total', 'precio': total, 'cantidad': 1}], descuento)
