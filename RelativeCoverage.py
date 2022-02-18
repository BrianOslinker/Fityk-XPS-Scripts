#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:12:33 2021

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

# read data
df = pd.read_csv(file)

with plt.style.context(['seaborn-colorblind']):

    # create figure
    fig, ax1 = plt.subplots()
    plt.tight_layout()
#    ax1.figsize = (8.5, 4)

    # plot peaks against binding energy
    #ax1.plot(df['x'], df['y'], 'o', color=color)

#    ax1.errorbar(df['x'], df['y'], yerr=0.05,
#                 fmt='o', capsize=2)

#    ax1.plot(df['x'], df['y'], linestyle='--', color='orange')

#    plt.axhline(y=0, linestyle=':', color='black')

    plt.errorbar(df['Coverage'], df['Mo5+'],
                 yerr=df['Mo5+ Error'], fmt='.', capsize=3, )

    ax1.plot(df['Coverage'], df['Mo5+'], linestyle='--',
             color='lightblue', label='Mo$^{5+}$')

    plt.errorbar(df['Coverage'], df['Mo6+'],
                 yerr=df['Mo6+ Error'], fmt='.', capsize=3, color='darkorange')

    ax1.plot(df['Coverage'], df['Mo6+'], linestyle=':',
             color='orange', label='Mo$^{6+}$')

    # label Chart
    # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.legend(loc='upper right')
    plt.title('Relative  Coverage of Mo$^{5+}$ and Mo$^{6+}$')
    ax1.set_xlabel('Monolayers (ML)')  # global
    ax1.set_ylabel('Coverage (%)')  # global
    plt.ylim(0, 100)
    plt.tight_layout()

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(file))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
# filename = os.path.splitext(filename)[0]        # removes .dat from file
# fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
