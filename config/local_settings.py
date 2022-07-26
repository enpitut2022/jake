import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'django-insecure-hxetmh14ypo_@ft&=5(=a(&ott8=&)qygy#)suu#$zk)3$bpzl'

#settings.pyからそのままコピー
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
DEBUG = True