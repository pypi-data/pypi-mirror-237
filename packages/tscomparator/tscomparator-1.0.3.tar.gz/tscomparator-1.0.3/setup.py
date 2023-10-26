from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'tscomparator',
  packages = find_packages(),
  version = '1.0.3',
  license='',
  description = 'A timeseries comparison and analysis tool for Python',
  author = 'Grant Ellison',
  author_email = 'gellison321@gmail.com',
  url = 'https://github.com/gellison321/tscomparator',
  download_url = 'https://github.com/gellison321/tscomparator/archive/refs/tags/1.0.3.tar.gz',
  keywords = ['timeseries', 'data science','data analysis', 'time series comparison'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
  ],
  install_requires=['numpy', 'scipy'],
)