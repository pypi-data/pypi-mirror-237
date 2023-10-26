from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'To update and retrieve documentation data'
LONG_DESCRIPTION = 'A package that allows to update and retrieve documentation data.'

# Setting up
setup(
    name="doc-controller",
    version=VERSION,
    author="Bernard Birendra Das",
    author_email="<bernardbdas@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['rasa'],
    keywords=['python', 'conversational AI', 'AI', 'Task Automation', 'SimplifyQA', 'Simplify3x'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)