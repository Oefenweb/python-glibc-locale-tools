# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
  with open('README.md') as f:
    return f.read()


setup(name='glibc-locale-tools',
      version='0.0.1',
      author='Mischa ter Smitten',
      author_email='mtersmitten@oefenweb.nl',
      maintainer='Mischa ter Smitten',
      maintainer_email='mtersmitten@oefenweb.nl',
      url='http://www.oefenweb.nl/',
      download_url='https://github.com/Oefenweb/glibc-locale-tools',
      license='MIT',
      description='Tools to work with (glibc) locale files (e.g. LC_MONETARY, LC_NUMERIC, LC_TIME)',
      long_description=readme(),
      py_modules=['glibc_locale_tools'],
      scripts=['bin/glibc-locale-tools'],
      platforms=['GNU/Linux'])
