from setuptools import setup, find_packages
import codecs
import os
# 
here = os.path.abspath(os.path.dirname(__file__))
# 
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()\

from pathlib import Path
this_directory = Path(__file__).parent
#long_description = (this_directory / "README.md").read_text()

VERSION = '''0.12'''
DESCRIPTION = '''One-line-web-scraping by combining pandas and BeautifulSoup4'''

# Setting up
setup(
    name="a_pandas_ex_bs4df",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_bs4df',
    author="Johannes Fischer",
    author_email="aulasparticularesdealemaosp@gmail.com",
    description=DESCRIPTION,
long_description = long_description,
long_description_content_type="text/markdown",
    #packages=['beautifulsoup4', 'lxml', 'pandas', 'regex', 'requests', 'useful_functions_easier_life'],
    keywords=['BeautifulSoup4', 'bs4', 'pandas', 'web scraping'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
    install_requires=['beautifulsoup4', 'lxml', 'pandas', 'regex', 'requests', 'useful_functions_easier_life'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*