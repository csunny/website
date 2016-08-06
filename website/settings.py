"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
<<<<<<< HEAD
=======
# import xadmin
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v9zg7_-mwicz=471#*bs(kf&e@=)-#0g&!e%=fkgs&z9c)0*0y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

<<<<<<< HEAD
ALLOWED_HOSTS = ['localhost', 'example.com']
=======
ALLOWED_HOSTS = []
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222

################
#  xadmin conf #
#              #
#    *****     #
################
<<<<<<< HEAD
ADMINS = (
    # (name ,email name)
    ('magic', 'magic.chen@fuwo.com'),
)
MANAGERS = ADMINS
=======
# ADMINS=(
#     #(name ,email name)
#     ('magic','magic.chen@fuwo.com'),
# )
# MANAGERS = ADMINS
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',
<<<<<<< HEAD
    # 'debug_toolbar',
=======
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
<<<<<<< HEAD
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
=======
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
)

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
	'USER': '',
	'PASSWORD': '',
	'HOST':'',
	'PORT':'',
    }
}

<<<<<<< HEAD
# CELERY SETTINGS
BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

=======
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

<<<<<<< HEAD
# INTERNAL_IPS = ('127.0.0.1',)
=======

>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'static'),
)


##########################
<<<<<<< HEAD
# There is something error#
=======
#There is something error#
>>>>>>> 90f339b206b0e46222c2a3534b2e2a9b82322222
#     **need check**     #
##########################

# from django.utils.translation import ugettext_lazy as _
# TEMPLATES = (
#     ('zh-cn',_("Simplified Chinese")),
#     ('en',_('English')),
#
# )
# LOCALE_PATHS = (
#     os.path.join(BASE_DIR,"locale"),
# )
#
