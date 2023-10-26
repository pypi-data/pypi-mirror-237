from pathlib import Path

from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


# Function to discover and collect .pyi files
def discover_pyi_files(root_package):
    pyi_files = []
    for package_name in find_packages(root_package):
        package_path = root_package + '/' + package_name.replace('.', '/')
        pyi_files.extend([str(p) for p in Path(package_path).rglob('*.pyi')])

    return pyi_files


setup(
    name="mep_tools",
    version="1.1.26",
    author="Khai",
    author_email="sarraj@marksmen.nl",
    license="MIT",
    packages=find_packages(),
    package_data={'': discover_pyi_files('./mep_tools/')},
    description="grpc for rep",
    long_description="hold the code for the grpc files",
    install_requires=requirements,
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)
