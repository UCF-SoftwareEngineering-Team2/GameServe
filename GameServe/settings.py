"""
Django settings for GameServe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os


#########################################################################################
#                               Project Paths
#########################################################################################
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))
PROJECT_ROOT = PROJECT_PATH

#########################################################################################
#              Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
#########################################################################################
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't$-eqj2!z(dn8mhimh9j+%f$9x1(y#8jzli)65g_$mh&5w-9=7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#########################################################################################
#                             Application definition
#########################################################################################
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', # Allows permissions association with models
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'south',

    # Debug Tools
    'django_extensions',            # Allows ./manage runscript addDB
    'django_pdb',                   # Debugging ./manage.py runserver --ipdb

    # APIs
    'tastypie',                     # json REST calls
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    "sendgrid",


    # Project-specifics
    'profile',                     # User account models
    'events',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',    # Manage sessions b/t req
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # assoc users w/ req
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_pdb.middleware.PdbMiddleware',                     # https://github.com/tomchristie/django-pdb
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend"
)

# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}
SITE_ID=1

# Django allauth. Require username and email for registeration
# Allow login via username or email
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD='username_email'


ACCOUNT_SIGNUP_FORM_CLASS='profile.forms.RegisterForm'





ROOT_URLCONF = 'GameServe.urls'
WSGI_APPLICATION = 'GameServe.wsgi.application'




#########################################################################################
#                              Database Configuration
#               https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#########################################################################################

# we only need the engine name, as heroku takes care of the rest
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gameserve',
        'USER': 'kizzlebot',
        'PASSWORD': 'tree444',
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


SENDGRID_EMAIL_HOST = "smtp.sendgrid.net"
SENDGRID_EMAIL_PORT = 587
SENDGRID_EMAIL_USERNAME = "kizzlebot"
SENDGRID_EMAIL_PASSWORD = "tree4444"

# Specify custom user model
AUTH_USER_MODEL = 'profile.User'
ACCOUNT_EMAIL_VERIFICATION = "optional"



#########################################################################################
#                               Internationalization
#                   https://docs.djangoproject.com/en/1.6/topics/i18n/
#########################################################################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = False








#########################################################################################
#                       Static files (CSS/js) [http://bit.ly/djangoStatic]
#
# Info: For each application, by default django searches static files in myApp/static/
#########################################################################################
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'
# File Storage engine to use for ./manage.py collectstatic
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)









#########################################################################################
# Template Settings
#########################################################################################
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)




if os.environ.get('ENVIRON') == None:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
        }
    }

    # Parse database configuration from $DATABASE_URL environment variable on heroku
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Static asset configuration
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
       os.path.abspath(os.path.join(PROJECT_PATH, 'static')),
    )


# try to load local_settings.py if it exists
try:
  from local_settings import *
except Exception as e:
  pass
