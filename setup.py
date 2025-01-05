# setup.py

from setuptools import setup, find_packages

setup(
    name='text_normalizer',
    version='0.2',
    description='A Python module for normalizing text at character and word levels.',
    author='Estifanos Abebaw',
    author_email='tekle.estifanos.17@gmail.com',
    packages=find_packages(),  # This automatically finds all the Python files in the module
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
