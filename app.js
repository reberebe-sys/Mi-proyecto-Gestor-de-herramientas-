// Configuración de la API
const API_URL = '/api/tools';

let tools = [];
let selectedToolId = null;
const gridColumns = 6;
const gridRows = 4;
const locations = [];

// Generar coordenadas del almacén (A1, A2... B1...)
for (let r = 0; r < gridRows; r++) {
    const letter = String.fromCharCode(65 + r);
    for (let c = 1; c <= gridColumns; c++) {
        locations.push(`${letter}${c}`);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initUI();
    fetchTools();
    startClock();
});

// SONIDOS MEJORA
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playSound(type) {
    const oscillator = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();
    oscillator.connect(gainNode);
    gainNode.connect(audioCtx.destination);

    if (type === 'select') {
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(440, audioCtx.currentTime);
        gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
        oscillator.start();
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
        oscillator.stop(audioCtx.currentTime + 0.1);
    } else if (type === 'success') {
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(880, audioCtx.currentTime);
        gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
        oscillator.start();
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
        oscillator.stop(audioCtx.currentTime + 0.2);
    }
}

function startClock() {
    const clockElement = document.getElementById('real-time-clock');
    setInterval(() => {
        const now = new Date();
        clockElement.textContent = now.toLocaleTimeString();
    }, 1000);
}

async function fetchTools() {
    try {
        const response = await fetch(API_URL);
        tools = await response.json();
        renderInventory();
        renderMap();
        updateAnalytics();
        if (selectedToolId) showDetail(selectedToolId);
    } catch (error) {
        console.error('Error cargando herramientas:', error);
    }
}

function initUI() {
    const locationSelect = document.getElementById('location');
    locations.forEach(loc => {
        const option = document.createElement('option');
        option.value = loc;
        option.textContent = `Posición ${loc}`;
        locationSelect.appendChild(option);
    });

    document.getElementById('tool-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const toolData = {
            name: document.getElementById('name').value,
            location: document.getElementById('location').value,
            max_uses: parseInt(document.getElementById('max-uses').value)
        };

        try {
            const resp = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(toolData)
            });
            if (resp.ok) {
                fetchTools();
                e.target.reset();
                showNotification('Herramienta registrada correctamente');
            }
        } catch (error) {
            alert('Error al guardar la herramienta');
        }
    });

    // Buscador
    document.getElementById('search-input').addEventListener('input', (e) => {
        renderInventory(e.target.value);
    });

    // Exportar CSV
    document.getElementById('btn-export').onclick = () => {
        const csvContent = "data:text/csv;charset=utf-8,ID,Nombre,Ubicacion,Uso,VidaUtil\n"
            + tools.map(t => `${t.id},${t.name},${t.location},${t.current_uses},${t.max_uses}`).join("\n");
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "inventario_herramientas.csv");
        document.body.appendChild(link);
        link.click();
        showNotification('Reporte generado correctamente');
    };

    // Modal QR
    document.getElementById('btn-qr').onclick = () => {
        const tool = tools.find(t => t.id === selectedToolId);
        if (!tool) return;

        document.getElementById('qr-modal').classList.add('active');
        document.getElementById('qr-tool-name').textContent = tool.name;
        document.getElementById('qr-tool-loc').textContent = `Ubicación: ${tool.location}`;
        showNotification('Cargando datos seguros...');
    };
}

function updateAnalytics() {
    // Calcular Salud Global
    if (tools.length === 0) return;

    const avgLife = tools.reduce((acc, t) => acc + (1 - t.current_uses / t.max_uses), 0) / tools.length;
    document.getElementById('health-index').textContent = `Salud Global: ${(avgLife * 100).toFixed(0)}%`;

    // Top Herramientas (más usadas)
    const topTools = [...tools].sort((a, b) => b.current_uses - a.current_uses).slice(0, 3);
    const topList = document.getElementById('top-tools-list');
    topList.innerHTML = topTools.map(t => `<li>${t.name} (${t.current_uses} usos)</li>`).join('') || '<li>Sin datos</li>';

    // Animación de bar chart (aleatoria para simular)
    const bars = document.querySelectorAll('.bar');
    bars.forEach(bar => {
        const h = Math.floor(Math.random() * 80) + 20;
        bar.style.height = `${h}%`;
    });
}

function renderMap() {
    const grid = document.getElementById('warehouse-grid');
    grid.innerHTML = '';

    locations.forEach(loc => {
        const shelve = document.createElement('div');
        const toolInLoc = tools.find(t => t.location === loc);

        shelve.className = `shelve ${selectedToolId && toolInLoc?.id === selectedToolId ? 'selected' : ''}`;
        shelve.innerHTML = `<span class="shelve-id">${loc}</span>`;

        if (toolInLoc) {
            const dot = document.createElement('div');
            const lifePercent = (1 - toolInLoc.current_uses / toolInLoc.max_uses) * 100;

            let status = 'occupied';
            if (lifePercent < 20) status = 'critical';
            else if (lifePercent < 50) status = 'warning';

            dot.className = `occupancy-dot ${status}`;
            shelve.appendChild(dot);
            shelve.innerHTML += `<span class="tool-icon">🛠️</span>`;

            // TOOLTIP MEJORA
            shelve.title = `${toolInLoc.name} (${lifePercent.toFixed(0)}% salud)`;

            shelve.onclick = () => {
                playSound('select');
                showDetail(toolInLoc.id);
            };
        }

        grid.appendChild(shelve);
    });
}

function renderInventory(filter = '') {
    const list = document.getElementById('inventory-list');
    list.innerHTML = '';

    document.getElementById('total-tools').textContent = `Total: ${tools.length}`;
    const criticalCount = tools.filter(t => (1 - t.current_uses / t.max_uses) < 0.2).length;
    document.getElementById('critical-tools').textContent = `Alertas: ${criticalCount}`;
    document.getElementById('critical-tools').style.color = criticalCount > 0 ? 'var(--danger)' : 'var(--text-secondary)';

    const filteredTools = tools.filter(t =>
        t.name.toLowerCase().includes(filter.toLowerCase()) ||
        t.location.toLowerCase().includes(filter.toLowerCase())
    );

    if (filteredTools.length === 0) {
        list.innerHTML = '<p style="color: var(--text-secondary); text-align: center; padding: 2rem;">No se encontraron herramientas.</p>';
        return;
    }

    filteredTools.forEach(tool => {
        const lifePercent = Math.max(0, (1 - tool.current_uses / tool.max_uses) * 100);
        const item = document.createElement('div');
        item.className = `tool-item ${selectedToolId === tool.id ? 'active' : ''}`;
        item.innerHTML = `
            <div class="tool-info">
                <h4>${tool.name}</h4>
                <p>Ubicación: <strong>${tool.location}</strong> | Uso: ${tool.current_uses}/${tool.max_uses}</p>
            </div>
            <div class="life-bar-container">
                <div class="life-bar" style="width: ${lifePercent}%; background: ${getLifeColor(lifePercent)}"></div>
            </div>
        `;
        item.onclick = () => showDetail(tool.id);
        list.appendChild(item);
    });
}

async function showDetail(id) {
    selectedToolId = id;
    const tool = tools.find(t => t.id === id);
    const panel = document.getElementById('detail-panel');
    const content = document.getElementById('tool-detail-content');

    panel.style.display = 'block';
    renderMap(); // Actualizar selección en mapa

    const lifePercent = Math.max(0, (1 - tool.current_uses / tool.max_uses) * 100);

    content.innerHTML = `
        <div style="margin-bottom: 1.5rem;">
            <h2 style="color: var(--accent-color); font-size: 1.4rem;">${tool.name}</h2>
            <p style="font-size: 0.9rem; color: var(--text-secondary);">ID Sistema: #${tool.id}</p>
        </div>
        <div style="background: rgba(0,0,0,0.2); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <p style="margin-bottom: 0.5rem;">📍 Ubicación: <span style="color: white; font-weight: 600;">${tool.location}</span></p>
            <p style="margin-bottom: 0.5rem;">🔄 Ciclos completados: <span style="color: white; font-weight: 600;">${tool.current_uses}</span></p>
            <p>🔋 Vida estimada: <span style="color: ${getLifeColor(lifePercent)}; font-weight: 600;">${lifePercent.toFixed(1)}%</span></p>
        </div>
        <div id="history-container">
            <h4 style="font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 0.5rem;">HISTORIAL RECIENTE</h4>
            <div id="history-list" style="max-height: 100px; overflow-y: auto; font-size: 0.75rem;">
                Cargando historial...
            </div>
        </div>
    `;

    fetchHistory(id);

    document.getElementById('btn-use-tool').onclick = async () => {
        try {
            const resp = await fetch(`${API_URL}/${id}/use`, { method: 'PUT' });
            if (resp.ok) {
                playSound('success');
                fetchTools();
                showNotification('Uso registrado');
            }
        } catch (error) {
            alert("No se pudo registrar el uso");
        }
    };

    // BOTÓN MANTENIMIENTO MEJORA
    const btnMaint = document.getElementById('btn-maintenance');
    btnMaint.onclick = async () => {
        if (confirm('¿Confirmar reafilado/mantenimiento de esta herramienta?')) {
            await fetch(`${API_URL}/${id}/maintenance`, { method: 'PUT' });
            playSound('success');
            fetchTools();
            showNotification('Herramienta puesta a punto');
        }
    };

    document.getElementById('btn-delete-tool').onclick = async () => {
        if (confirm('¿Retirar herramienta del almacén?')) {
            await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
            panel.style.display = 'none';
            selectedToolId = null;
            fetchTools();
        }
    };
}

async function fetchHistory(id) {
    try {
        const resp = await fetch(`${API_URL}/${id}/history`);
        const history = await resp.json();
        const historyList = document.getElementById('history-list');
        if (history.length === 0) {
            historyList.innerHTML = 'Sin registros previos.';
        } else {
            historyList.innerHTML = history.map(log => `
                <div style="padding: 4px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <span style="color: var(--accent-color)">[${log.action}]</span> 
                    ${new Date(log.timestamp).toLocaleString()}
                </div>
            `).join('');
        }
    } catch (e) {
        console.error(e);
    }
}

function getLifeColor(percent) {
    if (percent < 20) return 'var(--danger)';
    if (percent < 50) return 'var(--warning)';
    return 'var(--success)';
}

function showNotification(msg) {
    const toast = document.createElement('div');
    toast.style.cssText = `
        position: fixed; bottom: 20px; right: 20px; 
        background: var(--accent-color); color: white;
        padding: 10px 20px; border-radius: 8px; z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        animation: slideIn 0.3s ease-out;
    `;
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.5s';
        setTimeout(() => toast.remove(), 500);
    }, 2000);
}
