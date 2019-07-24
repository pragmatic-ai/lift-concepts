from distutils.core import setup
from setuptools import find_packages
setup(
    name='pragma_universe',
    packages=find_packages(),
    version='0.0.1',
    description='Pragma Universe',
    author='Ramtin Seraj',
    author_email='mehdizadeh.ramtin@gmail.com',
    url='https://github.com/pragmatic-ai/pragma-universe',
    download_url='https://github.com/pragmatic-ai/pragma-universe/tarball/0.1',
    keywords=['natural language processing', 'nlp', 'Artificial intelligence', 'ontology'],
    classifiers=['Intended Audience :: Information Technology',
                 'Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                 'Topic :: Scientific/Engineering :: Information Analysis',
                 'Topic :: Text Processing',
                 'Topic :: Text Processing :: Filters',
                 'Topic :: Text Processing :: General',
                 'Topic :: Text Processing :: Indexing',
                 'Topic :: Text Processing :: Linguistic',
                 ],
    install_requires=[
    ],
)