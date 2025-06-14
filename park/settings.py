import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'parking_db_3of6',
        'USER': 'parking_user',
        'PASSWORD': 'zIa9A8kicLBDh8hC4k6xq4DZXH9oQGfw',
        'HOST': 'dpg-d13s1c8gjchc73fgk4t0-a.oregon-postgres.render.com',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,  # Deshabilitar conexiones persistentes
        'OPTIONS': {
            'sslmode': 'require',
            'connect_timeout': 30,
            'keepalives': 1,
            'keepalives_idle': 30,
            'keepalives_interval': 10,
            'keepalives_count': 5,
            'tcp_user_timeout': 30000,  # 30 segundos en milisegundos
        }
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'staticfiles'))

# Media files
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.RoleAssignmentMiddleware',
    'users.middleware.AuditMiddleware',
    'users.middleware.TwoFactorAuthMiddleware',
] 

# Configuración de Email
EMAIL_BACKEND = 'contactoisfaj@gmail.com'
EMAIL_HOST = 'contactoisfaj@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'contactoisfaj@gmail.com'
EMAIL_HOST_PASSWORD = 'aorf dfzp wxwo ykos'
DEFAULT_FROM_EMAIL = 'contactoisfaj@gmail.com'
ADMIN_EMAIL = 'contactoisfaj@gmail.com'  # Email del administrador para notificaciones

# Configuración de Sesión
SESSION_COOKIE_AGE = 3600  # 1 hora en segundos
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = True  # Solo enviar cookies por HTTPS
SESSION_COOKIE_HTTPONLY = True  # Prevenir acceso a cookies por JavaScript

# Configuración de Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'users': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Configuración de Autenticación de Dos Factores
TWO_FACTOR_AUTH = {
    'ENABLED': True,
    'REQUIRED_FOR_ADMIN': True,
    'REQUIRED_FOR_STAFF': True,
    'SESSION_EXPIRY': 3600,  # 1 hora en segundos
    'BACKUP_CODES_COUNT': 10,
    'BACKUP_CODES_LENGTH': 8,
}

# Configuración de Notificaciones
NOTIFICATION_SETTINGS = {
    'ENABLE_EMAIL_NOTIFICATIONS': True,
    'ENABLE_PUSH_NOTIFICATIONS': False,
    'DEFAULT_NOTIFICATION_TYPES': ['RESERVATION', 'PAYMENT', 'SYSTEM'],
}

# Configuración de Preferencias de Usuario
USER_PREFERENCES = {
    'DEFAULT_THEME': 'light',
    'AVAILABLE_THEMES': ['light', 'dark', 'system'],
    'DEFAULT_NOTIFICATION_PREFERENCES': {
        'RESERVATION': True,
        'PAYMENT': True,
        'SYSTEM': True,
    },
}

# Configuración de reintentos de conexión
DB_CONN_RETRY_TIMEOUT = 30  # segundos
DB_CONN_RETRY_INTERVAL = 5  # segundos
DB_CONN_MAX_RETRIES = 5  # número máximo de reintentos 