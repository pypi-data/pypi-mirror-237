from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name_iurywmp",
    version="0.0.1",
    author="iurywmp",
    author_email="iuryprobo@gmail.com",
    description="This is a test file for DIO bootcamp",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iurywmp/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)