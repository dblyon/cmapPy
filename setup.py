# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='cmapPy',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='3.3.3',

    description='Assorted tools for interacting with .gct, .gctx files and other Connectivity Map (Broad Institute) data/tools',
    long_description="cmapPy: Tools for interacting with .gctx and .gct files, and other Connectivity Map resources. See our documentation at http://cmappy.readthedocs.io/en/latest/, and for more information on the file formats and available resources, please see clue.io/gctx.",

    # The project's main homepage.
    url='https://github.com/cmap/cmapPy',

    # Author details
    maintainer='Oana Enache',
    maintainer_email='oana@broadinstitute.org',

    # Choose your license
    license='BSD 3-clause',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3'
    ],

    # What does your project relate to?
    keywords='gct gctx file-manipulation Connectivity Map CMap Broad Institute',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib','docs','tutorials', 'tests', 'performance_testing']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy>=1.11.2', 'pandas>=0.18', 'h5py>=2.6.0', 'requests>=2.13.0', 'six'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={},
    include_package_data=True, # reads these from MANIFEST.in

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={'console_scripts': ['gctx2gct=cmapPy.pandasGEXpress.gctx2gct:main', 'gct2gctx=cmapPy.pandasGEXpress.gct2gctx:main', 
        'concat=cmapPy.pandasGEXpress.concat:main', 'subset=cmapPy.pandasGEXpress.subset:main']},

    tests_require=['unittest']
)
