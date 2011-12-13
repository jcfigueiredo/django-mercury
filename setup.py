from setuptools import setup, find_packages

setup(
    name = "django-mercury",
    version = "0.1",
    url = 'http://github.com/jacobian/django-shorturls',
    license = 'MIT',
    description = "Django support to Mercury Editor",
    author = 'Claudio Figueiredo <jcfigueiredo@gmail.com>',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
