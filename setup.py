from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-ressources',
    version='0.0.4',
    author='Samuel Goldszmidt',
    author_email='samuel.goldszmidt@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://forge.ircam.fr/p/django-ressources/',
    license='LICENSE.txt',
    description='Django base templates for all ressources.ircam.fr website.',
    long_description=open('README.txt').read(),
    install_requires=[
        "django-compressor==2.1",
    ],
    zip_safe=False,
)
