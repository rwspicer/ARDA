"""
Django settings for arda_db project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wngfh!vr%wi8o5q7fej7ehl)lpjqtxe(+3_!f#@1r0ubve-z)n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']
# all the Nessa production values are set at the end of the file


# Application definition
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'dev_static')]
 
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'browser',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)


ROOT_URLCONF = 'arda_db.urls'

WSGI_APPLICATION = 'arda_db.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if DEBUG == False:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'arda_db_deployed.sqlite3'),
        'USER': 'arda-admin',
		'PASSWORD': 'ICannotRememberTheLastTimeI8',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'arda_db.sqlite3'),
            #~ 'USER': 'arda-admin',
            #~ 'PASSWORD': 'ICannotRememberTheLastTimeI8',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Anchorage'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


#~ if DEBUG == True
    #~ EMAIL_HOST = 'localhost'
    #~ EMAIL_PORT = 1025
    
ADMINS = (('Admin', 'atupek@alaska.edu'),('ross', 'rwspicer@alaska.edu'))
