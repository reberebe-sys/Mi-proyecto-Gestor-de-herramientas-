# Gestor de Herramientas v2.1 Enterprise

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

Gestor de Herramientas es una solucion industrial avanzada para la monitorizacion en tiempo real, trazabilidad y mantenimiento preventivo de utillajes y herramientas de taller. Disenado bajo una estetica Dark Engineering, combina potencia analitica con una experiencia de usuario intuitiva y moderna.

**[Ver Demo Online (GitHub Pages)](https://reberebe-sys.github.io/Mi-proyecto-Gestor-de-herramientas-/)**

---

## Caracteristicas Principales

### Mapa Interactivo de Almacen
Visualizacion dinamica tipo Grid de las estanterias (Posiciones A1-D6).
- **Semaforo Industrial:** Codigo de colores automatico (Verde, Naranja, Rojo) basado en el desgaste.
- **Alertas Criticas:** Efecto de pulso visual cuando una herramienta requiere atencion inmediata.
- **Smart Tooltips:** Informacion instantanea al pasar el puntero.

### Smart Analytics & Dashboards
- **KPI de Salud Global:** Indice porcentual del estado de todo el inventario.
- **Tendencias de Desgaste:** Visualizacion de barras sobre el uso acumulado.
- **Ranking de Rotacion:** Identificacion de las herramientas con mayor carga de trabajo.

### Gestion de Ciclo de Vida
- **Registro de Uso:** Un solo clic para trackear cada ciclo de trabajo.
- **Mantenimiento Tecnico:** Boton de reset para afilados o reparaciones con registro en el historial.
- **Auditoria (Logs):** Trazabilidad completa con marcas de tiempo para cada accion.

### Digitalizacion & Exportacion
- **Generador de QR:** Creacion de etiquetas unicas para identificacion fisica.
- **Reportes CSV:** Exportacion masiva de datos lista para Excel/ERP.
- **Sonidos Industriales:** Confirmacion acustica de operaciones criticas.

---

## Stack Tecnologico
- **Backend:** Python con FastAPI.
- **Base de Datos:** SQLite con SQLAlchemy (Persistencia garantizada).
- **Frontend:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript.
- **Diseno:** Google Fonts (Outfit & JetBrains Mono).

---

## Instalacion y Uso Local

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

## Documentacion Adicional
Para mas detalles sobre el funcionamiento y mantenimiento del sistema, consulta nuestro [Manual Paso a Paso](./MANUAL_PASO_A_PASO.md) y la [Presentacion de Exitos](./PRESENTACION.md).

---
*Desarrollado para el sector industrial 4.0 - reberebe-sys*
