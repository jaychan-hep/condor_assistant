from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='condor_assistant',
   version='1.0',
   description='Handy tool for condor submission',
   license="MIT",
   long_description=long_description,
   author='Jay Chan',
   author_email='jay.chan@cern.ch',
   url="http://www.foopackage.example/",
   packages=['condor_assistant'],
   install_requires=[],
   scripts=[]
)
