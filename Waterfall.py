#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 00:54:53 2022

@author: Brian Oslinker
"""

# import packages
import seaborn as sns
import tkinter as tk
import os
import ProcessXPSData as xps
from matplotlib import pyplot as plt
from matplotlib.figure import figaspect
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

# list of coverage for vairous does
Coverage = [0.00, 0.05, 0.10, 0.15, 0.20, 0.30,
            0.40, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 3.00, 4.00]


# create plot with aspect ratio
w, h = figaspect(2/1)  # defines plot aspect ratio
fix, axis = plt.subplots(figsize=(w, h))

axis.set_yticks([])                 # removes y-axis tick marks
axis.invert_xaxis()                 # inverts x-axis (traditional for xps)

i = 2
# parses each .dat file
for path in pathlist:

    # choose data file
    df = xps.ProcessData(path)

    # set common dataframe values to variables for convenience
    x = df['Binding Energy']
    data_fit = df['Fit']
    data_measured = df['Measured']

    "# plot figure"
    if i == 2:
        offset = data_measured.max()*.25

        # set colors and styles for component functions of first plot
        color = sns.color_palette("colorblind", 6)
        col = len(df.columns)
        axis.plot(x, data_measured, '.', color='Black')
        axis.plot(x, data_fit, linestyle='-', color=color[0])
        line = ['--', ':', '-.', '-']

        for j in range(1, col-3):
            axis.plot(x, df['Peak ' + str(j)], linestyle=line[j-1],
                      color=color[j-1])

        xlabel = x.min()-1.5

        plt.text(xlabel, (data_fit.iloc[-1]), str(Coverage[i-2])+' ML')

    else:
        axis.plot(x, data_fit - (i*offset), color='grey')

        plt.text(xlabel, (data_fit.iloc[-1] -
                          (i*offset)), str(Coverage[i-2])+' ML')

    i = i+1

plt.axhline(y=0, linestyle='-', linewidth=.5, color='black')

# plt.title("Si2p")     # gives the plot the same title as the filename
axis.set_xlabel('Binding Energy (eV)')
axis.set_ylabel('Arbitrary Units')
# plt.tight_layout()
# axis[0].invert_xaxis()  # invert x-axis to follow XPS plot convention

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(path))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file

plt.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
