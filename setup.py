from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Blah blah',
    long_description='Blah blahBlah blahBlah blah',
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Simon M',
    author_email='simon@miszewski.co.za'

)