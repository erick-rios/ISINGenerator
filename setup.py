from setuptools import setup, find_packages

setup(
    name='ISINGenarator',
    version='0.1.0',
    author='Erick Jesús Ríos González',
    description='Ising Model 2D generator.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        'numpy>=1.16.5,<1.23.0',
        'scipy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
