#!/usr/bin/env python3
"""Crea un proyecto nuevo a partir de proyectos/_plantilla.

Uso:
    python herramientas/nuevo_proyecto.py "Robot sumo 4 llantas"
    python herramientas/nuevo_proyecto.py "Seguidor de linea" --anio 2025
"""
import argparse
import datetime
import re
import shutil
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLA = RAIZ / "proyectos" / "_plantilla"


def slug(texto: str) -> str:
    """'Robot Sumo Ñandú' -> 'robot-sumo-nandu'"""
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    texto = re.sub(r"[^a-zA-Z0-9]+", "-", texto).strip("-").lower()
    return texto


def main() -> int:
    p = argparse.ArgumentParser(description="Crea un proyecto nuevo del Club Robótica ITSC.")
    p.add_argument("nombre", help='Nombre del proyecto, ej. "Robot sumo 4 llantas"')
    p.add_argument("--anio", type=int, default=datetime.date.today().year)
    args = p.parse_args()

    s = slug(args.nombre)
    if not s:
        print("❌ El nombre no puede quedar vacío.")
        return 1

    destino = RAIZ / "proyectos" / f"{args.anio}-{s}"
    if destino.exists():
        print(f"❌ Ya existe: {destino.relative_to(RAIZ)}")
        return 1

    shutil.copytree(PLANTILLA, destino)

    hoy = datetime.date.today().isoformat()
    for archivo in destino.rglob("*.md"):
        t = archivo.read_text(encoding="utf-8")
        t = t.replace("{{NOMBRE}}", args.nombre).replace("{{FECHA}}", hoy)
        archivo.write_text(t, encoding="utf-8")

    rel = destino.relative_to(RAIZ).as_posix()
    print(f"✅ Proyecto creado en {rel}/")
    print("   Siguientes pasos:")
    print(f"   1. Llena {rel}/README.md")
    print(f"   2. Agrega tu proyecto a la tabla del README.md principal")
    print(f"   3. git checkout -b proyecto/{args.anio}-{s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
