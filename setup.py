from version import __version__
from setuptools import find_packages, setup
from setuptools import Command
import os


class VersionCommand(Command):
    description = "Printing version of the package"

    user_options = []

    def initialize_options(self):
        """Override default one if needed"""
    def finalize_options(self):
        """Override default one if needed"""
    def run(self):
        print(__version__)

setup(
    name='hello_world',
    version=__version__,
    description="A simple hello world Flask app",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,

    cmdclass={'version': VersionCommand},

    setup_requires=['pytest-runner'],
    tests_require=[
        "pytest<=7.4.4",
        "requests",
        "urllib3==1.26.19",
        "exceptiongroup<=1.1.3",
        "typing-extensions<=4.5.0"
    ],
    install_requires=[
        "Click==8.1.7",
        "Flask==3.0.3",
        "Jinja2==3.1.6",
        "MarkupSafe==2.1.5",
        "Werkzeug==3.1.5",
        "markdown==3.7",
        "blinker==1.6.2",
        "pluggy==1.3"
    ],
)
