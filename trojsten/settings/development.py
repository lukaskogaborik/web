from __future__ import absolute_import
from trojsten.settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'database.sqlite3'),
    },
}

DEBUG = True
TEMPLATE_DEBUG = True
SUBMIT_PATH = '/tmp'

#INSTALLED_APPS += ('debug_toolbar',)
#MIDDLEWARE_CLASSES = (('debug_toolbar.middleware.DebugToolbarMiddleware',)
#    + MIDDLEWARE_CLASSES)

INTERNAL_IPS = ('127.0.0.1',)