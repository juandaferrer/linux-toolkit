# Juan Ferrer's Toolkit

A personal collection of Linux utilities, automation scripts, and infrastructure-related tools built while learning system administration and Python.

The goal of this repository is simple: solve real problems with practical scripts instead of reinventing the wheel every time.

## What you'll find

* 🐧 Linux administration utilities
* 🐍 Python automation scripts
* ⚙️ System diagnostic tools
* 📋 Environment setup helpers
* 🚀 Future infrastructure and DevOps experiments

## Current Projects

### ⚙️ SysDiag (Linux Diagnostic Helper)
Un script robusto en Python para la recolección automatizada y selectiva de logs críticos del sistema. Diseñado para administración de servidores y ejecución no bloqueante mediante tareas programadas (`cron`).

* **Filtrado Inteligente:** Captura únicamente eventos críticos (`-p 4` en `journalctl`, `--level=err,warn` en `dmesg` y `--failed` en `systemctl`).
* **Modo Consolidado:** Si se ejecuta sin argumentos, genera un reporte completo de 50 líneas por módulo separados limpiamente.

#### Uso rápido:
```bash
# Reporte completo automatizado (50 líneas de cada uno)
sudo python3 sysdiag.py

# Diagnóstico selectivo con líneas personalizadas
sudo python3 sysdiag.py dmesg 100
sudo python3 sysdiag.py journalctl 20
```
## Why this repository?

I created this repository to document my learning journey while building tools that I can actually use in real environments.

Rather than writing small practice programs, I prefer creating utilities that automate repetitive tasks or simplify Linux administration.

## Technologies

* Python
* Linux
* Bash (coming soon)

## Disclaimer

These scripts are provided as-is.

Always review any script before executing it on a production system. Some utilities may require elevated privileges depending on the task being performed.

## Contributions

Suggestions, improvements and constructive feedback are always welcome.
