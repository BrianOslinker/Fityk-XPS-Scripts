#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:04:21 2021

@author: brianoslinker
"""

# import packages
import tkinter as tk
from tkinter import filedialog
import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# import data
root = tk.Tk()
root.withdraw()                                           # hides empty window
file = filedialog.askopenfile(
    title='Select Data Folder')                           # asks user for files
output = filedialog.askdirectory(
    title='Select Save Folder')                           # asks where to save
root.destroy()

# read data
df = pd.read_csv(file)

# cut parts
df = df[df['Coverage'] < 1.0]

x = df['Molecules']
y = df['Delta Theta']

m, b = np.polyfit(x, df['Delta Theta'], 1)

with plt.style.context(['seaborn-colorblind']):

    # create figure
    fig, ax1 = plt.subplots()

    ax1.scatter(x, df['Delta Theta'])

    plt.plot(x, m*x, linestyle=':', label='Best Fit')

    for i in range(0, df.shape[0]):
        plt.text(x[i]+0.5e12, y[i], str(df.iloc[i, 0])+' ML')

    # label Chart
    plt.legend(loc='upper left')
    plt.title('Change in Surface Dipole Potential')
    ax1.set_xlabel('Aeral Density N$^-_A cm^{-2}$')  # global
    ax1.set_ylabel('Change in Surface Dipole (eV)')  # global
    plt.xlim(right=x.max()+0.4e13)
    plt.tight_layout()

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(file))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
