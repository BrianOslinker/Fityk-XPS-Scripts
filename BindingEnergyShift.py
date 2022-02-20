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

# import data
root = tk.Tk()
root.attributes('-topmost', True)                       # forces window to top
root.withdraw()                                           # hides empty window
file1 = filedialog.askopenfile(
    title='Select Data C1s')
file2 = filedialog.askopenfile(
    title='Select Data Si2p')                       # asks user for files
output = filedialog.askdirectory(
    title='Select Save Folder')                           # asks where to save
root.destroy()

df = pd.read_csv(file1, names=['x', 'y'])
df2 = pd.read_csv(file2, names=['x', 'y'])

with plt.style.context(['seaborn-colorblind']):

    color = sns.color_palette("colorblind", 6)

    # create figure
    fig, ax1 = plt.subplots()
    plt.tight_layout()
    # ax1.figsize = (8.5, 4)

    # plot peaks against binding energy
    # ax1.plot(df['x'], df['y'], 'o', color=color)

    ax1.errorbar(df['x'], df['y'], yerr=0.05,
                 fmt='o', capsize=2, color=color[0])

    ax1.errorbar(df2['x'], df2['y'], yerr=0.05,
                 fmt='^', capsize=2, color=color[1])

    ax1.plot(df['x'], df['y'], linestyle='-.', color=color[0])

    ax1.plot(df2['x'], df2['y'], linestyle='--', color=color[1])

    plt.axhline(y=0, linestyle=':', color='black')

    # label Chart
    # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.title('BE Shift')
    ax1.set_xlabel('Monolayers (ML)')  # global
    ax1.set_ylabel('Electron Volt Shift (eV)')  # global
    plt.tight_layout()


# saves as .svg with same name as the .dat file
# removes path from file
filename = os.path.basename("BindingEnergyShift")
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
