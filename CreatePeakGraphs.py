#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:17:25 2021

@author: Brian Oslinker
"""

# import packages
import tkinter as tk
from tkinter import filedialog
from pathlib2 import Path
import os
import pandas as pd
import ProcessXPSData as xps

# import data
root = tk.Tk()
root.withdraw()                                           # hides empty window
directory = filedialog.askdirectory(
    title='Select Data Folder')                           # asks user for files
output = filedialog.askdirectory(title='Save As Folder')  # asks where to save
root.destroy()                                            # removes window

# creates a list of .dat files in the directory
pathlist = Path(directory).rglob('*.dat')

# parses each .dat file
for path in pathlist:

    # creates data frame with file
    df = pd.read_table(str(path), delimiter=' ')

    # choose data file
    df = xps.ProcessData(df)

    # checks what ploting function to call
    if df['Binding Energy'].mean() > 260:
        fig = xps.PlotC1s(df)
    else:
        fig = xps.PlotOther(df)

    # saves as .svg with same name as the .dat file

    filename = os.path.basename(str(path))          # removes path from file
    filename = os.path.splitext(filename)[0]        # removes .dat from file
    fig.savefig(os.path.join(output, filename+".svg"))  # saves as svg
