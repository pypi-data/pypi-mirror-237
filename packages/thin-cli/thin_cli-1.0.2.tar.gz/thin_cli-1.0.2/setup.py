from setuptools import setup, find_packages

setup(
    name='thin_cli',
    version='1.0.2',
    description='A thin command line interface framework.',
    author='Avery Cowan',
    url='https://github.com/averycowan/lite_cli',
    packages=find_packages(exclude=['example']),
    install_requires=['typing_extensions'],
)