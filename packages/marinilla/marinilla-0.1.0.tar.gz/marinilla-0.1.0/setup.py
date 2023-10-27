from setuptools import setup, find_packages

with open("README.md","r") as fh:
    description_l = fh.read()

setup(
    name='marinilla',
    version='0.1.0',
    packages=find_packages(include=['marinilla']),
    description='Libreria de suma',
    long_description=description_l,
    long_description_content_type="text/markdown",
    author='Juan Esteban Ospina ',
    license='MIT',
    install_requires=["numpy==1.26.1","pandas==2.1.1"],
    python_requires='>=3.10.12',
    author_email = "juan.ospina25@udea.edu.co"
    
)