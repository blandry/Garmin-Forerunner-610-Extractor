#!/usr/bin/env python

from distutils.core import setup

setup(name='Garmin Extractor',
      version='1.0',
      description='Extracts FIT files from ANT-FS based sport watches such as Garmin Forerunner 60, 405CX, 310XT, 610 and 910XT.',
      author='Gustav Tiger',
      url='https://github.com/Tigge/Garmin-Forerunner-610-Extractor',
      install_requires=['pyusb==1.0.0a3'],
      packages=['garmin'],
     )
