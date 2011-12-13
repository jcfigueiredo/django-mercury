DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/djmercury.db',
    }
}

INSTALLED_APPS = ['djmercury']
ROOT_URLCONF = ['djmercury.urls']
