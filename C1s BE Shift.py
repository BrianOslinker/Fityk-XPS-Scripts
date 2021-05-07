#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:15:57 2021

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

df = pd.read_csv(file, names=['x', 'y'])

with plt.style.context(['seaborn-colorblind']):

    # create figure
    fig, ax1 = plt.subplots()
    plt.tight_layout()
#    ax1.figsize = (8.5, 4)

    # plot peaks against binding energy
    #ax1.plot(df['x'], df['y'], 'o', color=color)

    ax1.errorbar(df['x'], df['y'], yerr=0.025,
                 fmt='o', capsize=5, color='black')

    ax1.plot(df['x'], df['y'], linestyle='--')

    plt.axhline(y=0, linestyle=':', color='black')

    # label Chart
    # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.title('C1s BE Shift')
    ax1.set_xlabel('Monolayers (ML)')  # global
    ax1.set_ylabel('Electron Volt Shift (eV)')  # global
    plt.tight_layout()

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(file))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
