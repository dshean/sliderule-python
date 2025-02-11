import os
from setuptools import setup, find_packages

# get long_description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# get install requirements
with open('requirements.txt') as fh:
    install_requires = fh.read().splitlines()

# semantic version configuration for setuptools-scm
setup_requires = ["setuptools_scm"]
use_scm_version = {
    "relative_to": __file__,
    "local_scheme": "node-and-date",
    "tag_regex":r'^(?:[\\w-]+-)?(?P<version>[vV]?\d+\.\d+\.\d+)',
}

setup(
    name='sliderule',
    author='SlideRule Developers',
    description='Python client for interacting with sliderule server',
    long_description_content_type="text/markdown",
    url='https://github.com/ICESat2-SlideRule/sliderule-python/',
    license='Apache',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    use_scm_version=use_scm_version,
)
