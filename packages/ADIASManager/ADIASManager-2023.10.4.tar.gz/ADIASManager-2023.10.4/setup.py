from setuptools import setup, find_packages

VERSION = '2023.10.4'
DESCRIPTION = 'Tools for simplifying processes on ADIAS'
LONG_DESCRIPTION = 'Tools for launching remote clusters and managing S3 storage on ADIAS'

# Setting up
setup(
    # the name must match the folder name
    name="ADIASManager", 
    version=VERSION,
    author="Lachlan Phillips",
    author_email="lachlan.phillips@csiro.au",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[], # 'dask', 'dask-gateway', 'dask-cuda', 's3fs'
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'ADIAS', 'clusters'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)