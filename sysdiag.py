import subprocess
import sys

"""
SPANISH: Esta idea vino de que alguien quería ver la salida de diagnóstico del sistema en un número específico de líneas,
y yo pensé que sería útil tener un script que permitiera al usuario especificar cuántas líneas de salida de diagnóstico del sistema desea ver,
y aprovechar de subir un script a mi GitHub para que otros puedan usarlo también. El script solicita al usuario que ingrese
el número de líneas que desea ver y el comando de diagnóstico del sistema que desea ejecutar, y la salida
se va a un archivo de texto llamado 'sysdiag_output.txt'. Esto permite al usuario ver la salida de diagnóstico del sistema
en un formato más manejable y también guardar la salida para referencia futura.

Por favor, ten en cuenta que este script requiere privilegios de superusuario para ejecutar ciertos comandos de diagnóstico del sistema,
y el usuario debe tener cuidado al ejecutar comandos que puedan afectar la estabilidad del sistema. Además, 
por favor, asegúrate de tener los permisos necesarios para ejecutar los comandos de diagnóstico del sistema en tu entorno.

Considera que este script es solo un ejemplo y puede requerir modificaciones para adaptarse a tus necesidades específicas.

También es importante recordar que este script está diseñado para ser ejecutado en un entorno Linux,
y puede no funcionar correctamente en otros sistemas operativos.

Dejame un comentario si tienes alguna pregunta o sugerencia sobre cómo mejorar este script. ¡Gracias por usarlo!

Visita mi GitHub https://github.com/juandaferrer/IaCofFerrer para más scripts útiles, visita mi sitio web juandaferrer.xyz.

USA ESTE SCRIPT BAJO TU PROPIO RIESGO. NO ME HAGO RESPONSABLE DE NINGÚN DAÑO QUE PUEDA OCASIONAR EL USO DE ESTE SCRIPT.
NO USAR PARA PROPÓSITOS MALICIOSOS, EL DE ARRIBA TE ESTA OBSERVANDO.
"""

lines = int(input("Enter the NUMBER (e.g., 10) of lines to display from the system diagnostic output: "))

diag = input("Enter the system diagnostic command to run (e.g., 'dmesg', 'journalctl', 'systemctl'): ")

if lines == 0:
    print("No lines to display. Exiting.") #para que abres el script si no quieres ver nada? no entiendo la logica de la vida humana...
    sys.exit(0)

if lines < 0:
    print("Number of lines cannot be negative. Exiting.") #... 300.000 años de evolución y no puedes entender que no se puede mostrar un número negativo de líneas...
    sys.exit(1)

if diag not in ['dmesg', 'journalctl', 'systemctl']: #vamos, eres un ser humano inteligente...
    print("Invalid command. Please enter a valid system diagnostic command.")
    sys.exit(1)

if diag == 'dmesg':
    command = ['dmesg', '-T', '--level=err,warn']  # Solo errores y advertencias del kernel
elif diag == 'journalctl':
    command = ['journalctl', '-p', '4', '-n', str(lines)]  # Solo errores y advertencias del sistema (-p 4)
elif diag == 'systemctl':
    command = ['systemctl', '--failed', '--no-legend'] # Solo servicios fallidos


try:
    # Ejecuta el comando estructurado arriba
    output = subprocess.check_output(command, text=True)
    
    # Si es systemctl, aplicamos el límite de líneas manualmente cortando el texto
    if diag == 'systemctl':
        output = "\n".join(output.splitlines()[-lines:])
        
    # Nombre de archivo dinámico según el comando elegido
    filename = f"{diag}-failed-log.txt"
    
    # Guardar los resultados en el archivo
    with open(filename, "w") as file:
        file.write(output)
        
    print(f"\n[OK] Diagnostic successfully completed, the output is saved in: {filename}")

except subprocess.CalledProcessError as e:
    print(f"\n[ERROR] Failed to execute '{diag}'. Did you forget to use sudo? you CAN'T forget to use sudo, you are not root, and you are trying to run a command that requires root privileges. Please try again with 'sudo' (sudo sysdiag.py).")
    # sys.exit(1)