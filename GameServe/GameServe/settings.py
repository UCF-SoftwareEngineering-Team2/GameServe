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
SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))
BASE_DIR = PROJECT_PATH


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
    'django_extensions',            # Allows ./manage runscript addDB
    'django_pdb',                   # Debugging ./manage.py runserver --ipdb
    'tastypie',                     # json REST calls
    'accounts',                     # User account models
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
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)
ROOT_URLCONF = 'GameServe.urls'
WSGI_APPLICATION = 'GameServe.wsgi.application'



#########################################################################################
#                              Database Configuration
#               https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#########################################################################################
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbsql',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}










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
STATIC_URL = '/static/'

# File Storage engine to use for ./manage.py collectstatic
STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'

# Add'l Paths to search for static files when invoking ./manage.py collectstatic
STATICFILES_DIRS = (os.path.join(PROJECT_PATH,'static'),)








#########################################################################################
#                               Template Files
#########################################################################################
AUTH_PROFILE_MODULE = 'accounts.User'
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)