from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

from custom_login_ui import __version__ as version

setup(
	name="Teciza Login",
	version=version,
	description="multi themes for frappe & erpnext apps",
	author="Mohammed Arham",
	author_email="nawferarham@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)