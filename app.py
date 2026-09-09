from abc import ABC, abstractmethod
from datetime import datetime, timezone

# ==============================================================================
# PUNTO 4: MANTENIMIENTO ADAPTATIVO (datetime + Adaptador API v2)
# ==============================================================================

# Corrección de fecha para Python 3.12+
timestamp = datetime.now(timezone.utc)


class ClienteAPIv2:

    def get_user(self, id):
        return {'id': id, 'full_name': 'Ana'}


class AdaptadorAPIv2:

    def __init__(self, cliente_v2):
        self.cliente_v2 = cliente_v2

    def obtener_usuario(self, id):
        respuesta_v2 = self.cliente_v2.get_user(id)
        return {'user_id': respuesta_v2['id'], 'name': respuesta_v2['full_name']}


# ==============================================================================
# PUNTO 5: MANTENIMIENTO PERFECTIVO (Patrón Strategy + Descuentos)
# ==============================================================================


class EstrategiaDescuento(ABC):

    @abstractmethod
    def aplicar(self, subtotal: float) -> float:
        ...


class DescuentoPorcentual(EstrategiaDescuento):

    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje

    def aplicar(self, subtotal: float) -> float:
        return subtotal - (subtotal * self.porcentaje / 100)


class DescuentoFijo(EstrategiaDescuento):

    def __init__(self, valor: float):
        self.valor = valor

    def aplicar(self, subtotal: float) -> float:
        return max(0, subtotal - self.valor)


# --- NUEVA ESTRATEGIA (Extensión OCP - Sin modificar CalculadoraFactura) ---
class DescuentoPorVolumen(EstrategiaDescuento):

    def __init__(self, unidades_totales: int):
        self.unidades_totales = unidades_totales

    def aplicar(self, subtotal: float) -> float:
        if self.unidades_totales > 10:
            return subtotal * 0.95  # 5% adicional
        return subtotal


class CalculadoraFactura:

    def __init__(self, estrategias: list[EstrategiaDescuento] = None):
        self.estrategias = estrategias or []

    def calcular(self, items):
        subtotal = sum(i['precio'] * i['cantidad'] for i in items)
        for estrategia in self.estrategias:
            subtotal = estrategia.aplicar(subtotal)
        return round(subtotal, 2)


# ==============================================================================
# EJECUCIÓN Y PRUEBAS EN CONSOLA (Docker output)
# ==============================================================================
if __name__ == '__main__':
    print('--- DEMOSTRACIÓN PUNTO 4 ---')
    print(f'Timestamp UTC: {timestamp}')
    adaptador = AdaptadorAPIv2(ClienteAPIv2())
    print(f'Usuario adaptado: {adaptador.obtener_usuario(1)}\n')

    print('--- DEMOSTRACIÓN PUNTO 5 ---')
    items = [{'precio': 10.0, 'cantidad': 12}]  # 12 unidades (>10)
    total_unidades = sum(i['cantidad'] for i in items)

    calc = CalculadoraFactura([DescuentoPorVolumen(total_unidades)])
    total = calc.calcular(items)
    print(
        f'Subtotal original: $120.0 | Total con Descuento por Volumen: ${total}'
    )