# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=parking_system.settings \
    PORT=8000

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario no root
RUN useradd -m appuser && chown -R appuser:appuser /app

# Copiar el archivo de requisitos
COPY --chown=appuser:appuser requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorios necesarios
RUN mkdir -p /app/staticfiles /app/media && \
    chown -R appuser:appuser /app/staticfiles /app/media

# Copiar el código fuente
COPY --chown=appuser:appuser . .

# Exponer el puerto
EXPOSE ${PORT}

# Script de inicio
COPY --chown=appuser:appuser entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Cambiar al usuario no root
USER appuser

# Comando para ejecutar la aplicación
ENTRYPOINT ["/entrypoint.sh"] 