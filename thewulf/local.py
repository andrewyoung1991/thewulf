from thewulf.common import *

DEBUG = True
TEMPLATE_DEBUG = True
VERBOSE_SQL = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'thewulf',
        'USER': 'thewulf',
        'PASSWORD': 'thewulf-rules'
    }
}
