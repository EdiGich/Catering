"""
Django settings for catering_website project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
#       import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
#       env = environ.Env()
#       environ.Env.read_env()  # Read the .env file if it exists

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#       SECRET_KEY =env('SECRET_KEY', default='django-insecure-u(tgga&l^2^@pz89ez@rgz7zxg9=#!+#@!cqr!jzgms*f+--6s')

# SECURITY WARNING: don't run with debug turned on in production!
#       DEBUG = env.bool('DEBUG', default=True)

# ALLOWED_HOSTS = ['15bf-41-215-141-174.ngrok-free.app']
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])


# Application definition

INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'corsheaders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'catering_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'catering_website.wsgi.application'

# REST Framework configuration
# REST_FRAMEWORK = {
#     'DEFAULT_A[UTHENTICATION_CLASSES': 
#         ['rest_framework_simplejwt.authentication.JWTAuthentication','rest_framework.authentication.TokenAuthentication',],
#     'DEFAULT_PERMISSION_CLASSES': 
#         ('rest_framework.permissions.AllowAny','rest_framework.permissions.IsAuthenticated',)}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Simple JWT settings (optional customization)
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # I can adjust this as needed
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # Your Flutter web URL
# ]
CORS_ALLOW_ALL_ORIGINS = True


# Email settings
#       EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
#       EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
#       EMAIL_PORT = env('EMAIL_PORT', default=587)
#       EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)

#       EMAIL_HOST_USER = env('EMAIL_HOST_USER') 
#       EMAIL_HOST_PASSWORD =  env('EMAIL_HOST_PASSWORD')
#       DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

#will delete these after environ starts working
SECRET_KEY='django-insecure-u(tgga&l^2^@pz89ez@rgz7zxg9=#!+#@!cqr!jzgms*f+--6s'
ALLOWED_HOSTS=['127.0.0.1', 'localhost', '10.0.2.2','15bf-41-215-141-174.ngrok-free.app']
DEBUG=True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreplydtcaterers@gmail.com'  # Your new Gmail address
EMAIL_HOST_PASSWORD = 'jlkl sxvs xhmv sxhm' # The password for this account
DEFAULT_FROM_EMAIL = 'noreplydtcaterers@gmail.com'