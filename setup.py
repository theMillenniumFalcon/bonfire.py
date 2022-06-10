from distutils.core import setup
from os import path
from bonfire import __version__

this_dir = path.abspath(path.dirname(__file__))

with open(path.join(this_dir, "README.rst"), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bonfire',
    packages=['bonfire', 'bonfire.utils', 'bonfire.events'],
    version=__version__,
    description='A Python wrapper for the bonfire API.',
    project_urls={
        "Documentation": "non extistant right now",
    },
    long_description=long_description,
    author='theMillenniumFalcon',
    author_email='nishankpr435@gmail.com',
    url='https://github.com/theMillenniumFalcon/bonfire.py',
    download_url=f'https://github.com/theMillenniumFalcon/bonfire.py/archive/{__version__}.tar.gz',
    keywords=["dogehouse"],
    install_requires=[],
    classifiers=[
        # Development statuses:
        'Development Status :: 1 - Planning',
        # Development Status :: 2 - Pre-Alpha
        # Development Status :: 3 - Alpha
        # Development Status :: 4 - Beta
        # Development Status :: 5 - Production/Stable
        # Development Status :: 6 - Mature
        # Development Status :: 7 - Inactive
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)