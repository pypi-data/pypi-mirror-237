from setuptools import setup, find_packages

setup(
    name="goldhand",
    version="1.0.1",
    author="Mihaly",
    author_email="ormraat.pte@gmail.com",
    description="A package working with financial data",
    license="MIT",
    install_requires=['pandas_datareader', 'pandas', 'pandas_ta', 'plotly', 'scipy', 'numpy', 'requests'],
    packages=find_packages(),
)


