import os
from pathlib import Path
import environ

env = environ.Env(
    DEBUG=(bool, False)  # по умолчанию включаем DEBUG локально
)
environ.Env.read_env()

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECRET_KEY = env('SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split(",")



# Без жёстких ограничений безопасности для локалки:
# if not DEBUG:
#     INTERNAL_IPS = ['127.0.0.1']
#     SECURE_HSTS_SECONDS = 0
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = False
#     SECURE_HSTS_PRELOAD = False

#     SECURE_CONTENT_TYPE_NOSNIFF = False
#     SECURE_BROWSER_XSS_FILTER = False
#     X_FRAME_OPTIONS = 'DENY'

#     CSRF_COOKIE_SECURE = False
#     SESSION_COOKIE_SECURE = False
#     SECURE_SSL_REDIRECT = False

if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # НЕ включаем SECURE_SSL_REDIRECT, Render сам терминирует TLS, нам достаточно SECURE_PROXY_SSL_HEADER


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

# SOCIAL_AUTH_FACEBOOK_KEY = env("SOCIAL_AUTH_FACEBOOK_KEY")
# SOCIAL_AUTH_FACEBOOK_SECRET = env("SOCIAL_AUTH_FACEBOOK_SECRET")

# SOCIAL_AUTH_TWITTER_KEY = env("SOCIAL_AUTH_TWITTER_KEY")
# SOCIAL_AUTH_TWITTER_SECRET = env("SOCIAL_AUTH_TWITTER_SECRET")

INSTALLED_APPS = [
    'social_django',
    'accounts',
    'rest_framework',
    'blog',
    'bootstrap5',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',"django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ROOT_URLCONF = 'blog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog', 'templates')],
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

WSGI_APPLICATION = 'blog_project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': env('DB_PORT'),
#     }
# }


# DATABASES = {
#     "default": env.db(
#         "DATABASE_URL",
#         default=f"postgres://{env('DB_USER')}"
#                 f":{env('DB_PASSWORD')}"
#                 f"@{env('DB_HOST', default='localhost')}"
#                 f":{env('DB_PORT', default='5432')}"
#                 f"/{env('DB_NAME')}"
#     )
# }

import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
