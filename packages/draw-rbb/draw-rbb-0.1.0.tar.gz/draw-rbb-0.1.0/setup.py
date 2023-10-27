from setuptools import setup, find_packages
import os

VERSION = '0.1.0'
DESCRIPTION = 'Drawing rounded bounding box with text'
LONG_DESCRIPTION = 'Drawing rounded bounding box with text'

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

# Setting up
setup(
    name="draw-rbb",
    version=VERSION,
    author="Alex Choi",
    author_email="geol.choi@vivity.ai",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=install_requires,
    keywords=['python', 'opencv', 'rounded bounding box'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license='MIT'
)
