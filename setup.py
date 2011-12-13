import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-mercury",
    version = "0.1",
    url = 'https://github.com/jcfigueiredo/django-mercury',
    license = 'MIT',
    long_description = read('README'),
    description = "Django support to Mercury Editor",
    
    author = 'Claudio Figueiredo',
    author_email='jcfigueiredo@gmail.com',
    
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
