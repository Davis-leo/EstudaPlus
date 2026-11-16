"""
Django settings for core project - VERSÃO KUBERNETES / DOCKER
Compatível com local (Laragon/.env) e com K8s (ConfigMap + Secret)
"""
from pathlib import Path
from decouple import config
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Segurança / Debug via env ---
# No K8s: DJANGO_SECRET_KEY vem do Secret backend-secret
# Local: vem do .env
SECRET_KEY = config('DJANGO_SECRET_KEY', default='dev-inseguro-troque-em-prod-123')

# No K8s deixe DEBUG=False. Local pode deixar True.
DEBUG = config('DEBUG', default=True, cast=bool)

# TRAVA 1 CORRIGIDA: antes era [] -> K8s rejeita todo request com DisallowedHost
# Agora aceita qualquer host no cluster, ou lista via env
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',') if config('ALLOWED_HOSTS', default='*') != '*' else ['*']

APPEND_SLASH = False

# TRAVA 2 CORRIGIDA: antes fixo em 127.0.0.1 -> dentro do pod isso não existe
# Agora usa env, com fallback que funciona no K8s
BASE_URL = config('BASE_URL', default='http://backend-service:8000')
FRONTEND_BASE_URL = config('FRONTEND_BASE_URL', default='http://localhost:3000')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'accounts',
    'courses',
    'dashboard',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# --- Database ---
# No K8s: DB_HOST=mysql-service (vem do ConfigMap backend-config)
# Local: DB_HOST=127.0.0.1 (vem do .env)
# decouple já faz o cast, mas o K8s manda PORT como string "3306" -> cast=int resolve
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'NAME': config('DB_NAME', default='estudaplus'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'PORT': config('DB_PORT', default='3306', cast=int),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTH_USER_MODEL = 'accounts.User'

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
# Necessário para coletar static no Docker (se usar collectstatic)
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.utils.custom_exception.custom_exception_handler',
    'DEFAULT_RENDERER_CLASSES': [
        'core.utils.renderers.CustomJSONRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7)
}