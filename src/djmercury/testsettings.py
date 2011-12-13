DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': '/tmp/djmercury.db',
    }
}

INSTALLED_APPS = ['djmercury']
ROOT_URLCONF = ['djmercury.urls']
