# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el código fuente del proyecto al contenedor
COPY . .

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
