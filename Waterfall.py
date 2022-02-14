# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 00:54:53 2022

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

offset = 2e5  # defines offset (as electron counts so use big numbers)

# creates a list of .dat files in the directory
pathlist = Path(directory).rglob('*.dat')

# create figure
fig, ax1 = plt.subplots()
ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
plt.tight_layout()

i = 0
# parses each .dat file
for path in pathlist:

    # choose data file
    df = xps.ProcessData(path)

    x = df['Binding Energy']    # set binding energy to x for convenience

    # set fit and measured
    data_fit = df['Fit']
    data_measured = df['Measured']

    # plot figure
    ax1.plot(x, data_fit - (i*offset), color='grey')
    i = i+1

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(path))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file

plt.title("C1s")     # gives the plot the same title as the filename
plt.tight_layout()
ax1.set_yticklabels([])
plt.yticks([])

# plt.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
plt.savefig("C1s.svg")  # saves as svg
