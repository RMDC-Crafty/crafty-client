from setuptools import setup

setup(
     name='crafty-client',
     version='1.0.0',
     description='A python library for talking to Crafty Web minecraft server control panel',
     author='kevdagoat',
     url='https://gitlab.com/crafty-controller/crafty-client',
     install_requires=[
          'requests',
          'urllib3',
      ],
     packages=['crafty-web-client']
)