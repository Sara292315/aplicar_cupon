# Laboratorio - Reparación de Fallas Post-Despliegue
## Incidencia FACT-014

### Título
KeyError al aplicar cupón inexistente en `aplicar_cupon()`

### Severidad
Alta

### Impacto en el Negocio
Un cupón inexistente provocaba una excepción no controlada durante el proceso de cálculo de una orden. Esto podía interrumpir el proceso de facturación y afectar a los usuarios que intentaran utilizar un cupón inválido.

### Módulo Afectado
`facturacion.py`

---

### Pasos para Reproducir
1. Importar la función `aplicar_cupon`.
2. Ejecutar:
   ```python
   aplicar_cupon(100, "DESC30")