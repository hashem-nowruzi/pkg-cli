from setuptools import setup
from pathlib import Path

HERE = Path(__file__).parent

setup(name='pkg-cli',
      version='0.0.0',
      packages=['pkg'],
      description='Create Packages and Publish them to PyPi',
      keywords=['pypi', 'package', 'pkg-cli', 'pkg'],
      license='MIT',
      author='Hashem',
      long_description=(HERE / 'README.md').read_text(),
      long_description_content_type='text/markdown',
      author_email='PersonalHashem@gmail.com',
      url='https://github.com/githashem/pkg-cli',
      python_requires='>=3.7',
      )
