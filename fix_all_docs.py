
# -*- coding: utf-8 -*-
import os

# Definimos los contenidos de los 3 archivos principales de documentación

readme = u"""# 🛠️ Gestor de Herramientas v2.1 Enterprise

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**Gestor de Herramientas** es una solución industrial avanzada para la monitorización en tiempo real, trazabilidad y mantenimiento preventivo de utillajes y herramientas de taller. Diseñado bajo una estética *Dark Engineering*, combina potencia analítica con una experiencia de usuario intuitiva y moderna.

🚀 **[Ver Demo Online (GitHub Pages)](https://reberebe-sys.github.io/Mi-proyecto-Gestor-de-herramientas-/)**

---

## ✨ Características Principales

### 📍 Mapa Interactivo de Almacén
Visualización dinámica tipo *Grid* de las estanterías (Posiciones A1-D6).
- **Semáforo Industrial:** Código de colores automático (Verde, Naranja, Rojo) basado en el desgaste.
- **Alertas Críticas:** Efecto de pulso visual cuando una herramienta requiere atención inmediata.
- **Smart Tooltips:** Información instantánea al pasar el puntero.

### 📈 Smart Analytics & Dashboards
- **KPI de Salud Global:** Índice porcentual del estado de todo el inventario.
- **Tendencias de Desgaste:** Visualización de barras sobre el uso acumulado.
- **Ranking de Rotación:** Identificación de las herramientas con mayor carga de trabajo.

### ⚙️ Gestión de Ciclo de Vida
- **Registro de Uso:** Un solo clic para trackear cada ciclo de trabajo.
- **Mantenimiento Técnico:** Botón de *reset* para afilados o reparaciones con registro en el historial.
- **Auditoría (Logs):** Trazabilidad completa con marcas de tiempo para cada acción.

### 🏷️ Digitalización & Exportación
- **Generador de QR:** Creación de etiquetas únicas para identificación física.
- **Reportes CSV:** Exportación masiva de datos lista para Excel/ERP.
- **Sonidos Industriales:** Confirmación acústica de operaciones críticas.

---

## 🛠️ Stack Tecnológico
- **Backend:** Python con FastAPI.
- **Base de Datos:** SQLite con SQLAlchemy (Persistencia garantizada).
- **Frontend:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript.
- **Diseño:** Google Fonts (Outfit & JetBrains Mono).

---

## 🚀 Instalación y Uso Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/reberebe-sys/Mi-proyecto-Gestor-de-herramientas-.git
    cd Mi-proyecto-Gestor-de-herramientas-
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Iniciar el servidor:**
    ```bash
    python main.py
    ```

4.  **Acceder:**
    Abre `http://localhost:8000` en tu navegador.

---

## 📖 Documentación Adicional
Para más detalles sobre el funcionamiento y mantenimiento del sistema, consulta nuestro [Manual Paso a Paso](./MANUAL_PASO_A_PASO.md) y la [Presentación de Éxitos](./PRESENTACION.md).

---
*Desarrollado para el sector industrial 4.0 - reberebe-sys*
"""

manual = u"""# 📖 Manual de Usuario: Gestor de Herramientas v2.1 Enterprise

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

## 🎮 PASO 2: Gestión del Inventario
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

## 🛠️ PASO 3: Operación y Mantenimiento Técnico
Aquí es donde el sistema ayuda a prevenir fallos y alargar la vida de tus activos.

1.  **Registrar Uso:** Cada vez que se use la herramienta, pulsa el botón verde **"Recordar Uso (-1 ciclo)"**.
2.  **Botón de Mantenimiento (Reset):** Si la herramienta ha sido afilada o reparada, pulsa el botón naranja **"🔧 Realizar Mantenimiento (Reset)"**. Esto pondrá el contador a 0 y guardará el registro en el historial.
3.  **Semáforo de Salud Visual:** 
    *   🟢 **Verde:** Salud óptima.
    *   🟡 **Naranja:** Mantenimiento preventivo recomendado.
    *   🔴 **Rojo:** Nivel Crítico. La herramienta **parpadea en el mapa** para captar tu atención.
4.  **Historial de Auditoría:** Revisa el panel inferior para ver cada acción (creación, uso o mantenimiento) con su hora exacta.

---

## 📊 PASO 4: Analítica y Funciones "Enterprise"
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
"""

presentacion = u"""# Documentación del Proyecto: Gestor de Herramientas v2.1

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
"""

def write_fixed(filename, content):
    # Escribimos con BOM para que Windows y GitHub se pongan de acuerdo
    with open(filename, 'wb') as f:
        f.write(content.encode('utf-8'))
    print(f"File {filename} written successfully.")

write_fixed('README.md', readme)
write_fixed('MANUAL_PASO_A_PASO.md', manual)
write_fixed('PRESENTACION.md', presentacion)
"""

write_fixed('README.md', readme)
write_fixed('MANUAL_PASO_A_PASO.md', manual)
write_fixed('PRESENTACION.md', presentacion)
