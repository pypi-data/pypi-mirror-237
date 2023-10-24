import argparse
from CoolProp.CoolProp import PropsSI
from tabulate import tabulate
import math
import os


class CoolerDataProcessor:
    def __init__(self, input_file, output_file):
        """
        Constructor for initializing the CoolerDataProcessor object.

        Parameters:
        - input_file (str): Path to the input file containing temperature and pressure data.
        - output_file (str): Path to the output file to store processed data.
        """        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        self.input_file = input_file
        self.output_file = output_file
        self.data = []
        self.out = []
        self.prev_temp = None

    def psi_to_fahrenheit(self, psi):
        """
        Convert pressure in psi to temperature in Fahrenheit.

        Parameters:
        - psi (float): Pressure in psi.

        Returns:
        - temp_fahrenheit (float): Temperature in Fahrenheit.
        """        
        psi = max(-13.7, psi)
        psi_pa = (psi + 14.7) / 0.000145037737730
        temp_kelvin = PropsSI("T", "P", psi_pa, "Q", 1, "Ammonia")
        temp_fahrenheit = 9 / 5 * (temp_kelvin - 273.15) + 32
        return temp_fahrenheit

            
    def write_row(self, row):
        """
        Write processed data to the output file.

        Parameters:
        - row (list): A list of data rows to write to the output file.
        """
        with open(self.output_file, 'w') as f1:
            f1.write("t,tmp,inrange,cooling\n")
            for r in row:
                f1.write(f"{r[0]},{r[1]},{r[3]},{r[2]}\n")


    def process_data(self): 
        """
        Process the input data and store the results in the 'out' attribute.

        Returns:
        - out (list): Processed data stored as a list of lists.
        """
        with open(self.input_file, "r") as f:
            next(f)  # Skip the header
            lines = f.readlines()
        
        for line in lines:
            timestamp, psi = line.strip().split(',')
            psi = float(psi)    
            tf = self.psi_to_fahrenheit(psi)  
            
            if self.prev_temp is not None:
                if tf < self.prev_temp:
                    in_range = 10 <= tf < 20
                    cooling = True
                else:
                    in_range = tf <= 20 or tf > 40
                    cooling = False
            else:
                in_range = None
                cooling = None

            self.out.append([timestamp, tf, in_range, cooling])
            self.prev_temp = tf
        self.write_row(self.out)
        return self.out

    
    def print_table(self,section_title, headers, data):
        """
        Print a table with the provided data.

        Parameters:
        - section_title (str): Title for the printed table.
        - headers (list): List of table headers.
        - data (list): Data to be displayed in the table.
        """
        table = tabulate(data, headers, tablefmt="fancy_grid")
        print(f"-{section_title}-")
        print(table)
        print()
    
    def print_results(self):
        """
        Print the results, including tables for nice cooler temp times, low temperatures, and the average temperature.
        """
        print("---Results---")    
        # Extract data
        nice_cooler_times = [(data_point[0], data_point[1]) for data_point in self.out if not data_point[2] and data_point[3]]
        low_temps = [(data_point[0], data_point[1]) for data_point in self.out if data_point[1] < 0]
    
        # Print tables
        self.print_table("Nice Cooler Temp Times", ["Time", "Temperature"], nice_cooler_times)
        self.print_table("Low Temperature", ["Time", "Temperature"], low_temps)
    
        # Calculate and print Average Temperature
        temperatures = [data_point[1] for data_point in self.out]
        avg_temp = sum(temperatures) / len(self.out)
        self.print_table("Average Temperature", ["Value"], [(f"{avg_temp:.2f}",)])


def main():
    """
    The main function for the Cooler Data Processor command-line tool.
    It parses command-line arguments, processes the input data, and prints the results.
    """
    parser = argparse.ArgumentParser(description="Cooler Data Processor")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output CSV file")

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    temp_processor = CoolerDataProcessor(input_file, output_file)
    out = temp_processor.process_data()
    temp_processor.print_results()

if __name__ == "__main__":
    main()
