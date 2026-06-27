# This code is written so a cronjob can execute a Python script and generate a log file with system information,
# then create a .txt file with the logs. The file must be created in the same folder as the script,
# named sys-diagnostic-(date,time).txt so a SysAdmin can diagnose an issue. To execute it, use the shell command
# "sudo python3 sysdiag.py (journalctl, dmesg, systemctl) (number of lines to display)". If the first argument is not specified,
# all three outputs will be shown, separated by 5 blank lines. If the number of lines is not specified,
# only 50 lines of each will be shown. The code starts below.
# visit juandaferrer.xyz or my github.com/juandaferrer/linux-toolkit for more information about my projects and Python scripts
import subprocess
import sys
from datetime import datetime
import os

if os.geteuid() != 0:
    print("[ERROR] Run this script with sudo.")
    sys.exit(1)

try: # cronjob to run the Python script and generate a log file with system information
    log_type = sys.argv[1] if len(sys.argv) > 1 else "all"
    num_lines = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"sys-diagnostic-{timestamp}.txt"

    with open(log_filename, "w") as log_file:
        
        # 1. journalctl -p 4 -n <num_lines> --no-pager
        if log_type in ["journalctl", "all"]:
            log_file.write("=== journalctl (ERRORS/WARNINGS) ===\n")
            # Add -p 4 to keep the diagnosis focused on critical issues
            res = subprocess.run(["journalctl", "-p", "4", "-n", str(num_lines), "--no-pager"], capture_output=True, text=True)
            log_file.write(res.stdout if res.stdout else "No issues found.\n")
            log_file.write("\n" * 5)

        # 2. dmesg -T --level=err,warn
        if log_type in ["dmesg", "all"]:
            log_file.write("=== dmesg (KERNEL ERR/WARN) ===\n")
            # Filter by level and trim lines manually in Python
            res = subprocess.run(["dmesg", "-T", "--level=err,warn"], capture_output=True, text=True)
            lines = res.stdout.splitlines()[-num_lines:]
            log_file.write("\n".join(lines) if lines else "No kernel issues found.\n")
            log_file.write("\n" * 5)

        # 3. systemctl --failed --no-legend
        if log_type in ["systemctl", "all"]:
            log_file.write("=== systemctl (FAILED SERVICES) ===\n")
            # Only failed services and apply the manual limit
            res = subprocess.run(["systemctl", "--failed", "--no-legend"], capture_output=True, text=True)
            lines = res.stdout.splitlines()[-num_lines:]
            log_file.write("\n".join(lines) if lines else "All services running smoothly.\n")
            log_file.write("\n" * 5)

    print(f"[OK] Log file '{log_filename}' created successfully.")

except Exception as e: # error handling to capture any error that may occur during script execution
    print(f"An error occurred: {e}")
    sys.exit(1)