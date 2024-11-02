# setup.py
from setuptools import setup, find_packages

setup(
    name="davmscraper",              
    version="0.1.0",                
    author="Davletvm",
    author_email="davletvm@gmail.com",
    description="Job Scrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/davletvm8787/davmsscarpper",  
    packages=find_packages(),         
    classifiers=[                    
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',          
    install_requires=[              
        # 'example_package>=1.0',     
    ],
)