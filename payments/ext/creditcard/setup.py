"""The setuptools setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

# Define your dependencies here
requirements = []
setup_requirements = []

setup(
    author="MaisTodos",
    author_email="devs@maistodos.com.br",
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Portuguese",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A simple credit cards validation library in Python",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="creditcard",
    name="python-creditcard",
    packages=find_packages(include=["creditcard", "creditcard.*"]),
    setup_requires=setup_requirements,
    url="https://github.com/MaisTodos/python-creditcard",
    version="0.0.1",
    zip_safe=False,
)
