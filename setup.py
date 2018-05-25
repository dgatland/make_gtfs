from setuptools import setup, find_packages


# Import ``__version__`` variable
exec(open('make_gtfs/_version.py').read())

with open('README.rst') as f:
    readme = f.read()

setup(
    name='make_gtfs',
    version=__version__,
    author='Alex Raichev',
    url='https://github.com/mrcagney/make_gtfs',
    description='A Python 3.5+ library to make GTFS feeds from simpler files',
    long_description=readme,
    license='MIT',
    install_requires=[
        'gtfstk >= 9.1.0',
        # Avoid isinstance bug in Pandas 0.23.0 with Python 3.5.2
        'pandas < 0.23.0',
        'Shapely >= 1.6.4',
        'utm >= 0.4.2',
        'click >= 6.7',
    ],
    entry_points={
        'console_scripts': ['make_gtfs=make_gtfs.cli:make_gtfs'],
    },
    packages=find_packages(exclude=('tests', 'docs'))
)
