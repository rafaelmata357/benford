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
        dataset: A dataset containing numbers, can be a pandas dataset, an numpy array, a list
        """
        self.dataset = dataset
        pass

    def load_dataset(self, dir, type='csv'):
        """ Function to read a dataset using pandas"""
        pass
