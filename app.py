from datetime import datetime, timezone

# --- 1. Migración de fecha (Mantenimiento Adaptativo) ---
# Corrección recomendada para Python 3.12+
timestamp = datetime.now(timezone.utc)
print(f"Timestamp UTC (Corrige DeprecationWarning): {timestamp}")


# --- 2. Implementación de Patrón Adapter (API v1 -> v2) ---
class ClienteAPIv2:
    """Simula la nueva API externa v2 con esquema JSON actualizado."""
    def get_user(self, id):
        return {"id": id, "full_name": "Ana"}

class AdaptadorAPIv2:
    """Aísla el sistema principal adaptando la respuesta de la v2 al formato antiguo."""
    def __init__(self, cliente_v2):
        self.cliente_v2 = cliente_v2

    def obtener_usuario(self, id):
        respuesta_v2 = self.cliente_v2.get_user(id)
        # Traducción de claves: {"id", "full_name"} -> {"user_id", "name"}
        return {"user_id": respuesta_v2["id"], "name": respuesta_v2["full_name"]}


# Prueba del adaptador
cliente_v2 = ClienteAPIv2()
adaptador = AdaptadorAPIv2(cliente_v2)
usuario = adaptador.obtener_usuario(1)

print(f"Datos recibidos tras la adaptación: {usuario}")