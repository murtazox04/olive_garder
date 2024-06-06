from decouple import config
from . import INSTALLED_APPS, MIDDLEWARE

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS.append("corsheaders")
MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "olive_garden_admin",  # Make sure this matches POSTGRES_DB
        "USER": "root",  # Make sure this matches POSTGRES_USER
        "PASSWORD": "root",  # Make sure this matches POSTGRES_PASSWORD
        "HOST": "admin_db",  # This should match the service name in docker-compose.yml
        "PORT": "5432",
    }
}

CORS_ALLOW_METHODS = [
    '*'
]
CORS_ALLOW_HEADERS = [
    '*'
]
CORS_ORIGIN_WHITELIST = [
    'https://*',
    'http://*'
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
