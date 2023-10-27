from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    description_l= fh.read()

setup(
    name='libreriaNueva',
    version='0.1.0',
    packages=find_packages(include= ['librerianueva']),
    description='libreria de suma',
    long_description=description_l,
    long_description_content_type='text/markdown',
    author='Ana Maria',
    license='MIT',
    install_requires=['numpy==1.26.1', 'pandas==2.1.1'],
    python_requires='>=3.9.12',
    author_email='aarcila01@gmail.com',
    git= 'https://gitlab.com/ana.arcila1/cursofci-2023-2.git'

)