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

Coverage = [0.00, 0.05, 0.10, 0.15, 0.20, 0.30,
            0.40, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 3.00, 4.00]

# create figure
'''
fig = plt.figure(constrained_layout=True)

gs = GridSpec(1, 3, figure=fig)
axis[0] = fig.add_subplot(gs[0, :])
axis[1] = fig.add_subplot(gs[1, :])
'''

w, h = figaspect(2/1)  # defines plot aspect ratio

# fig, axis = plt.subplots(2, 1, sharex=True, gridspec_kw={
#                         'height_ratios': [1, 2]}, figsize=(w, h))

fix, axis = plt.subplots(figsize=(w, h))

# for a in axis:
#    a.set_yticklabels([])
axis.set_yticks([])

'''adjust plot settings'''
# plt.subplots_adjust(hspace=0)

axis.invert_xaxis()

i = 2
# parses each .dat file
for path in pathlist:

    # choose data file
    df = xps.ProcessData(path)

    x = df['Binding Energy']    # set binding energy to x for convenience

    # set fit and measured
    data_fit = df['Fit']
    data_measured = df['Measured']

    # plot figure

    if i == 2:
        offset = data_measured.max()*.25

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
