#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:    Rafael Mata M.
# DATE CREATED:  19 Nov 2020                                
# REVISED DATE:  19 Nov 2020
# PURPOSE: A package to analyze a dataset of numbers and apply the Benfords Law
#
#   Usage:
#  ush
#   
##

# Imports python modules

import pandas as import pd
import numpy as np
import matplotlib.pyplot as plt 

class Benford:
    
    def __init__(self, dataset=None):
        """
        Function to initialize the class

        Parameters:
        -------------------------
        dataset: A dataset containing numbers, a numpy array  or a list
        """
        self.dataset = dataset
        
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
        self.dataset = pd.read_csv(dir, sep=sep )

        return None

    def load_dataset(self, dir):
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
