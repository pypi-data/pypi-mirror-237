from setuptools import setup, find_packages 

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='fuzzystk',
    version='0.1.0',
    license='MIT License',
    author='Henrique de Lemos Braga',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='henriquelemosbraga@gmail.com',
    keywords='fuzzystk',
    description=u'Biblioteca fuzzystk',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib'],)