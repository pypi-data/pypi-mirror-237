from setuptools import setup, find_packages

setup(
    name='study_buddy',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "pytesseract~=0.3.10",
        "pdf2image~=1.16.3",
        "Pillow~=10.1.0",
        "setuptools~=68.2.0"
    ],
    author='Michael S.',
    author_email='pypi.6b0s8@simplelogin.com',
    description='A simple package for parsing PDFs to text for Linux and Mac OS',
    license='MIT',
)
