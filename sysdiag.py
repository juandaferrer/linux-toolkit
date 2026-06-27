import subprocess
import sys

"""
SPANISH: Esta idea vino de que alguien quería ver la salida de diagnóstico del sistema en un número específico de líneas,
y yo pensé que sería útil tener un script que permitiera al usuario especificar cuántas líneas de salida de diagnóstico del sistema desea ver,
y aprovechar de subir un script a mi GitHub para que otros puedan usarlo también. El script solicita al usuario que ingrese
el número de líneas que desea ver y el comando de diagnóstico del sistema que desea ejecutar, y la salida
se vuelca de forma dinámica en un archivo de texto según el comando elegido (ej. 'journalctl-failed-log.txt'). Esto permite al usuario ver la salida
en un formato más manejable y también guardar el registro para referencia futura.

Por favor, ten en cuenta que este script requiere privilegios de superusuario para ejecutar ciertos comandos de diagnóstico del sistema,
y el usuario debe tener cuidado al ejecutar comandos que puedan afectar la estabilidad del sistema. Además, 
por favor, asegúrate de tener los permisos necesarios para ejecutar los comandos de diagnóstico del sistema en tu entorno.

Considera que este script es solo un ejemplo y puede requerir modificaciones para adaptarse a tus necesidades específicas.

También es importante recordar que este script está diseñado para ser ejecutado en un entorno Linux,
y puede no funcionar correctamente en otros sistemas operativos.

Dejame un comentario si tienes alguna pregunta o sugerencia sobre cómo mejorar este script. ¡Gracias por usarlo!

Visita mi GitHub https://github.com/juandaferrer/linux-toolkit para más scripts útiles, visita mi sitio web juandaferrer.xyz.

USA ESTE SCRIPT BAJO TU PROPIO RIESGO. NO ME HAGO RESPONSABLE DE NINGÚN DAÑO QUE PUEDA OCASIONAR EL USO DE ESTE SCRIPT.
NO USAR PARA PROPÓSITOS MALICIOSOS, EL DE ARRIBA TE ESTA OBSERVANDO.
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
    print("No lines to display. Exiting.") #para que abres el script si no quieres ver nada? no entiendo la logica de la vida humana...
    sys.exit(0)

if lines < 0:
    print("Number of lines cannot be negative. Exiting.") #... 300.000 años de evolución y no puedes entender que no se puede mostrar un número negativo de líneas...
    sys.exit(1)

diag = input("Enter the system diagnostic command to run (e.g., 'dmesg', 'journalctl', 'systemctl'): ")

if diag not in ['dmesg', 'journalctl', 'systemctl']: #vamos, eres un ser humano inteligente...
    print("Invalid command. Please enter a valid system diagnostic command.")
    sys.exit(1)

# SOLUCIÓN: Aplicamos el límite nativo en dmesg y journalctl
if diag == 'dmesg':
    command = ['dmesg', '-T', '--level=err,warn']  
elif diag == 'journalctl':
    command = ['journalctl', '-p', '4', '-n', str(lines)]  # Solo errores y advertencias del sistema (-p 4)
elif diag == 'systemctl':
    command = ['systemctl', '--failed', '--no-legend'] # Solo servicios fallidos

try:
    # Ejecuta el comando estructurado arriba
    output = subprocess.check_output(command, text=True)
    
    # Si es systemctl o dmesg, aplicamos el límite de líneas manualmente cortando el texto
    if diag in ['systemctl', 'dmesg']:
        output = "\n".join(output.splitlines()[-lines:])
        
    # Nombre de archivo dinámico según el comando elegido
    filename = f"{diag}-failed-log.txt"
    
    # Guardar los resultados en el archivo
    with open(filename, "w") as file:
        file.write(output)
        
    print(f"\n[OK] Diagnostic successfully completed, the output is saved in: {filename}")

except subprocess.CalledProcessError as e:
    print(f"\n[ERROR] Failed to execute '{diag}'. Did you forget to use sudo?")
    print(f"System details: {e}")
    sys.exit(1)
