from setuptools import setup

setup(
    name='pfpcap',
    version='0.1',
    scripts=['pfpcap.py'],
    py_modules=['pfpcap'],
    install_requires=['mechanize>=0.2.5']
)
