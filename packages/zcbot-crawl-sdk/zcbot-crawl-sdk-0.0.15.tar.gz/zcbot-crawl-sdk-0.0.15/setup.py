from distutils.core import setup
from setuptools import find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='zcbot-crawl-sdk',
      version='0.0.15',
      description='zcbot celery sdk for zsodata',
      long_description=long_description,
      author='zsodata',
      author_email='team@zso.io',
      url='http://www.zsodata.com',
      install_requires=['pika', 'demjson', 'requests'],
      python_requires='>=3.7',
      license='BSD License',
      packages=find_packages(),
      platforms=['all'],
      include_package_data=True
      )
