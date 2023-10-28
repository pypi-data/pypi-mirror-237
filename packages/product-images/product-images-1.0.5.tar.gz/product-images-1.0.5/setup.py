
from setuptools import setup, find_packages


version = '1.0.5'
url = 'https://github.com/pmaigutyak/product-images'


setup(
    name='product-images',
    version=version,
    description='Django run app',
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='%s/archive/%s.tar.gz' % (url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT'
)
