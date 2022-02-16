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

offset = 2.5e5  # defines offset (as electron counts so use big numbers)

# creates a list of .dat files in the directory
pathlist = Path(directory).rglob('*.dat')

# create figure
'''
fig = plt.figure(constrained_layout=True)

gs = GridSpec(1, 3, figure=fig)
axis[0] = fig.add_subplot(gs[0, :])
axis[1] = fig.add_subplot(gs[1, :])
'''

w, h = figaspect(1.5/1)  # defines plot aspect ratio

fig, axis = plt.subplots(2, 1, sharex=True, gridspec_kw={
                         'height_ratios': [1, 2]}, figsize=(w, h))

for a in axis:
    #    a.set_yticklabels([])
    a.set_yticks([])

'''adjust plot settings'''
plt.subplots_adjust(hspace=0)

axis[1].invert_xaxis()

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
    axis[1].plot(x, data_fit - (i*offset), color='grey')

    if i == 0:
        color = sns.color_palette("colorblind", 6)
        col = len(df.columns)
        axis[0].plot(x, data_measured, '.', color='Black')
        axis[0].plot(x, data_fit, linestyle='-', color=color[0])
        line = ['--', ':', '-.', '-']

        for i in range(1, col-3):
            axis[0].plot(x, df['Peak ' + str(i)], linestyle=line[i-1],
                         color=color[i-1])

    i = i+1

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(path))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file

# plt.title("Si2p")     # gives the plot the same title as the filename
# plt.set_xlabel('Binding Energy (eV)')  # global
# plt.set_ylabel('Arbitrary Units')  # global
# plt.tight_layout()
# axis[0].invert_xaxis()  # invert x-axis to follow XPS plot convention

plt.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
