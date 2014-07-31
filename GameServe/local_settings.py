from settings import PROJECT_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dbsql",
        "USER": "kizzlebot",
        "PASSWORD": "tree444",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
