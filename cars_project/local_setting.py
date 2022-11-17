# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9awa4tebni$cfe8@z-22(cna=6q4s)1ib5+!=zk*ppimmb=f5@'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '2139NW118th!'
    }
}