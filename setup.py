#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

long_description = open('README').read().strip()


setup(name='spc',
      version='0.3',
      description='Statistical Process Control library for monitoring process behaviour',
      long_description=long_description,
      author='Michal Nowikowski',
      author_email='godfryd@gmail.com',
      url='http://pww.pw.pl/',
      packages=['spc'],
      license="MIT",
      platforms=["Any"],
      install_requires=['NumPy'],
      #include_package_data=True,
      package_data={"docs": "*"},
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Quality Assurance'
        ]
     )
