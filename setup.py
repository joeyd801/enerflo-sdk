from setuptools import find_packages, setup

setup(
    name='enerflo_sdk',
    packages=find_packages(),
    description='An SDK for the Enerflo API',
    version='1.0',
    author='Garrett Franklin',
    author_email='garrett@stackintegrated.com',
    install_requires=['requests']
)
