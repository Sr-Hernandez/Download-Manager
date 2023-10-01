import requests
from tqdm import tqdm
import argparse
import requests
from tkinter import filedialog
from tqdm import tqdm
import os




parser = argparse.ArgumentParser(description='Gestor de descargas en Python')
parser.add_argument('-u', '--url', type=str, help='URL del archivo a descargar', required=True)
args = parser.parse_args()
url = args.url

def descargar_archivo(url, nombre_archivo):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
   

    with open(nombre_archivo, 'wb') as archivo:
        with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, colour='green') as barra_progreso:
            for data in response.iter_content(chunk_size=1024):
                archivo.write(data)
                barra_progreso.update(len(data))

if __name__ == "__main__":
    # url = "https://download2279.mediafire.com/gmrzlek8qhhgFjhmxmpurONuvY9BlXB3U2b6M9gLUqCoctKQD1yELbkeJjI-2z_GQ4KQtK72joWGLG39VL32vXkxIyEB4BTs2zIlxDbam_MXFPl5FmvoRQb3V1IATRqPYBkMLIrFrzk0iYJZ9bHLGGxdv7N4LVU6_LK8D6o-vXsnz3I/032farq6vfvo674/M11ort1alK11omb11at11UE-22.03.2022-elamigos.part07.rar"  # Reemplaza con una URL de descarga real
    nombre_archivo = os.path.basename(url)

    print(f"Descargando {nombre_archivo}...")
    descargar_archivo(url, nombre_archivo)
    print("Descarga completa.")
