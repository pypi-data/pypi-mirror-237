from setuptools import setup

with open('README.rst', 'r', encoding='utf-8') as f:
    ln = f.read()

setup(
    name="PySieveEra",
    version="0.1",
    description="Generate a list of prime numbers within a specified range",
    long_description= ln,
    long_description_content_type='text/x-rst',
    license="MIT",
    author="Md. Ismiel Hossen Abir",
    packages=["PySieveEra"],
    url="https://pypi.org/project/PySieveEra/",
    install_requires=[]
    
)