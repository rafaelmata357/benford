# A Python package to apply the Benford´s Law analysis

## Project Motivation

As part of the Udacity Data Science nanodegree this is a project to create and deploy a Python package, based on this I decided to use the Benford´s Law to create a package using OOP than can apply the analyzis to a dataset, an imgae or a numpy array of numbers.

## Installation:

`pip intall py-benford`


This package uses these libraries

- pandas
- numpy 
- matplotlib


The python version used: **3.8**

## Files in the repository

- README.md    : This file
- setup.py     : Setup file for the package
- .gitignore   : File to ignore files and not load to the GitHub repository
- LICENSE      : The MIT License
- py-benford
    - bendord.py     :   The Benford Class
    - __init__.py    :   Inititalization file for the package
- tests
    - tests.py       :   Script for unit tests of the Benford Class
    - Benford_plot_test.ipynb : Jupyter Notebook to test the graphs plotting ot the Benford Class
    - flower.jpg     :   JPG image to test the Benford Class
    - population.csv :   CSV dataset with the Wordl Population to test the Benford Class



## How To use the package  

1. Create an instace with the Benford Class
    - `benford = Benford()`

2. Load a dataset or an image , 
    - `bendford.load_dataset(dataset_name)`
    - `benford.load_image(image_name)`

3. Do the benford analysis using the benford_analysis method
    - `benford.benford_analysis()`

4. Graph or plot the results using plot() method
    - `benford.plot()`

5. Save the results using expor_to_csv() method:
    - `benford.export_to_csv(filename)`


### Example using the pakage to analyze an image:



```python
#Import libraries
import pandas as pd
import numpy as np
from py-benford import Benford
import matplotlib.pyplot as plt
from PIL import Image


image_file = 'flower.jpg'      #Read image
image = Benford()              #Create Benford instance
image.load_image(image_file)   #Load image
image.benford_analysis()       #Do Analysis
image.plot()                   #Plot Benford´s analysis
```


![Example](https://github.com/rafaelmata357/benford/blob/master/docs/image-benford-analysis.png)



## Terms of use:

This is a tool to do  an initial analyzis using Benford´s Law  and plot how the digit´s probability are distributed on different datasets, it is not a formal analysis or study using the Benford´s Law 

## License:

The code follows this license: https://opensource.org/licenses/MIT
