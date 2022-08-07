from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='condor_assistant',
   version='1.3',
   description='Handy tool for condor submission',
   license="MIT",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Jay Chan',
   author_email='jay.chan@cern.ch',
   url="https://github.com/qwerasd903/condor_assistant",
   packages=['condor_assistant'],
   install_requires=[],
   scripts=["example.py"]
)
