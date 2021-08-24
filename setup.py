import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    LONG_DESC = f.read()

VERSION = '0.0.4'

setup(
    name='profiles-backup',
    version=VERSION,
    license='MIT',
    description='Backup the Profiles folder of Thunderbird.',
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/profiles-backup',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': ['profiles-backup=profiles_backup.cli:main'],
    },
    install_requires=['psutil'],
    tests_require=['pytest'],
)
