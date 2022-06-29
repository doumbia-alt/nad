import dj_database_url
from disnad.settings import*

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()
SECRET_KEY = 'v_ya#8%%4npw*7(^=7_ooznw$(i6kbp!i9wymp6s$b_@$@ees-'
ALLOWED_HOSTS = ['isnad.herokuapp.com']