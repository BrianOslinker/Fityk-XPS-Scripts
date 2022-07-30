#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:04:21 2021

@author: brianoslinker
"""

# import packages
import tkinter as tk
import os
import pandas as pd
import numpy as np
from tkinter import filedialog
from matplotlib import pyplot as plt


# import data
root = tk.Tk()
root.attributes('-topmost', True)                   # forces window to top
root.withdraw()                                     # hides empty window
file = filedialog.askopenfile(
    title='Select Data Folder')                     # asks user for files
output = filedialog.askdirectory(
    title='Select Save Folder')                     # asks where to save
root.destroy()

# Set Font Size
plt.rcParams['font.size'] = '16'

# read data
df = pd.read_csv(file)

# cut parts
df = df[df['Coverage'] <= 0.4]

# set values to x and y for convenience
x = df['Molecules']
y = df['Delta Theta']

'''
get 1st degree polynomial fit from data
function is deprecated, rewrite using numpy.polynomial in future
'''
m, b = np.polyfit(x, y, 1)

# temp set style to seaborn colorblind
with plt.style.context(['seaborn-colorblind']):

    # create figure
    fig, ax1 = plt.subplots()

    # creates a scaterplot of data
    ax1.scatter(x, y)

    # plots best fit line from first data point
    plt.plot(x, m*x, linestyle=':', label='Best Fit')

    # labels the points with ML value for respective points
    for i in range(0, df.shape[0]):
        plt.text(x[i]+((x.max()*.025)), y[i], str(df.iloc[i, 0])+' ML')

    # label Chart
#    plt.legend(loc='upper left')
    # plt.title('Change in Surface Dipole Potential')
    ax1.set_xlabel('Areal Density N$^-_A cm^{-2}$')  # global
    ax1.set_ylabel('Change in Surface Dipole (eV)')  # global
    plt.xlim(right=x.max()*1.25)
    plt.tight_layout()

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(file))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
# filename = os.path.splitext(filename)[0]        # removes .dat from file
# fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
plt.rcdefaults
