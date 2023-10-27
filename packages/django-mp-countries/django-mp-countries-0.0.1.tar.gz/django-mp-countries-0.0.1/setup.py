
from setuptools import setup, find_packages


version = '0.0.1'
url = 'https://github.com/pmaigutyak/mp-countries'


setup(
    name='django-mp-countries',
    version=version,
    description='Django countries app',
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
)
