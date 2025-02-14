# Usa Python 3.11 como imagen base
FROM python:3.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /api_gateway

# Copiar requirements.txt antes de instalar dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar solo el código necesario
COPY .  .


# Exponer el puerto 8000
EXPOSE 8000

# Cambiar el directorio de trabajo a api_gateway antes de ejecutar uvicorn
#WORKDIR /app/api_gateway

# Asegurar que uvicorn carga correctamente el módulo
ENTRYPOINT ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
