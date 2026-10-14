<p align="center">
  <img src="recursos/identidad/logo.png" alt="Logo Club Robótica ITSC" width="260">
</p>

<h1 align="center">Club Robótica ITSC</h1>
<p align="center"><i>TecNM Campus Cananea</i></p>

Bitácora y archivo de **todos** los proyectos del **Club Robótica ITSC** (TecNM Campus Cananea): modelos 3D, diagramas, código, fotos, resultados de competencias y, sobre todo, **lo que aprendimos**.

La idea es simple: que ninguna generación empiece desde cero. Si vas a hacer un robot nuevo, primero date una vuelta por aquí y revisa qué se hizo, qué funcionó y qué no.

---

## ¿Qué hay en este repo?

```
├── proyectos/          ← Un folder por proyecto (robots, prototipos, pruebas)
│   └── _plantilla/     ← Copia esto para empezar un proyecto nuevo
├── competencias/       ← Registro de cada evento: fecha, robot, resultado
├── recursos/
│   ├── guias/          ← Tutoriales hechos por el club (flashear, soldar, CAD…)
│   ├── componentes/    ← Fichas de componentes que ya probamos
│   └── reglamentos/    ← Reglamentos de competencias
└── CONTRIBUTING.md     ← Cómo subir tu proyecto (léelo antes de subir algo)
```

Cada proyecto tiene la misma estructura, así encuentras todo rápido:

```
proyectos/2026-robot-sumo/
├── README.md               ← Ficha del proyecto (empieza aquí)
├── bitacora.md             ← Diario de avances, problemas y decisiones
├── bom.csv                 ← Lista de materiales con costos y proveedores
├── cad/                    ← Modelos 3D, planos, STL para imprimir
├── electronica/            ← Esquemáticos, PCB, diagramas de conexión
├── firmware/               ← Código del robot
├── docs/                   ← Reportes, presentaciones, datasheets
└── media/                  ← Fotos y links a videos
```

---

## Índice de proyectos

| Proyecto | Año | Tipo | Estado | Competencia | Integrantes |
|---|---|---|---|---|---|
| [Ejemplo: Robot sumo 4 llantas](proyectos/) | 2026 | Sumo | En desarrollo | — | — |

> Estados: Terminado · En desarrollo · Abandonado (¡también se documenta, se aprende mucho de lo que falla!)

## Competencias

Ver [competencias/README.md](competencias/README.md).

---

## Reglas de oro

1. **Documenta mientras haces, no al final.** Al final ya se te olvidó por qué cambiaste el motor.
2. **Sube siempre los formatos "universales"** además del nativo: STEP + STL + PDF de planos, no solo el `.SLDPRT`. Las versiones de SolidWorks no son compatibles hacia atrás y el que venga después quizá no tenga tu versión.
3. **Escribe las lecciones aprendidas.** Es la sección más valiosa de cada proyecto.
4. **Nada de contraseñas, tokens ni datos personales** en el repo.
5. **Videos → YouTube/Drive y aquí solo el link.** GitHub no es para videos pesados.

## Antes de clonar

Este repo usa **Git LFS** para archivos grandes (CAD, STL, etc.). Instálalo antes de clonar:

```bash
git lfs install
git clone https://github.com/EsCarlosGG/club-robotica-itsc.git
```

Si clonas sin LFS, los modelos 3D te van a salir como archivos de texto chiquitos. Detalles en [CONTRIBUTING.md](CONTRIBUTING.md).
