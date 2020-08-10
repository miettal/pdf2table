from setuptools import find_packages
from setuptools import setup


setup(
    name='pdf2table',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-WTF',
        'Flask-Caching',
        'tabula-py',
    ],
)
