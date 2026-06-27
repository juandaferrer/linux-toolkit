import subprocess
import sys

"""
This idea came from someone wanting to see system diagnostic output with a specific number of lines,
and I thought it would be useful to have a script that lets the user specify how many lines of system diagnostic output to display,
and to upload a script to my GitHub for others to use as well. The script asks the user to enter
how many lines they want to see and which system diagnostic command to run, then dumps the output
dynamically into a text file according to the chosen command (e.g. 'journalctl-failed-log.txt'). This lets the user view the output
in a more manageable format and also save the log for future reference.

Please note that this script requires superuser privileges to execute certain system diagnostic commands,
and the user should be careful when running commands that could affect system stability. Also,
make sure you have the necessary permissions to run the system diagnostic commands in your environment.

Keep in mind that this script is only an example and may require modifications to fit your specific needs.

It is also important to remember that this script is designed to run in a Linux environment,
and may not work correctly on other operating systems.

Leave me a comment if you have any questions or suggestions on how to improve this script. Thanks for using it!

Visit my GitHub https://github.com/juandaferrer/linux-toolkit for more useful scripts, visit my website juandaferrer.xyz.

USE THIS SCRIPT AT YOUR OWN RISK. I AM NOT RESPONSIBLE FOR ANY DAMAGE THAT MAY BE CAUSED BY USING THIS SCRIPT.
DO NOT USE FOR MALICIOUS PURPOSES, THE ONE ABOVE IS WATCHING YOU.
"""

raw_input = input("Enter the NUMBER (e.g., 10) of lines to display from the system diagnostic output: ")

try:
    # Intentamos convertir a entero puro
    lines = int(raw_input)
except ValueError:
    # Si falla, verificamos si el usuario metió un flotante
    if '.' in raw_input or ',' in raw_input:
        print(f"\nCome on bro, you have more than a decade of experience in life itself, in literature, and in the analytics of your surroundings, and you come up with {raw_input}? Brother, type that right.")
    else:
        # Si puso texto o cualquier otra basura
        print(f"\n[ERROR] '{raw_input}' is not even a valid number. Exiting.")
    sys.exit(1)

if lines == 0:
    print("No lines to display. Exiting.") # Why open the script if you do not want to see anything? I do not understand the logic of human life...
    sys.exit(0)

if lines < 0:
    print("Number of lines cannot be negative. Exiting.") # ...300,000 years of evolution and you still cannot understand that you cannot display a negative number of lines...
    sys.exit(1)

diag = input("Enter the system diagnostic command to run (e.g., 'dmesg', 'journalctl', 'systemctl'): ")

if diag not in ['dmesg', 'journalctl', 'systemctl']: # come on, you are an intelligent human being...
    print("Invalid command. Please enter a valid system diagnostic command.")
    sys.exit(1)

# SOLUCIÓN: Aplicamos el límite nativo en dmesg y journalctl
if diag == 'dmesg':
    command = ['dmesg', '-T', '--level=err,warn']  
elif diag == 'journalctl':
    command = ['journalctl', '-p', '4', '-n', str(lines)]  # Only system errors and warnings (-p 4)
elif diag == 'systemctl':
    command = ['systemctl', '--failed', '--no-legend'] # Only failed services

try:
    # Execute the command structured above
    output = subprocess.check_output(command, text=True)
    
    # If it's systemctl or dmesg, apply the line limit manually by trimming the text
    if diag in ['systemctl', 'dmesg']:
        output = "\n".join(output.splitlines()[-lines:])
        
    # Dynamic filename according to the chosen command
    filename = f"{diag}-failed-log.txt"
    
    # Save the results to the file
    with open(filename, "w") as file:
        file.write(output)
        
    print(f"\n[OK] Diagnostic successfully completed, the output is saved in: {filename}")

except subprocess.CalledProcessError as e:
    print(f"\n[ERROR] Failed to execute '{diag}'. Did you forget to use sudo?")
    print(f"System details: {e}")
    sys.exit(1)
