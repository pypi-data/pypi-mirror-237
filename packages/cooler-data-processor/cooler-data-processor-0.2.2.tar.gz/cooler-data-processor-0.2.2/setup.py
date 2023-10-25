from setuptools import setup, find_packages
description="Cooler Data Processor",

long_description=open("README.md").read(),
long_description_content_type="text/markdown",

setup(
    name="cooler-data-processor",
    version="0.2.2",
    description="A Cooler Data Processor",
    author="Charmi Patel",
    packages=find_packages(),
    install_requires=[
        "argparse",
        "CoolProp",
        "tabulate",
        "unittest",  
        "time",
        "unittest.mock",
        
    ],
    tests_require=[
        "unittest",  
        "time",
        "unittest.mock",
    ],
)

