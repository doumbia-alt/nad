import dj_database_url
from disnad.settings import*

DEBUG = False
TEMPLATE_DEBUG = False


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = '91q@vd01_b2zym!w^@(mc7%8yq^2zw3c#$mp(_&u!e@lg!^$(4'
ALLOWED_HOSTS = ['www.institut-isnad.com']