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
A robust Python script for automated, selective collection of critical system logs. Designed for server administration and non-blocking execution through scheduled tasks (`cron`).

* **Smart Filtering:** Captures only critical events (`-p 4` in `journalctl`, `--level=err,warn` in `dmesg`, and `--failed` in `systemctl`).
* **Consolidated Mode:** When run without arguments, it produces a complete report of 50 lines per module, separated cleanly.

#### Quick use:
```bash
# Automated full report (50 lines of each)
sudo python3 sysdiag.py

# Selective diagnostics with custom line counts
sudo python3 sysdiag.py dmesg 100
sudo python3 sysdiag.py journalctl 20
```


## 🌐 Personal Website & Portfolio

Want to see my full profile, technical articles, and ongoing infrastructure experiments? 

Check out my live portfolio at:
👉 **[juandaferrer.xyz](https://juandaferrer.xyz)**

*What you'll find there:*
- 📑 Comprehensive resume and technical skill breakdown.
- 🚀 Deep dives into my personal projects and lab setups.
- 🐧 Linux system administration and automation insights.

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

