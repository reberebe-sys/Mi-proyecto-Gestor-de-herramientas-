// Versión compatible con GitHub Pages (Simulación de API para estáticos)
const locations = [];
const gridColumns = 6;
const gridRows = 4;

for (let r = 0; r < gridRows; r++) {
    const letter = String.fromCharCode(65 + r);
    for (let c = 1; c <= gridColumns; c++) {
        locations.push(`${letter}${c}`);
    }
}

// Datos iniciales para la web estática
let tools = JSON.parse(localStorage.getItem('gh_tools')) || [
    { id: 1, name: "Fresa de 10mm", location: "A1", current_uses: 120, max_uses: 200 },
    { id: 2, name: "Broca HSS 5mm", location: "B3", current_uses: 450, max_uses: 500 }
];

let selectedToolId = null;

document.addEventListener('DOMContentLoaded', () => {
    initUI();
    fetchTools();
    startClock();
});

function startClock() {
    const clockElement = document.getElementById('real-time-clock');
    if (clockElement) {
        setInterval(() => {
            const now = new Date();
            clockElement.textContent = now.toLocaleTimeString();
        }, 1000);
    }
}

// Simulador de sonidos para web
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playSound(type) {
    const oscillator = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();
    oscillator.connect(gainNode);
    gainNode.connect(audioCtx.destination);
    oscillator.type = 'sine';
    if (type === 'select') oscillator.frequency.setValueAtTime(440, audioCtx.currentTime);
    else oscillator.frequency.setValueAtTime(880, audioCtx.currentTime);
    gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
    oscillator.start();
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    oscillator.stop(audioCtx.currentTime + 0.1);
}

function fetchTools() {
    renderInventory();
    renderMap();
    updateAnalytics();
    if (selectedToolId) showDetail(selectedToolId);
}

function initUI() {
    const locationSelect = document.getElementById('location');
    if (locationSelect) {
        locations.forEach(loc => {
            const option = document.createElement('option');
            option.value = loc;
            option.textContent = `Posición ${loc}`;
            locationSelect.appendChild(option);
        });
    }

    const form = document.getElementById('tool-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const newTool = {
                id: Date.now(),
                name: document.getElementById('name').value,
                location: document.getElementById('location').value,
                current_uses: 0,
                max_uses: parseInt(document.getElementById('max-uses').value)
            };
            tools.push(newTool);
            saveData();
            fetchTools();
            e.target.reset();
            showNotification('Herramienta registrada');
        });
    }

    document.getElementById('search-input')?.addEventListener('input', (e) => {
        renderInventory(e.target.value);
    });

    document.getElementById('btn-export')?.addEventListener('click', () => {
        const csvContent = "data:text/csv;charset=utf-8,ID,Nombre,Ubicacion,Uso,VidaUtil\n"
            + tools.map(t => `${t.id},${t.name},${t.location},${t.current_uses},${t.max_uses}`).join("\n");
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "inventario_tools.csv");
        link.click();
    });
}

function saveData() {
    localStorage.setItem('gh_tools', JSON.stringify(tools));
}

function renderMap() {
    const grid = document.getElementById('warehouse-grid');
    if (!grid) return;
    grid.innerHTML = '';

    locations.forEach(loc => {
        const shelve = document.createElement('div');
        const toolInLoc = tools.find(t => t.location === loc);
        shelve.className = `shelve ${selectedToolId && toolInLoc?.id === selectedToolId ? 'selected' : ''}`;
        shelve.innerHTML = `<span class="shelve-id">${loc}</span>`;

        if (toolInLoc) {
            const lifePercent = (1 - toolInLoc.current_uses / toolInLoc.max_uses) * 100;
            let status = lifePercent < 20 ? 'critical' : (lifePercent < 50 ? 'warning' : 'occupied');
            shelve.innerHTML += `<div class="occupancy-dot ${status}"></div><span class="tool-icon">🛠️</span>`;
            shelve.title = `${toolInLoc.name} (${lifePercent.toFixed(0)}%)`;
            shelve.onclick = () => { playSound('select'); showDetail(toolInLoc.id); };
        }
        grid.appendChild(shelve);
    });
}

function renderInventory(filter = '') {
    const list = document.getElementById('inventory-list');
    if (!list) return;
    list.innerHTML = '';

    document.getElementById('total-tools').textContent = `Total: ${tools.length}`;
    const criticalCount = tools.filter(t => (1 - t.current_uses / t.max_uses) < 0.2).length;
    document.getElementById('critical-tools').textContent = `Alertas: ${criticalCount}`;

    const filtered = tools.filter(t => t.name.toLowerCase().includes(filter.toLowerCase()) || t.location.toLowerCase().includes(filter.toLowerCase()));

    filtered.forEach(tool => {
        const lifePercent = Math.max(0, (1 - tool.current_uses / tool.max_uses) * 100);
        const item = document.createElement('div');
        item.className = `tool-item ${selectedToolId === tool.id ? 'active' : ''}`;
        item.innerHTML = `<div class="tool-info"><h4>${tool.name}</h4><p>${tool.location} | ${tool.current_uses}/${tool.max_uses}</p></div><div class="life-bar-container"><div class="life-bar" style="width:${lifePercent}%;background:${getLifeColor(lifePercent)}"></div></div>`;
        item.onclick = () => showDetail(tool.id);
        list.appendChild(item);
    });
}

function showDetail(id) {
    selectedToolId = id;
    const tool = tools.find(t => t.id === id);
    const content = document.getElementById('tool-detail-content');
    const panel = document.getElementById('detail-panel');
    if (!tool || !content) return;
    panel.style.display = 'block';
    renderMap();
    const lifePercent = (1 - tool.current_uses / tool.max_uses) * 100;
    content.innerHTML = `<h2 style="color:var(--accent-color)">${tool.name}</h2><p>ID: #${tool.id}</p><div style="background:rgba(0,0,0,0.2);padding:10px;border-radius:8px;margin:10px 0"><p>📍 ${tool.location}</p><p>🔋 ${lifePercent.toFixed(1)}% salud</p></div>`;

    document.getElementById('btn-use-tool').onclick = () => { tool.current_uses++; saveData(); playSound('success'); fetchTools(); };
    document.getElementById('btn-maintenance').onclick = () => { tool.current_uses = 0; saveData(); playSound('success'); fetchTools(); };
    document.getElementById('btn-delete-tool').onclick = () => { tools = tools.filter(t => t.id !== id); selectedToolId = null; saveData(); panel.style.display = 'none'; fetchTools(); };
    document.getElementById('btn-qr').onclick = () => { document.getElementById('qr-modal').classList.add('active'); document.getElementById('qr-tool-name').textContent = tool.name; };
}

function updateAnalytics() {
    if (tools.length === 0) return;
    const avgLife = tools.reduce((acc, t) => acc + (1 - t.current_uses / t.max_uses), 0) / tools.length;
    document.getElementById('health-index').textContent = `Salud: ${(avgLife * 100).toFixed(0)}%`;
}

function getLifeColor(p) { return p < 20 ? 'var(--danger)' : (p < 50 ? 'var(--warning)' : 'var(--success)'); }

function showNotification(msg) {
    const toast = document.createElement('div');
    toast.style.cssText = "position:fixed;bottom:20px;right:20px;background:var(--accent-color);color:white;padding:10px 20px;border-radius:8px;z-index:1000;";
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}
