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

# list of coverage for vairous doses
Coverage = [0.00, 0.05, 0.10, 0.15, 0.20, 0.30,
            0.40, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 3.00, 4.00]

a = 3                           # set spaceing between first plot and waterfall

# create plot with aspect ratio
w, h = figaspect(3/1)                   # defines plot aspect ratio
fix, axis = plt.subplots(figsize=(w, h))

axis.set_yticks([])                     # removes y-axis tick marks
axis.invert_xaxis()                     # inverts x-axis (traditional for xps)

i = a                           # determines the spacing of first 'waterfall'

# parses each .dat file
for path in pathlist:

    # choose data file
    df = xps.ProcessData(path)

    # set common dataframe values to variables for convenience
    x = df['Binding Energy']
    data_fit = df['Fit']
    data_measured = df['Measured']

    # peak_center = df['fit'].idxmax()                    # peak center

    # plot figure
    if i == a:

        # set offset as % of the max value of first (largest) dose
        offset = data_measured.max()*.25
        peakloc = df['Peak 2'].idxmax()
        ypeak = data_fit.iloc[peakloc]
        peak_center = x.iloc[peakloc]

        # set colors and styles for component functions of first plot
        color = sns.color_palette("colorblind", 6)
        col = len(df.columns)
        axis.plot(x, data_measured, '.', color='Black')
        axis.plot(x, data_fit, linestyle='-', color=color[0])
        line = ['--', ':', '-.', '-']

        # plots the various peaks in the first dose
        for j in range(1, col-3):
            axis.plot(x, df['Peak ' + str(j)], linestyle=line[j-1],
                      color=color[j-1])

        # sets location of ML labels
        xlabel = x.min()-.5

        # label for the first envelope
        plt.text(xlabel, (data_fit.iloc[-1]), str(Coverage[i-2])+' ML')

        # plots envelope of following doses
    else:
        axis.plot(x, data_fit - (i*offset), color='grey')

        # adds ML label to data
        plt.text(xlabel, (data_fit.iloc[-1] -
                          (i*offset)), str(Coverage[i-2])+' ML')

    i = i+1     # increase counter

# plot line at y = 0
plt.axhline(y=0, linestyle='-', linewidth=.5, color='black')

# plot vertical line from initial peak
plt.vlines(x=peak_center, ymin=-(i*offset), ymax=ypeak)


if peak_center <= 150:
    BElim = [98, 106]
else:
    BElim = [281, 288]

axis.set_xlim([BElim[1], BElim[0]])


# set x and y axis labels
axis.set_xlabel('Binding Energy (eV)')
axis.set_ylabel('Arbitrary Units')
plt.tight_layout()

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(path))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file

plt.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
