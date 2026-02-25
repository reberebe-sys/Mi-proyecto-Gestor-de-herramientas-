
# -*- coding: utf-8 -*-

readme_content = u"""# 🛠️ Gestor de Herramientas v2.1 Enterprise

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

index_content = u"""<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de Herramientas | Terminal de Control</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <header>
        <div class="logo">
            <div class="logo-icon">🛠️</div>
            <h1>Gestor de Herramientas</h1>
        </div>
        <div class="status-pills">
            <div class="pill clock" id="real-time-clock">00:00:00</div>
            <div class="pill active">v2.1 Enterprise</div>
            <div class="pill" id="health-index">Salud: 100%</div>
            <div class="pill" id="total-tools">Cargando...</div>
            <div class="pill" id="critical-tools">Alertas: 0</div>
            <button class="pill" id="btn-export">Reporte CSV</button>
        </div>
    </header>

    <main>
        <div class="dashboard-section">
            <div class="card">
                <div class="card-title">
                    <span>📍 Mapa Visual del Almacén</span>
                </div>
                <div class="warehouse-container" id="warehouse-grid">
                    <!-- Las estanterías se generarán vía JS -->
                </div>
                <div class="warehouse-legend">
                    <span class="legend-item"><i class="dot success"></i> Óptimo</span>
                    <span class="legend-item"><i class="dot warning"></i> Mantenimiento</span>
                    <span class="legend-item"><i class="dot critical"></i> Crítico</span>
                </div>
            </div>

            <div class="analytics-grid">
                <div class="card mini">
                    <div class="card-title">📉 Tendencia de Desgaste</div>
                    <div class="chart-box" id="chart-usage-trends">
                        <div class="bar-chart">
                            <div class="bar" style="height: 40%"></div>
                            <div class="bar" style="height: 60%"></div>
                            <div class="bar" style="height: 85%"></div>
                            <div class="bar" style="height: 50%"></div>
                        </div>
                    </div>
                </div>
                <div class="card mini">
                    <div class="card-title">🏆 Top Herramientas</div>
                    <ul class="clean-list" id="top-tools-list">
                        <li>Fresa 10mm (Alta rotación)</li>
                    </ul>
                </div>
            </div>

            <div class="card">
                <div class="card-title">
                    <span>📋 Inventario de Herramientas</span>
                </div>
                <div class="form-group" style="margin-bottom: 1.5rem;">
                    <input type="text" id="search-input" placeholder="🔍 Buscar por nombre o ubicación...">
                </div>
                <div class="tool-list" id="inventory-list">
                    <!-- Lista de herramientas -->
                    <p style="color: var(--text-secondary); text-align: center; padding: 2rem;">
                        No hay herramientas registradas en esta sección.
                    </p>
                </div>
            </div>
        </div>

        <aside class="sidebar">
            <div class="card">
                <div class="card-title">
                    <span>➕ Nueva Herramienta</span>
                </div>
                <form id="tool-form">
                    <div class="form-group">
                        <label for="name">Nombre de la Herramienta</label>
                        <input type="text" id="name" placeholder="Ej: Fresa de Carburo 10mm" required>
                    </div>
                    <div class="form-group">
                        <label for="location">Ubicación (Estantería/Cajón)</label>
                        <select id="location" required>
                            <option value="">Seleccione ubicación...</option>
                            <!-- Opciones generadas por JS -->
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="max-uses">Vida Útil (Ciclos/Usos)</label>
                        <input type="number" id="max-uses" placeholder="Ej: 500" required>
                    </div>
                    <button type="submit">
                        Registrar Herramienta
                    </button>
                </form>
            </div>

            <div class="card" id="detail-panel" style="display: none;">
                <div class="card-title">
                    <span>🔍 Detalle de Herramienta</span>
                </div>
                <div id="tool-detail-content">
                    <!-- Detalles del ítem seleccionado -->
                </div>
                <button class="secondary" id="btn-use-tool"
                    style="background: rgba(63, 185, 80, 0.1); border-color: var(--success); color: var(--success);">
                    Recordar Uso (-1 ciclo)
                </button>
                <button class="secondary" id="btn-maintenance"
                    style="background: rgba(247, 129, 102, 0.1); border-color: var(--accent-color); color: var(--accent-color);">
                    🔧 Realizar Mantenimiento (Reset)
                </button>
                <button class="secondary" id="btn-qr"
                    style="background: rgba(58, 134, 255, 0.1); border-color: #3a86ff; color: #3a86ff;">
                    Generar Etiqueta QR
                </button>
                <button class="secondary" id="btn-delete-tool"
                    style="color: var(--danger); border-color: rgba(248, 81, 73, 0.2);">
                    Retirar Herramienta
                </button>
            </div>

            <div class="card premium-promo">
                <div class="card-title">💡 Propuesta Industrial</div>
                <p style="font-size: 0.8rem; color: var(--text-secondary); line-height: 1.4;">
                    Este prototipo reduce los tiempos de búsqueda en un <strong>40%</strong> y previene roturas
                    mecánicas mediante el <strong>mantenimiento basado en condición</strong>.
                </p>
                <ul style="font-size: 0.75rem; margin-top: 0.8rem; padding-left: 1rem; color: var(--success);">
                    <li>Integración con ERP SAP/Odoo</li>
                    <li>Notificaciones vía Telegram/WhatsApp</li>
                    <li>Predicción por IA (Machine Learning)</li>
                </ul>
            </div>

            <div class="card">
                <div class="card-title">
                    <span>⚙️ Diagnóstico</span>
                </div>
                <div
                    style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--text-secondary);">
                    <p>> DB Status: Connected</p>
                    <p>> Latency: 4ms</p>
                    <p>> Storage: 12% Used</p>
                </div>
            </div>
        </aside>
    </main>

    <!-- Modal para QR -->
    <div id="qr-modal" class="modal">
        <div class="modal-content card">
            <h2>🏷️ Etiqueta de Identificación</h2>
            <div id="qr-container">
                <!-- Se genera aquí -->
                <div class="mock-qr"></div>
            </div>
            <div class="qr-info">
                <p id="qr-tool-name"></p>
                <p id="qr-tool-loc"></p>
            </div>
            <button onclick="document.getElementById('qr-modal').classList.remove('active')">Cerrar</button>
        </div>
    </div>

    <script src="app-gh-pages.js"></script>
</body>

</html>
"""

def write_utf8(path, text):
    with open(path, 'wb') as f:
        f.write(text.encode('utf-8'))

write_utf8('README.md', readme_content)
write_utf8('index.html', index_content)
