from setuptools import find_packages
from setuptools import setup
import os


version = '0.2.dev0'


def read(*rnames):
    """Read file content."""
    with open(os.path.join(os.path.dirname(__file__), *rnames))as f:
        return f.read()


long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'smoke', 'test_smoke.rst')
    + '\n' +
    read('CHANGES.rst'))


setup(
    name='js.smoke',
    version=version,
    description="fanstatic smoke.js.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'smoke = js.smoke:library',
        ],
    },
)
