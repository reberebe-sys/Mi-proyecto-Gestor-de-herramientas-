# 🌐 Guía de Despliegue en GitHub (Manual de reberebe-sys)

Sigue estos pasos para subir tu proyecto y activar la demo web en **GitHub Pages**.

## Pasos Iniciales en tu PC
1. Abre la terminal en la carpeta del proyecto.
2. Inicializa git si no lo has hecho: `git init`
3. Añade tu repositorio remoto:
   ```bash
   git remote add origin https://github.com/reberebe-sys/Mi-proyecto--Gestor-de-herramientas-.git
   ```

## Opción A: Subir el código principal (Main)
Para que otros vean tu código Python (FastAPI):
1. `git add .`
2. `git commit -m "Versión 2.1 Enterprise con SQLite e Historial"`
3. `git push -u origin main`

## Opción B: Activar la Demo Online (GitHub Pages)
GitHub Pages solo sirve archivos estáticos (HTML/CSS/JS). He creado una versión especial llamada `app-gh-pages.js` que usa el almacenamiento del navegador (**LocalStorage**) para que la demo funcione sin servidor Python.

1. **Crea la rama de la web:** 
   ```bash
   git checkout -b gh-pages
   ```
2. **Prepara los archivos para la web:**
   * Abre `index.html` y cambia `<script src="app.js"></script>` por `<script src="app-gh-pages.js"></script>`.
3. **Sube la web:**
   ```bash
   git add .
   git commit -m "Despliegue de demo interactiva en GitHub Pages"
   git push origin gh-pages
   ```
4. **Activa en GitHub:**
   * Ve a tu repositorio en GitHub.com -> **Settings** -> **Pages**.
   * En "Branch", elige `gh-pages` y pulsa **Save**.
   * En unos minutos, tu web estará en: `https://reberebe-sys.github.io/Mi-proyecto--Gestor-de-herramientas-/`

---
*Nota: La versión de GitHub Pages es una demo. Los datos que introduzcas allí se guardan en tu navegador, mientras que la versión local (main) usa la base de datos SQLite profesional.*
