from setuptools import setup, find_packages

setup(
    name="fair-mobil",
    version="1.1.5",
    description="My package description",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.6.0",
        "pandas>=1.2.0",
        "geopandas>=0.9.0",
        "plotly>=5.0.0",
    ],
)