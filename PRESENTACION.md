# Documentación del Proyecto: Gestor de Herramientas v2.1

## 📝 Resumen del Proyecto
Este sistema ha sido diseñado para resolver la desorganización y el mantenimiento reactivo en talleres industriales. Permite un control total sobre la ubicación física y el ciclo de vida de herramientas de corte, moldes y utillajes.

---

## 🏆 Éxitos Alcanzados (Valor Añadido)
1.  **Reducción del Tiempos Muertos:** El mapa interactivo permite a los operarios encontrar cualquier herramienta en segundos, eliminando el "tiempo de búsqueda" no productivo.
2.  **Mantenimiento Preventivo Basado en Condición:** El sistema calcula la "Salud Global" del almacén. Si una herramienta baja del 20% de su vida útil, el sistema lanza una alerta visual crítica.
3.  **Trazabilidad Total:** Cada uso se registra en una base de datos SQLite con una marca de tiempo, permitiendo auditar quién y cuándo usó cada activo.
4.  **Movilidad y Digitalización:** Capacidad de generar etiquetas QR únicas para cada herramienta, facilitando la identificación física con smartphones.

---

## 💡 Propuestas de Mejora (Futuro del Proyecto)
Como dicen en mi pueblo, *"cuanto más azúcar más dulce"*. Aquí están las propuestas para escalar este prototipo a un entorno de fábrica inteligente (Smart Factory):

1.  **Integración con Machine Learning (IA):**
    *   Predecir el fallo de una herramienta basándose en el tipo de material procesado (no solo en el número de usos).
2.  **Conectividad IIoT (Internet de las Cosas):**
    *   Sensores en los cajones que detecten automáticamente si la herramienta está presente o no (Smart Shelving).
3.  **Notificaciones Push:**
    *   Enviar avisos automáticos al departamento de compras vía Telegram o Email cuando el stock de una herramienta crítica esté bajo.
4.  **Realidad Aumentada (AR):**
    *   Uso de una tablet para "ver" a través de las puertas de los armarios dónde está la pieza buscada.

---

## 🛠️ Tecnologías Utilizadas
*   **Backend:** Python (FastAPI) + SQLite (SQLAlchemy).
*   **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript Vanilla.
*   **Gestión:** REST API & Modelos de datos Pydantic.
