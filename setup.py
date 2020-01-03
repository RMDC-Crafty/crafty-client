from setuptools import setup

setup(
     name='crafty-client',
     version='0.99A',
     description='A python library for talking to Crafty Web minecraft server control panel',
     author='kevdagoat',
     url='https://gitlab.com/crafty-controller/crafty-client',
     install_requires=[
          'requests',
          'urllib3',
      ],
     packages=['crafty-web-client']
)