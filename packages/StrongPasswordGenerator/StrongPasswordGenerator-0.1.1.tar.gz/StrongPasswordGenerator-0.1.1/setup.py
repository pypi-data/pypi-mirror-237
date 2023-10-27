import sys

from setuptools import setup, find_packages

if sys.version_info < (3, 4):
  sys.exit('Python >= 3.4 is required')

setup(name='StrongPasswordGenerator',
      version='0.1.1',
      description='Generates a strong password',
      long_description=open("README.md").read(),
      url='http://github.com/ogelami/StrongPasswordGenerator',
      author='ogelami',
      author_email='ogelami@gmail.com',
      scripts=['bin/strongPasswordGenerator'],
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
