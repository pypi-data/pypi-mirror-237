from setuptools import setup, find_packages

setup(
    name='jacksung',
    version='0.0.2.23',
    author='Zijiang Song',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'pymysql',
        'pytz',
        'selenium',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'ecnu_login = jacksung.utils.login:main',
            'watch_gpu = jacksung.utils.nvidia:main'
        ]
    }
)
