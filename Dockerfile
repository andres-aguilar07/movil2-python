# imagen base de python
FROM python:3.10

WORKDIR /app

# Copiamos los archivos al contenedor (docker maneja su propio sistema de archivos)
COPY . .

# Se instalan las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Se expone el puerto
EXPOSE 5000

# Se define el comando de ejecución
CMD [ "python", "app/app.py" ]