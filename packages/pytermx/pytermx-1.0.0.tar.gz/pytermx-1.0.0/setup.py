from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytermx',
    version='1.0.0',
    description='A python terminal decors package',
    author='Sekateur',
    author_email='akamecanic+seka@email.com',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT'
)