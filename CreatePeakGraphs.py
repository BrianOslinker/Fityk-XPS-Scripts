#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:17:25 2021

@author: Brian Oslinker
"""

# import packages
import tkinter as tk
import os
import ProcessXPSData as xps
from matplotlib import pyplot as plt
from tkinter import filedialog
from pathlib2 import Path

# import data
root = tk.Tk()
root.attributes('-topmost', True)                       # forces window to top
root.withdraw()                                         # hides empty window
directory = filedialog.askdirectory(
    title='Select Data Folder')                         # asks user for files
output = filedialog.askdirectory(
    title='Select Save Folder')                         # asks where to save
root.destroy()                                          # removes window

# creates a list of .dat files in the directory
pathlist = Path(directory).rglob('*.dat')

# parses each .dat file
for path in pathlist:

    # choose data file
    df = xps.ProcessData(path)

    fig = xps.ImprovedPlot(df)  # Plots Figure

    # saves as .svg with same name as the .dat file
    filename = os.path.basename(str(path))          # removes path from file
    filename = os.path.splitext(filename)[0]        # removes .dat from file

    plt.title(filename)     # gives the plot the same title as the filename
    plt.tight_layout()

    fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
