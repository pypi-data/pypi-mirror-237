from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    readme = file.read()

setup(
    name='pygame_simple_core',
    version='0.1.4',
    license='MIT license',
    author='Vinicius Putti Morais',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='viniputtim@gmail.com',
    keywords='pygame',
    description='A Python library for building Pygame applications with reusable components and utilities.',
    packages=find_packages(),
    install_requires=['pygame']
)
