#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:01:53 2021

@author: brianoslinker
"""

# import packages
import tkinter as tk
from tkinter import filedialog
import os
from matplotlib import pyplot as plt
import pandas as pd

# import data
root = tk.Tk()
root.withdraw()                                           # hides empty window
file = filedialog.askopenfile(
    title='Select Data Folder')                           # asks user for files
output = filedialog.askdirectory(
    title='Select Save Folder')                           # asks where to save
root.destroy()

# set line styles
line = ['-', '--', ':', '-.']
# set legend
leg = ['0.0 ML', '0.05 ML', '0.1 ML', '0.2 ML',
       '0.4 ML', '0.6 ML', '1.0 ML', '1.5 ML', '3.0 Ml', '4.0 ML']

# read file
df = pd.read_csv(file)

# find size
col = int(len(df.columns)/2)

# change to binding energy
if df['x1'].mean() < 60:
    for i in range(0, col):
        df['x'+str(i+1)] = 150 - df['x'+str(i+1)]
else:
    for i in range(0, col):
        df['x'+str(i+1)] = 350 - df['x'+str(i+1)]

with plt.style.context(['seaborn-colorblind']):

    # create figure
    fig, ax1 = plt.subplots()
#    ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention

    # plot peaks against binding energy
    for i in range(0, col):
        ax1.plot(df['x'+str(i+1)], df['y'+str(i+1)],
                 linestyle=line[(i % 4)], label=leg[i])

    ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention

    # label Chart
    # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")

    ax1.set_xlabel('Binding Energy')  # global
    ax1.set_ylabel('Count (# electrons)')  # global
    ax1.set_yticklabels([])  # remove numbers from y axis

    if df['x1'].mean() > 240:
        plt.title('C1s Waterfall')
        plt.xlim(287, 281)
    else:
        plt.title('Si2p Waterfall')
        plt.xlim(106, 98)

    plt.tight_layout()
    plt.legend(loc="upper right")

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(file))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
