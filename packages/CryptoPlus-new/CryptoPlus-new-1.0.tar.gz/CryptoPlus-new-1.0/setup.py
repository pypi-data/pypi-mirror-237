#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='CryptoPlus-new',
      version='1.0',
      description='PyCrypto Cipher extension',
      author='Christophe Oosterlynck',
      author_email='str2hex@mail.ru',
      packages = find_packages('src'),
      install_requires = ['pycryptodome'],
      package_dir={'': 'src'}
     )

