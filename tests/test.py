# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:    Rafael Mata M.
# DATE CREATED:  24 Nov 2020                                
# REVISED DATE:  24 Nov 2020
# PURPOSE: A Class to test the Benford Class
#  
# Any changes to the Benford class library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest
import numpy as np
from benford import Benford


class TestBenfordClass(unittest.TestCase):
    def setUp(self):
        self.benford = Benford()
        

    def test_initialization(self): 
        self.assertEqual(self.benford.digits, np.array([1,2,3,4,5,6,7,8,9]), 'Incorrect digits array initialization')
        self.assertEqual(self.benford.dataset, None, 'Incorrect dataset initialization')

    def test_load_dataset(self):
        self.benford.load_dataset('population.csv')                                      # Load a dataset to test, base on world population
        data_sum = self.benford.dataset.sum()
        self.assertEqual(data_sum, 7794798739, 'data not read correctly')                # Summarize the values and check the result

    def test_digits_probabiliy(self):
        self.benford.benford_analysis()                                                   # Perform the Benford´s Law analysis
        digits_probability = np.round(self.benford.digits_count,decimals=2)
        self.assertEqual(digits_probability[0], 29.79, 'Digit 1 probability not calculated as expected')
        self.assertEqual(digits_probability[1], 15.74, 'Digit 2 probability not calculated as expected')
        self.assertEqual(digits_probability[2], 12.77, 'Digit 3 probability not calculated as expected')
        self.assertEqual(digits_probability[3], 8.94,  'Digit 4 probability not calculated as expected')
        self.assertEqual(digits_probability[4], 11.06, 'Digit 5 probability not calculated as expected')
        self.assertEqual(digits_probability[5], 7.66,  'Digit 6 probability not calculated as expected')
        self.assertEqual(digits_probability[6], 3.4,   'Digit 7 probability not calculated as expected')
        self.assertEqual(digits_probability[7], 5.96,  'Digit 8 probability not calculated as expected')
        self.assertEqual(digits_probability[8], 4.68,  'Digit 9 probability not calculated as expected')

    def test_load_image(self):

        image = self.Benford()
        image.load_image('./flower.jpg')                                                   # Load an image and calculate the digits probability using Benford´s Law
        image.benford_analysis()
        self.assertEqual(image.digits_count.sum() ,100,  'The total digits probability is incorrect')
 
        

    
if __name__ == '__main__':
    unittest.main()