def aplicar_cupon(total, cupon):
    cupones = {"DESC10": 10, "DESC20": 20}

    descuento = cupones.get(cupon)

    if descuento is None:
        raise ValueError(f"El cupón '{cupon}' no existe")

    return calcular_total(
        [{'nombre': 'total', 'precio': total, 'cantidad': 1}],
        descuento
    )