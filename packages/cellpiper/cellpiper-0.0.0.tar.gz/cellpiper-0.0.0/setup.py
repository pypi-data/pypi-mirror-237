import sys
import os
import time
import setuptools
import subprocess
from platform import system

try:
    from collections import Mapping
except ImportError:
    # This is a problem when building on python3.10
    import collections.abc
    # Add attributes to `collections` module before importing the package
    collections.Mapping = collections.abc.Mapping


# You can't use `pip install .` as pip copies setup.py to a temporary
# directory, parent directory is no longer reachable (isolated build) .
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, CURRENT_DIR)

if __name__ == '__main__':

    # Uploading new release:
    # - Check upload artifacts when running action, run actions
    # - Downlad artifact wheels on your local machine
    # - Create empty folder and put all *.whl files in the same folder
    # - From that folder call:
    #     twine upload ./*

    # Building from terminal (from python-package folder)
    #   python setup.py sdist
    #   twine upload dist/*

    # Supported commands:
    # From internet:
    #   pip install cellpiper
    # Locally for testing (from cellpiper/python-packate dir)
    #   pip install -e . --force-reinstall -v
    # Upload to test.pypi
    #   twine upload --repository testpypi dist/*
    # Istall from test.pypi
    #   pip install --force-reinstall -i https://test.pypi.org/simple/ cellpiper

    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="cellpiper",
        version="0.0.0",
        author="Ginko Balboa",
        author_email="ginkobalboa3@gmail.com",
        description="Orchestrate ML processing using pipes",
        packages=setuptools.find_packages(include=['cellpiper']),
        include_package_data=True,
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://www.cellpiper.com",
        project_urls={"github": "https://github.com/GinkoBalboa/cellpiper",
                      "documentation": "https://www.cellpiper.com"},
        classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: C++",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: Microsoft :: Windows :: Windows 10",
            "Operating System :: POSIX :: Linux",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Visualization",
            "Topic :: Software Development :: Code Generators",
        ],
        python_requires='>=3.7',
        zip_safe=False,
    )
