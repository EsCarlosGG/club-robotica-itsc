# 📤 Cómo subir tu proyecto

Guía para que cualquier integrante (aunque nunca haya usado Git) pueda subir su proyecto.

---

## 1. Prepara tu compu (solo la primera vez)

1. Crea tu cuenta en [github.com](https://github.com) y pásale tu usuario al encargado del repo para que te agregue como **colaborador** (te llega una invitación por correo que tienes que aceptar).
2. Instala [Git](https://git-scm.com/downloads) y [Git LFS](https://git-lfs.com).
3. Activa LFS:
   ```bash
   git lfs install
   ```
4. Clona el repo:
   ```bash
   git clone https://github.com/EsCarlosGG/club-robotica-itsc.git
   cd club-robotica-itsc
   ```

> 💡 **¿No te late la terminal?** Usa [GitHub Desktop](https://desktop.github.com). Hace todo esto con botones y ya trae soporte para LFS.

---

## 2. Crea tu proyecto

Desde la raíz del repo:

```bash
python herramientas/nuevo_proyecto.py "Robot sumo 4 llantas"
```

Eso crea `proyectos/2026-robot-sumo-4-llantas/` con todas las carpetas y plantillas. (Si no tienes Python, copia a mano la carpeta `proyectos/_plantilla/` y renómbrala.)

### Convención de nombres

- Carpeta: `AAAA-nombre-corto` → `2026-robot-sumo`, `2025-seguidor-de-linea`
- Todo en **minúsculas**, con **guiones**, **sin acentos ni espacios ni ñ**
- Archivos igual: `chasis-v2.step`, no `Chasis Versión FINAL (2).STEP`

---

## 3. ¿Qué subo y en qué formato?

| Tipo | Sube SIEMPRE | Además, si tienes |
|---|---|---|
| Piezas 3D | `.STEP` (universal) | Nativo (`.SLDPRT`, `.SLDASM`, `.f3d`) — indica versión de SolidWorks |
| Para imprimir | `.STL` o `.3MF` | Perfil del slicer (`.3mf` con config) |
| Planos | `.PDF` | `.SLDDRW` |
| Esquemáticos | `.PDF` exportado | Proyecto KiCad / EasyEDA / Fritzing |
| Diagramas | `.PNG`/`.SVG` o Mermaid en el README | Fuente editable (draw.io `.drawio`) |
| Código | Todo el proyecto (PlatformIO, Arduino, etc.) | — |
| Fotos | `.JPG` comprimido (< 1 MB c/u) | — |
| Videos | **Solo el link** (YouTube / Drive) | — |

### Límites de GitHub

- Archivo de más de **100 MB → GitHub lo rechaza.** Partirlo o subirlo a Drive y dejar el link.
- Los CAD y STL se van por **Git LFS** automáticamente (ya está configurado en `.gitattributes`), pero LFS también tiene cuota. No subas 20 versiones del mismo ensamble: sube la versión buena y anota los cambios en la bitácora.

---

## 4. Llena la documentación

Mínimo indispensable antes de que se acepte tu proyecto:

- [ ] `README.md` del proyecto con objetivo, integrantes, specs y **lecciones aprendidas**
- [ ] `bom.csv` con los componentes principales
- [ ] Al menos un diagrama (bloques o conexiones)
- [ ] Al menos una foto del robot
- [ ] Instrucciones para compilar/flashear el firmware

---

## 5. Súbelo

```bash
git checkout -b proyecto/2026-robot-sumo
git add proyectos/2026-robot-sumo
git commit -m "Agrega proyecto robot sumo 4 llantas"
git push -u origin proyecto/2026-robot-sumo
```

Luego en GitHub abre un **Pull Request** hacia `main`. Alguien del club lo revisa y lo acepta. Por último agrega tu proyecto a la tabla del `README.md` principal.

### Mensajes de commit

Cortos y que digan qué hiciste:

- ✅ `Agrega esquemático del driver de motores`
- ✅ `Corrige pinout del sensor VL53L7CX en firmware`
- ❌ `cambios`, `ya quedó`, `asdf`

---

## ❓ Dudas

Abre un *Issue* en GitHub o pregúntale a quien esté a cargo del repo este semestre.



---

## 🔑 Administración del repo

- El repo vive en la cuenta personal de quien lo administra. Los colaboradores se agregan en *Settings → Collaborators*.
- **Antes de que el encargado se gradúe**, tiene que transferir el repo a la cuenta de quien siga (*Settings → General → Transfer ownership*). GitHub redirige los links viejos, así que no se rompe nada.
