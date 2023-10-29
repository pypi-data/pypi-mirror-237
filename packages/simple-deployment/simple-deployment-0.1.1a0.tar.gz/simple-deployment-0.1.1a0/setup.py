from setuptools import setup, find_packages

# Read README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='simple-deployment',
    version='0.1.1-alpha',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        'backend': ['../frontend/*'],  
    },
    entry_points={
        'console_scripts': [
            'simple-deployment=backend.app2:main', 
        ],
    }
)
