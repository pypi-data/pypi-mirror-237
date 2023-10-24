from setuptools import setup, find_packages
long_description=""""
### Cooler Data Processor

The Cooler Data Processor is a Python tool for processing temperature and pressure data from a CSV file and analyzing it. This tool can convert pressure values to temperature in Fahrenheit, identify temperature ranges, and determine cooling conditions.

## Features

- **Data Processing**: Read input data from a CSV file and process it.
- **Conversion**: Convert pressure (PSI) to temperature (Fahrenheit).
- **Cooling and inrange Detection**: Detect cooling and inrange conditions based on temperature trends. This part of the code is logically replicated as it is from the source code provided in process_script.py
- **Table Output**: Display processed data in tabular format.
- **Performance**: Can handle large datasets efficiently.

## Installation

To install the Cooler Data Processor, you can use `pip`:
```bash
pip install cooler-data-processor
```


## Usage

To process your data, you can run the following command:
```bash
cd cooler_data_processor
python3 cooler_data_processor.py input1.csv output.csv
```


## Testing

You can run tests for the Cooler Data Processor using unittest. The tests include testing the data processing, temperature conversion, and performance with a large dataset.

To run the tests, use the following command:
```bash
python3 -m unittest test_cooler_data_processor.py
```

"""

setup(
    name="cooler-data-processor",
    version="0.2.1",
    description="A Cooler Data Processor",
    author="Charmi Patel",
    packages=find_packages(),
    install_requires=[
        "argparse",
        "CoolProp",
        "tabulate",
        
    ],
    tests_require=[
        "unittest",  
        "time",
        "unittest.mock",
    ],
)

