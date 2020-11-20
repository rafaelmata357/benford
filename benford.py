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

import pandas as import pd
import numpy as np
import matplotlib.pyplot as plt 

class Benford:
    
    def __init__(self, dataset=None, normalized=True):
        """
        Function to initialize the class

        Parameters:
        -------------------------
        dataset: A dataset containing numbers, a numpy array  or a list
        """
        self.dataset = dataset
        self.normalized = normalized
        self.digits = np.array(range(1,10))      
        self.digits_count = np.zeros(9) 
        
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

