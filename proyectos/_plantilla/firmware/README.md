# Firmware

## Requisitos

- IDE / entorno: PlatformIO / Arduino IDE x.x / Makefile
- Placa y core: ej. `esp32` v3.x, Teensyduino 1.59
- Librerías (con versión):
  - 

## Compilar y cargar

```bash
# ej. PlatformIO
pio run -t upload
```

## Estructura del código

Qué hace cada archivo/módulo, en una línea.

## Parámetros a calibrar

| Constante | Archivo | Valor actual | Qué controla |
|---|---|---|---|
| `KP` | `control.h` | 1.2 | Ganancia proporcional del PID |
