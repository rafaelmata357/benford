#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:    Rafael Mata M.
# DATE CREATED:  19 Nov 2020                                
# REVISED DATE:  09 dic 2020
# PURPOSE: A Class to analyze a dataset of numbers and apply the Benfords Law counting the frequency of the first digit
#          from 1 - 9
#
#  Usage:
#         1. Create a new object with the class Benford, with an numpy array or list, or
#         2. Load a dataset with the method: load_dataset(args) or
#         3. Load an image with the method: load_image(args)
#         4. Analyze the data with the mehtod: apply_benford(args)
#         5. Plot the results or export to a file
#         6. Export the results to a file
#

# Imports python modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

class Benford:

    ''' A Class to perform the Benford´S Law analysis for the first leading digits [1-9]
    
        Atributes:
        -----------------------
        dataset : numpy array of integers with the numbers to analyzed
        normalized : boolean, flag to indicate if the output is normalized with the total values or the digits frequency
        digits: numpy array with digits 1 to 9
        digits_count: numpy array to store the leading digits frequency
        reference: The Benford´s theorical reference for the leading digits

        Methods:
        ------------------------
        __init__ : Method to initialize the attributes
        load_daaset : Method to read a .csv file and load the dataset
        load_image: Method to load an image and load the dataset 
        benford_analysis: Mehtod to analyze the leading digits using the Benford´s Law
        plot : Method to plot the resuls in a bar chart
        export_to_csv : Method to export the results to a .csv file
        
    '''
    
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
        
        try:
            dataset = pd.read_csv(dir, sep=sep )
            dataset = np.asarray(dataset)
            self.dataset = dataset
        except:
            print('The dataset could not be read, please check the address')

        return None

    def load_image(self, path):
        """ Function to read an image using numpy
            Parameters:
            -------------
            path: str, address of the image, a local file or a http address

            Returns:
            -------------
            None
        """
        
        image = np.array(Image.open(path))
        print('Image read')
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

        
        self.dataset = np.abs(self.dataset)                       #Convert all values to positive
        self.dataset = self.dataset[self.dataset > 0]             #Remove the values with 0 
        
        numbers, counts = np.unique(self.dataset, return_counts = True)      # Count the numbers in the dataset and their frequency
    
        numerical_units = np.log10(numbers).astype(int)     # Get the int part of log base 10 of the numbers to know the number of units (10s, 100s, 1000s) 
        first_digit = numbers//10**numerical_units          # Get the first digit using  numbers // 10^numerical_units
    
        
        # Summarize the first digit counts
        for digit in self.digits:
            self.digits_count[digit-1] = counts[first_digit==digit].sum()

        if self.normalized:                                                 # If normalized, get the digits probability
            self.digits_count = self.digits_count/self.digits_count.sum()*100
    
   
        return None

    def plot(self, figsize=(12, 6)):
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

        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
        
        ax.set_title('Benford Law Analysis Results',fontsize=20)
        ax.set_xlabel('Digits', fontsize=16)
        
        if not self.normalized:
            ax.set_ylabel('Freq', fontsize=16)
             
        if self.normalized:
            df = pd.DataFrame({'Benford Reference':[30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6],'P(D) Results':self.digits_count},index=self.digits)
            df.plot.bar(ax=ax,grid=False,  color=['teal','#5cb85c'], width=0.8)
            for p in ax.patches:
                value = '{:.01f}'.format(p.get_height()) # Get the value length
                offset = (8 - len(value)) // 2 / 30      # Calculate the offset to center the label on the bar
                       
                ax.annotate('{:.01f}'.format(p.get_height()), (p.get_x()+offset, p.get_height()+0.1),fontsize=9,  weight='bold')
        else:
            ax.bar(self.digits, self.digits_count, color='g')
        
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='right')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.get_yaxis().set_ticks([])
            
        plt.show()

        return None

    def export_to_csv(self, path):
        """ Function to export the benford analysis results to a file as a dataframe, including the benford reference values
        Parameters:
        -------------
            
        path = str, path and filename where to save the results
         
        Returns:
        -------------
        A saved .csv file
        """

        df = pd.DataFrame({'Benford Reference':[30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6],'P(D) results':self.digits_count},index=self.digits)
        df.index.rename('Digits',inplace=True)
        df.to_csv(path, header=True)

        return None



        



