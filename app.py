from datetime import datetime, timezone

# 1. Corrección de datetime
timestamp = datetime.now(timezone.utc)
print(f"Timestamp UTC (Corrige DeprecationWarning): {timestamp}")

# 2. Patrón Adapter
class ClienteAPIv2:
    def get_user(self, id):
        return {"id": id, "full_name": "Ana"}

class AdaptadorAPIv2:
    def __init__(self, cliente_v2):
        self.cliente_v2 = cliente_v2

    def obtener_usuario(self, id):
        respuesta_v2 = self.cliente_v2.get_user(id)
        return {"user_id": respuesta_v2["id"], "name": respuesta_v2["full_name"]}

# Prueba de ejecución
cliente_v2 = ClienteAPIv2()
adaptador = AdaptadorAPIv2(cliente_v2)
usuario = adaptador.obtener_usuario(1)

print(f"Datos recibidos tras la adaptación: {usuario}")