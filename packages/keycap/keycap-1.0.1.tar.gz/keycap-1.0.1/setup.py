from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='keycap',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'contourpy>=1.1.1',
        'cycler>=0.12.1',
        'fonttools>=4.43.1',
        'kiwisolver>=1.4.5',
        'matplotlib>=3.8.0',
        'numpy>=1.26.1',
        'packaging>=23.2',
        'Pillow>=10.1.0',
        'pyparsing>=3.1.1',
        'python-dateutil>=2.8.2',
        'six>=1.16.0'    
    ],

    long_description=long_description,
    long_description_content_type="text/markdown", 
)
