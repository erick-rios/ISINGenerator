from setuptools import setup, find_packages

setup(
    name='ISINGenarator',
    version='0.1.0',
    author='Erick Jesús Ríos González',
    description='Ising Model 2D generator.',
    long_description=open('README.md').read(),
    packages=find_packages(where="src"),
    py_modules=[
        'isingenerator.__about__',
        'isingenerator.create_data_simulation',
        'isingenerator.__init__',
        'isingenerator.ising_model_2d',
        'isingenerator.lattice_square',
        'isingenerator.__main__',
        'isingenerator.main_simulation',
        'isingenerator.monte_carlo_simulation',
        'isingenerator.neighbors',
        'isingenerator.topological_variables',
        'isingenerator.writer_csv',
        'isingenerator.geometric_variables',
    ],
    package_dir={"": "src"},
    install_requires=[
        'numpy>=1.16.5,<1.23.0',
        'scipy',
        'networkx',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
