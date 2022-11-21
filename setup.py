from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in setting/__init__.py
from setting import __version__ as version

setup(
	name="setting",
	version=version,
	description="setting",
	author="setting",
	author_email="setting@123",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
