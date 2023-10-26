from setuptools import setup, find_packages

setup(
    name="scrapethat",
    version="1.0.2",
    author="Mihaly Orsos",
    author_email="ormraat.pte@gmail.com",
    description="Tools for faster scraping",
    url="https://github.com/misrori/scrapethat",
    license="MIT",
    install_requires=["bs4", "requests", "pandas", "cloudscraper"],
    packages=find_packages()
)

