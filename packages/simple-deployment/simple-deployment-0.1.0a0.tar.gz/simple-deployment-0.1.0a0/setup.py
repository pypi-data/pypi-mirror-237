from setuptools import setup, find_packages

# Read requirements.txt and store the dependencies in a list
with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setup(
    name='simple-deployment',
    version='v0.1.0-alpha',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    package_data={
        'chatbot': ['frontend/*'],
    },
    entry_points={
        'console_scripts': [
            'simple-deployment=chatbot.backend.app2:main',
        ],
    }
)
