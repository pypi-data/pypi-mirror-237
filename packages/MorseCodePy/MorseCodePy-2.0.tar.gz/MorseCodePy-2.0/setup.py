from setuptools import setup

with open('README.md', 'r') as readme:
    documentation = readme.read()

setup(name='MorseCodePy',
      packages=['MorseCodePy'],
      version='2.0',
      author='CrazyFlyKite',
      author_email='karpenkoartem2846@gmail.com',
      description='Easily and correctly encode and decode text into Morse code',
      long_description=documentation,
      long_description_content_type='text/markdown'
      )
