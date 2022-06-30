import dj_database_url
from disnad.settings import*

DEBUG = True
TEMPLATE_DEBUG = True


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['isnad.herokuapp.com']