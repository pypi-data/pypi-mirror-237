from setuptools import setup, find_packages
from os.path import abspath, dirname, join

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    # Name 
    name="tac_test_package",

    # Version
    version="0.1.0",

    # Packages
    packages=['tac_test_package', 'tac_test_package/models', 'tac_test_package/models/run', 'tac_test_package/models/utils'],

    # Description
    description="A python library",

    # The content that will be shown for the project page.
    long_description=README_MD,
    long_description_content_type="text/markdown",

    # The url field - Link to a git repository
    url="https://github.com/conect2ai/",

    # The author name and email 
    author="Miguel",
    author_email="miguel.amaral.111@ufrn.edu.com",

    # Classifiers
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],

    # Keywords are tags that identify your project and help searching for it
    # This field is OPTIONAL
    keywords="Annomaly Detection",

    install_requires=['numpy', 'pandas', 'matplotlib', 'seaborn', 'ipython', 'scikit-learn']
)