# 📖 Manual de Usuario: Gestor de Herramientas v2.1 Enterprise

¡Bienvenido al manual oficial de tu nuevo sistema de gestión industrial! Este documento explica paso a paso cómo instalar, configurar y utilizar el prototipo para que cualquier persona, sin conocimientos técnicos, pueda manejarlo.

---

## 🚀 PASO 1: Instalación y Puesta en Marcha
Para que el sistema funcione, necesitamos preparar el "motor" (backend).

1.  **Abrir la Terminal:** Ve a la carpeta del proyecto `El meu projecte`.
2.  **Instalar librerías:** Escribe este comando y pulsa Enter:
    ```powershell
    pip install -r requirements.txt
    ```
3.  **Encender el sistema:** Escribe este comando para arrancar el servidor:
    ```powershell
    python main.py
    ```
4.  **Acceder a la interfaz:** Abre tu navegador (Chrome, Edge...) y escribe esta dirección:
    `http://localhost:8000`

---

## 🛠️ PASO 2: Gestión del Inventario
Una vez dentro, verás la terminal de control con un **reloj en tiempo real** en la cabecera.

### 2.1 Registrar una herramienta nueva
En el panel de la derecha (**➕ Nueva Herramienta**):
1.  Escribe el **Nombre** (ej. "Broca de Titanio 5mm").
2.  Elige una **Ubicación** en el mapa (ej. Posición B3).
3.  Indica la **Vida Útil** (cuántas veces se puede usar antes de que se rompa o gaste).
4.  Pulsa el botón naranja **"Registrar Herramienta"**. Escucharás un sonido positivo y aparecerá en el mapa.

### 2.2 Localizar y Consultar Detalles
*   **En el Mapa:** Pasa el ratón sobre un cajón ocupado para ver un **Tooltip** (etiqueta rápida) con el nombre y la salud. Haz clic para seleccionarla.
*   **En la Lista:** Usa la barra de búsqueda (**🔍**) para filtrar por nombre o ubicación en tiempo real.
*   **Sonidos de Selección:** Cada vez que selecciones una herramienta, escucharás un "beep" de confirmación técnica.

---

## 📈 PASO 3: Operación y Mantenimiento Técnico
Aquí es donde el sistema ayuda a prevenir fallos y alargar la vida de tus activos.

1.  **Registrar Uso:** Cada vez que se use la herramienta, pulsa el botón verde **"Recordar Uso (-1 ciclo)"**.
2.  **Botón de Mantenimiento (Reset):** Si la herramienta ha sido afilada o reparada, pulsa el botón naranja **"🔧 Realizar Mantenimiento (Reset)"**. Esto pondrá el contador a 0 y guardará el registro en el historial.
3.  **Semáforo de Salud Visual:** 
    *   🟢 **Verde:** Salud óptima.
    *   🟡 **Naranja:** Mantenimiento preventivo recomendado.
    *   🔴 **Rojo:** Nivel Crítico. La herramienta **parpadea en el mapa** para captar tu atención.
4.  **Historial de Auditoría:** Revisa el panel inferior para ver cada acción (creación, uso o mantenimiento) con su hora exacta.

---

## 📈 PASO 4: Analítica y Funciones "Enterprise"
Diseñado para la toma de decisiones por parte de los responsables de planta.

1.  **Dashboard de Analítica:** 
    *   **Salud Global:** Un porcentaje en la cabecera que indica el estado medio de todo el taller.
    *   **Tendencia de Desgaste:** Gráfico visual que muestra el uso acumulado.
    *   **Top Herramientas:** Lista de las 3 piezas con más rotación (más usadas).
2.  **Generar Etiqueta QR:** Haz clic para ver la etiqueta de identificación única. Útil para el etiquetado físico de cajones.
3.  **Reporte CSV (Excel):** Pulsa el botón verde **"Reporte CSV"** en la cabecera para descargar instantáneamente toda la base de datos y trabajar con ella en Excel.

---

## ❓ Preguntas Frecuentes (FAQ)
*   **¿Se borran los datos al apagar el PC?** No. Todo se guarda automáticamente en `herramientas.db`.
*   **¿Cómo sé si una herramienta es crítica?** El punto en el mapa empezará a parpadear en rojo y el indicador superior de "Alertas" subirá de número automáticamente.

---
*Manual actualizado v2.1.2 - Sistema de Gestión Técnica Avanzada*
