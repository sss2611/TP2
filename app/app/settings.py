import os
from pathlib import Path
import dj_database_url  # Requerido para manejar la URL de la base de datos de Render

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# Carga la clave secreta desde la variable de entorno de Render
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-insecure-key')


# SECURITY WARNING: don't run with debug turned on in production!
# Desactiva DEBUG si estamos en el entorno de Render, si no, usa el valor por defecto.
DEBUG = 'RENDER' not in os.environ 


# Hosts Permitidos
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
# Añade el nombre de host externo proporcionado por Render
if 'RENDER_EXTERNAL_HOSTNAME' in os.environ:
    RENDER_EXTERNAL_HOSTNAME = os.environ['RENDER_EXTERNAL_HOSTNAME']
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cuentas',
    'mantenimiento'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # AÑADE WhiteNoise AQUÍ para servir los archivos estáticos en producción
    "whitenoise.middleware.WhiteNoiseMiddleware", 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# Configuración para usar la variable de entorno DATABASE_URL de Render
if os.environ.get('DATABASE_URL'):
    # PostgreSQL para Render
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600  # Conexiones persistentes
        )
    }
else:
    # SQLite para desarrollo local (si DATABASE_URL no está definida)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# ... (deja esta sección sin cambios)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# ... (deja esta sección sin cambios)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
# Directorio donde Django colocará los archivos estáticos para producción (requerido por WhiteNoise)
STATIC_ROOT = BASE_DIR / 'staticfiles' 

# Configuración de WhiteNoise para comprimir y servir los estáticos de forma eficiente
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'    

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = "cuentas.CustomUser"