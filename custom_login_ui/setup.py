from setuptools import setup, find_packages

setup(
    name='custom_login_ui',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'frappe',  # Add any other dependencies you need here
    ],
)
