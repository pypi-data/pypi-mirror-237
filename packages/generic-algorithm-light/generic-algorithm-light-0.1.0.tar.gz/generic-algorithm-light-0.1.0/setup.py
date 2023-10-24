from setuptools import find_packages, setup

setup(
    name="generic-algorithm-light",
    version="0.1.0",
    description="A lightweight genetic algorithm package for optimization",
    author="Fernando Zepeda",
    author_email="fernando.zepeda@pm.me",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    entry_points={
        "console_scripts": [],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
