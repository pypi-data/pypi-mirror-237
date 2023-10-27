from setuptools import find_packages, setup

with open("README.md","r") as fh:
    description_l=fh.read()

setup(
    name="alexislib",
    version='0.1.2',
    packages=find_packages(include=["alexislib"]),
    description="libreria de suma",
    long_description=description_l,
    long_description_content_type="text/markdown",
    author="ALexis",
    license="MIT",
    install_requires=["numpy==1.26.1","pandas"],
    python_requires=">=3.11.3",
    author_email="anderson.ruales@udea.edu.co",
    url="https://gitlab.com/udea3/cursofci-2023-2.git"


)