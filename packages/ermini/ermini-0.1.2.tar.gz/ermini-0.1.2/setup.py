from setuptools import setup, find_packages
from os import path

here = path.join(path.abspath(path.dirname(__file__)), 'ermini')

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt')) as f:
    required_packages = f.read().splitlines()

setup(
    name='ermini',
    version='0.1.2',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/crusat/ermini',
    author='Aleksey Kuznetsov aka crusat',
    author_email='crusat@yandex.ru',
    license='MIT',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3.9',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=required_packages,
)
