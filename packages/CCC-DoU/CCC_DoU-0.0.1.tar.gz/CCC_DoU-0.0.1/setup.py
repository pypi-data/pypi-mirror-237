from setuptools import setup
import setuptools

with open("README1.md", "r") as fh:
    long_description = fh.read()

setup(
    name='CCC_DoU',
    version='0.0.1',
    description='Chatterjee Correlation coefficient calculator with p-value',
    author= 'Shubhabrata Dokal',
    url = 'https://github.com/Partha0312bio/CCC_DU',
    long_description= long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['Chatterjee Correlation Coefficient', 'non linear correlation calculation ', ''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['CCC_DoU'],
    package_dir={'':'src'},
    install_requires = [
        'numpy',
        'pandas'
    ]
)
