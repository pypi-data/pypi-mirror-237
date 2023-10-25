from setuptools import setup, find_packages

setup(
    name='agentive',
    version='0.0.11',
    description='Python-based framework for building modular and extensible conversational agents',
    author='Morningside AI',
    install_requires=[
        'requests',
        'pandas',
        'tenacity',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
)