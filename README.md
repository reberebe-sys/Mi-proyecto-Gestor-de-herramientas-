# 🛠️ Gestor de Herramientas v2.1 Enterprise

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**Gestor de Herramientas** es una solución industrial avanzada para la monitorización en tiempo real, trazabilidad y mantenimiento preventivo de utillajes y herramientas de taller. Diseñado bajo una estética *Dark Engineering*, combina potencia analítica con una experiencia de usuario intuitiva y moderna.

🚀 **[Ver Demo Online (GitHub Pages)](https://reberebe-sys.github.io/Mi-proyecto--Gestor-de-herramientas-/)**

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
    git clone https://github.com/reberebe-sys/Mi-proyecto--Gestor-de-herramientas-.git
    cd Mi-proyecto--Gestor-de-herramientas-
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
