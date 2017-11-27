from setuptools import setup

setup(
    name='tellme',
    version='0.1',
    py_modules=['tellme'],
    install_requires=['Click',],
    entry_points={
        'console_scripts': [
            'tellme = tellme:cli',
        ]
    }
)
