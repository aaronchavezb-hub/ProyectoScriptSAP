import pyautogui
import os
from datetime import datetime

# Crear carpeta si no existe
carpeta_destino = "capturas_pantalla"
os.makedirs(carpeta_destino, exist_ok=True)

# Generar nombre de archivo con fecha y hora
nombre_archivo = datetime.now().strftime("captura_%Y%m%d_%H%M%S.png")
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)

# Tomar captura de pantalla
imagen = pyautogui.screenshot()

# Guardar imagen
imagen.save(ruta_completa)

print(f"La captura de pantalla se ha guardado en: {ruta_completa}")



import subprocess
import os

# Ruta del archivo que deseas ejecutar
ruta_archivo = "captura.png"  # Cambia esto por la ruta real

# Verifica si el archivo existe
if os.path.exists(ruta_archivo):
    subprocess.run(ruta_archivo, shell=True)
    print("Archivo ejecutado correctamente.")
else:
    print("El archivo no existe.")
