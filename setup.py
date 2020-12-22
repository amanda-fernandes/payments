from setuptools import find_packages, setup


# list comprehension:
# open file line by line and remove /n
def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="payments",
    version="0.1.0",
    description="Payments API",
    packages=find_packages(exclude=["./env"]),
    include_package_data=True,
    install_requires=read("requirements-dev.txt"),
)
