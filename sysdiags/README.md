
## System Diagnostics Utilities (SysDiag)

This directory contains a set of automated Python utilities designed to capture, filter, and log critical system events from `journalctl`, `dmesg`, and `systemctl`. 

The core objective is to replace rigid interactive scripts with flexible, production-ready tools that can be operated manually by a SysAdmin or executed silently via scheduled tasks (`cron`).

## Included Scripts

* **`sysdiag.py` (Human-Oriented):** An interactive CLI utility featuring a clean text menu and input validation. Ideal for quick, manual troubleshooting sessions.
* **`sysdiag-sa.py` (Automation-Oriented):** A non-blocking command-line interface tool built for automation, monitoring pipelines, and cronjobs.

---

## Features

* **Intelligent Log Filtering:** Minimizes noise by targeting only high-priority events (`-p 4` warnings/errors in `journalctl`, `--level=err,warn` in `dmesg`, and `--failed` units in `systemctl`).
* **Dual Execution Mode:** Runs specific diagnostics on demand or generates a consolidated full system report.
* **Cron-Safe Paths:** Automatically resolves absolute execution directory paths to ensure logs are written in the correct directory when run by system daemons.
* **Memory-Efficient Slicing:** Uses native Python string splitting to handle large log outputs without saturating system memory.

---

## Usage (`sysdiag.py`)

### 1. Consolidated System Report
If executed without arguments, it captures the last 50 lines of all three diagnostic modules, separating each section cleanly with 5 line breaks.
```bash
sudo python3 sysdiag.py

```

### 2. Selective Diagnostic Lookup

Pass the target module and the desired line limit as arguments to filter the output dynamically:

```bash
sudo python3 sysdiag.py dmesg 100
sudo python3 sysdiag.py journalctl 20
sudo python3 sysdiag.py systemctl 15

```

---

## Automation (Cronjob Setup)

To schedule a full system health audit every hour without human intervention, append the following line to your system crontab (`/etc/crontab`):

```text
0 * * * * root /usr/bin/python3 /path/to/your/folder/sysdiag.py

```

---

## Requirements & Security

* **OS:** Linux (systemd-based distributions such as RHEL/Debian).
* **Runtime:** Python 3.x.
* **Privileges:** These utilities require `root` privileges (`sudo`) to read restricted system rings and journals. Non-root executions will terminate safely with an error code.
