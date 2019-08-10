from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'postgres',
        'PASSWORD': 'docker',
        'HOST': '35.178.17.71',
        'PORT': '',
    }
}
DEBUG = True
