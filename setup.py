"""setup.py: From github.com/pypa/sampleproject"""
from setuptools import setup, find_packages


with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='zhatil',
    version='0.0.1',
    description='A chat bot framework.',
    long_description=long_description,
    url='https://zhatil.readthedocs.io',
    author='Mike Canoy',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'zhatil=zhatil:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/solus-impar/zhatil/issues',
        'Source': 'https://github.com/solus-impar/zhatil',
    }
)
