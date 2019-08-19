import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
    
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='myblog',
    version='0.1',
    packages=['blog'],
    include_package_data=True,
    license='BSD license',
    description='Simple Blog',
    long_description=README,
    url='https://www.example.com/',
    author='Theaska',
    author_email='tach.pu@gmail.com',
    classifiers=[
        'Enviroment :: Web Enviroment',
        'Framework :: Django',
        'Intendeed Audience :: Developers',
        'Licence :: OSI Approved :: BSD Licence',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python 3.6',
        'Programming Language :: Python 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )