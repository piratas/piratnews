
DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "%(db_name)s",
        # Not used with sqlite3.
        "USER": "%(db_name)s",
        # Not used with sqlite3.
        "PASSWORD": "%(db_password)s",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
        }
}

ALLOWED_HOSTS = ['127.0.0.1', '.localhost']
ALLOWED_HOSTS += %(hosts)s 

SECRET_KEY = '%(secret_key)s'


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
        }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

AWS_ACCESS_KEY_ID = '%(aws_key)s'
AWS_SECRET_ACCESS_KEY = '%(aws_secret)s'

