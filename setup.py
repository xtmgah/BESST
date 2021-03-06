
import os
from setuptools import setup, find_packages

setup(
    name='BESST',
    version='1.0.4.4',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
      ],
    scripts=['runBESST', 'docs/INSTALL.txt', 'docs/MANUAL.txt', 'scripts/reads_to_ctg_map.py'],
    description='Scaffolder for genomic assemblies.',
    author='Kristoffer Sahlin',
    author_email='kristoffer.sahlin@scilifelab.se',
    url='https://github.com/ksahlin/BESST',
    license='GPLv3',
    long_description=open(os.path.join(os.getcwdu(), 'README.md')).read(),
    install_requires=['pysam==0.7',
                      'networkx>=1.4',
                      'mathstats',
                      'scipy>=0.9'],
)
