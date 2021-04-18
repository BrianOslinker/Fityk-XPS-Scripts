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
root.withdraw()                                           # hides empty window
directory = filedialog.askdirectory(
    title='Select Data Folder')                           # asks user for files
output = filedialog.askdirectory(
    title='Select Save Folder')                           # asks where to save
root.destroy()                                            # removes window

# creates a list of .dat files in the directory
pathlist = Path(directory).rglob('*.dat')

# parses each .dat file
for path in pathlist:

    # choose data file
    df = xps.ProcessData(path)

    """
    checks what ploting function to call
    currently only works for C1s, MoO3d, and Si2p core levels
    """
    if df['Binding Energy'].mean() > 260:
        fig = xps.PlotC1sSeaborn(df)
    else:
        fig = xps.PlotOtherSeaborn(df)

    # saves as .svg with same name as the .dat file
    filename = os.path.basename(str(path))          # removes path from file
    filename = os.path.splitext(filename)[0]        # removes .dat from file

    plt.title(filename)     # gives the plot the same title as the filename

    fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
