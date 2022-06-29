import dj_database_url
from disnad.settings import*

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()
SECRET_KEY = '91q@vd01_b2zym!w^@(mc7%8yq^2zw3c#$mp(_&u!e@lg!^$(4'
ALLOWED_HOSTS = ['isnad.herokuapp.com']