from setuptools import setup, find_packages

setup(
    name="scVIDR",
    version="1.0",
    description="scVIDR",
    packages=find_packages(exclude=['bin', 'figures', 'metadata', 'notebooks'])
)
