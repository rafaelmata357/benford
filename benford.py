#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:    Rafael Mata M.
# DATE CREATED:  19 Nov 2020                                
# REVISED DATE:  20 Nov 2020
# PURPOSE: A Class to analyze a dataset of numbers and apply the Benfords Law counting the frequency of the first digit
#          from 1 - 9
#
#  Usage:
#         1. Create a new object with the class Benford, with an numpy array or list, or
#         2. Load a dataset with the method: load_dataset(args) or
#         3. Load an image with the method: load_image(args)
#         4. Analyze the data with the mehtod: apply_benford(args)
#         5. Plot the results or export to a file
##

# Imports python modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

class Benford:
    
    def __init__(self, dataset=None, normalized=True):
        """
        Function to initialize the class

        Parameters:
        -------------------------
        dataset: numpy array, A dataset containing numbers
        normalized: boolean
        """
        self.dataset = dataset
        self.normalized = normalized
        self.digits = np.array(range(1,10))      
        self.digits_count = np.zeros(9) 
        self.reference = np.array([30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6])
        
        return None

    def load_dataset(self, dir, sep=','):
        """ Function to read a dataset using pandas
            Parameters:
            -------------
            dir: str, address of the dataset and name

            Returns:
            -------------
            None
        """
        
        dataset = pd.read_csv(dir, sep=sep )
        dataset = np.asarray(dataset)
        dataset = np.abs(dataset)
        dataset = dataset[dataset > 0]
        self.dataset = dataset

        return None

    def load_image(self, dir):
        """ Function to read an image using numpy
            Parameters:
            -------------
            dir: str, address of the image, a local file or a http address

            Returns:
            -------------
            None
        """
        
        image = np.array(Image.open(dir))
        image = np.abs(image)                #Convert all values to positive
        image = image[image > 0]             #Remove the values with 0 
    
        self.dataset = image

        return None

    def benford_analysis(self):
        """ Function to analyze a dataset using the Benford´s Law, counting the frequency of first digits
            Parameters:
            -------------
            dataset: a numpy array containing integers

            Returns:
            -------------
            self.digits_count: Updated with the digits frequency normalized
        """

        numbers, counts = np.unique(self.dataset, return_counts = True)      # Count the numbers in the dataset and their frequency
    
        numerical_units = np.log10(numbers).astype(int)     # Get the int part of log base 10 of the numbers to know the number of units (10s, 100s, 1000s) 
        first_digit = numbers//10**numerical_units          # Get the first digit using  numbers // 10^numerical_units
    
        
        # Summarize the first digit counts
        for digit in self.digits:
            self.digits_count[digit-1] = counts[first_digit==digit].sum()
    
   
        return None

        def plot(self, figsize=(10,6)):
            """ Function to plot the benford results
            Parameters:
            -------------
            
            figsize = tuple, size of the figure to plot
            self.digits
            self.digits_count

            Returns:
            -------------
            A bar chart display in the screen
            """

            plt.figure(figsize=figsize)
            plt.title('Benford Analysis')
            plt.xlabel('Digit')
            if self.normalize:
                plt.ylabel('%')
            else:
                plt.ylabel('Freq')

            plt.grid(True)
            plt.bar(self.digits, self.digits_count, color='g')
            if self.normalize:
                plt.bar(self.digits, self.reference)

        return None


        



