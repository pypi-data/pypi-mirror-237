import os

import unittest
import time
from unittest.mock import Mock, patch

from cooler_data_processor import CoolerDataProcessor

class TestCoolerDataProcessor(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary input file with test data
        self.input_file = "test_input.csv"
        with open(self.input_file, "w") as f:
            f.write("Time,Pressure\n")
            f.write("1,4.1233454\n")
            f.write("2,9.54324234\n")
            f.write("3,25.09038\n")
            f.write("4,18.52345\n")
            f.write("5,26.713243\n")            
        
        # Create an instance of CoolerDataProcessor
        self.output_file = "test_output.csv"
        self.processor = CoolerDataProcessor(self.input_file, self.output_file)

    
    def test_exception_handling_missing_input_file(self):
        """
        Test that an exception is raised when trying to create an instance with a non-existent input file.
        """
        with self.assertRaises(FileNotFoundError):
            CoolerDataProcessor("dummy_file.csv", self.output_file)
            
    def test_psi_to_fahrenheit_mock(self):
        """
        Test the psi_to_fahrenheit method with a mocked PropsSI function.
        """
        # Mocking the PropsSI function from CoolProp
        with patch('cooler_data_processor.PropsSI', return_value=273.15) as mock_props:
            result = self.processor.psi_to_fahrenheit(0)
        # Assert that PropsSI was called with the expected parameters
        mock_props.assert_called_with("T", "P", 101352.93220972111, "Q", 1, "Ammonia")
        self.assertEqual(result, 32)  # Expected temperature in Fahrenheit
            
    
    def test_psi_to_fahrenheit(self):
        """
        Test the psi_to_fahrenheit method with various pressure values.
        """
        self.assertAlmostEqual(self.processor.psi_to_fahrenheit(0), -27.958,places=2)
        self.assertAlmostEqual(self.processor.psi_to_fahrenheit(10.125), -8.194, places=2)
        self.assertAlmostEqual(self.processor.psi_to_fahrenheit(14.845), -1.161, places=2)        
        self.assertAlmostEqual(self.processor.psi_to_fahrenheit(42.783), 28.192, places=2)
        self.assertAlmostEqual(self.processor.psi_to_fahrenheit(67.839), 46.006, places=2)
        self.assertAlmostEqual(self.processor.psi_to_fahrenheit(99.172), 63.116, places=2)
    

    def test_process_data(self):
        """
        Test the process_data method by processing test data and checking the processed data.
        """
        data = self.processor.process_data()
        self.assertEqual(len(data), 5)
        self.assertListEqual(data[0], ['1', -18.883857481665856, None, None])
        self.assertListEqual(data[1], ['2', -9.133144414735469, True, False])
        self.assertListEqual(data[2], ['3', 11.461663445674809, True, False])
        self.assertListEqual(data[3], ['4', 3.72110762101919, False, True])
        self.assertListEqual(data[4], ['5', 13.217065935949893, True, False])


    def test_performance_large_input(self):
        """
        Test the performance of processing a large input file.
        """
        # Generate a large input file with a significant amount of data
        num_data_points = 100000  # Adjust the number of data points as needed
        input_data = "Time,Pressure\n" + "\n".join([f"{i},{i*0.01}" for i in range(1, num_data_points + 1)])
        with open("test_input.csv", "w") as f:
            f.write(input_data)
        # Measure the time it takes to process the data
        start_time = time.time()
        self.processor.process_data()
        end_time = time.time()

        # Verify that the processing time is reasonable (adjust threshold as needed)
        max_processing_time = 10  # Maximum allowed processing time in seconds
        processing_time = end_time - start_time
        self.assertLess(processing_time, max_processing_time)


    
if __name__ == '__main__':
    unittest.main()
