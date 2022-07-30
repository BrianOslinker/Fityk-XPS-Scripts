#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:35:02 2022

@author: brian
"""

import tkinter as tk
import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tkinter import filedialog
from matplotlib.figure import figaspect

# import data
root = tk.Tk()
root.attributes('-topmost', True)                     # forces window to top
root.withdraw()                                       # hides empty window
file1 = filedialog.askopenfile(                       # ask for C1s location
    title='Select Data C1s')
file2 = filedialog.askopenfile(
    title='Select Data Si2p')                         # asks for Si2p location
output = filedialog.askdirectory(
    title='Select Save Folder')                       # asks where to save
root.destroy()

# Set Font Size
plt.rcParams['font.size'] = '16'

df = pd.read_csv(file1, names=['x', 'y'])
df2 = pd.read_csv(file2, names=['x', 'y'])

with plt.style.context(['seaborn-colorblind']):

    color = sns.color_palette("colorblind", 6)

    # create figure
    # create plot with aspect ratio
    w, h = figaspect(1/2)                   # defines plot aspect ratio
    fig, ax1 = plt.subplots(figsize=(w, h))

    plt.tight_layout()
    # ax1.figsize = (8.5, 4)

    # plot peaks against binding energy
    # ax1.plot(df['x'], df['y'], 'o', color=color)

    ax1.errorbar(df['x'], df['y'], yerr=0.05,
                 fmt='o', capsize=5, color=color[0], ms=10)

    ax1.errorbar(df2['x'], df2['y'], yerr=0.05,
                 fmt='^', capsize=5, color=color[1], ms=10)

    # plot C1s connecting line
    ax1.plot(df['x'], df['y'], linestyle='-.', color=color[0], label="C1s")

    # plot Si2p connecting line
    ax1.plot(df2['x'], df2['y'], linestyle='--', color=color[1], label="Si2p")

    plt.axhline(y=0, linestyle=':', color='black')

    # label Chart
    plt.legend(loc="lower left")
    ax1.set_xlabel('MoO$_{3}$ Coverage (ML)')  # global
    ax1.set_ylabel('Binding Energy Shift (eV)')  # global
    plt.tight_layout()


filename = "Binding Energy Shift"
# saves as .svg with same name as the .dat file
# filename = os.path.basename(str(file1))              # removes path from file
# filename = os.path.splitext(filename)[0]             # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
plt.rcdefaults
