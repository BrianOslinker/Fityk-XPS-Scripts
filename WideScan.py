#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 16:16:05 2021

@author: Brian Oslinker
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
root.destroy()                                            # removes window


df = pd.read_table(file, delimiter=' ', names=['x', 'y'])

df['x'] = 850 - df['x']

# return row of largest y
c1s = df.nlargest(1, 'y')

# lazy way to get other core levels
df2 = df[df['x'] < 250]
si2p = df2.nlargest(1, 'y')

df3 = df[df['x'] > 300]
o1s = df3.nlargest(1, 'y')


with plt.style.context(['seaborn-colorblind']):

    # create figure
    fig, ax1 = plt.subplots()
    ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
    plt.tight_layout()
#    ax1.figsize = (8.5, 4)

    # plot peaks against binding energy
    ax1.plot(df['x'], df['y'])

    # label Chart
    # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")

    # label peaks
    plt.text(c1s['x']-5, c1s['y'], 'C 1s')
    plt.text(si2p['x']-5, si2p['y'], 'Si 2p')
    plt.text(o1s['x']-5, o1s['y'], 'O 1s')

    plt.title('850 eV Survey Scan')
    ax1.set_xlabel('Binding Energy (eV)')  # global
    ax1.set_ylabel('Count (# electrons)')  # global
    ax1.set_yticklabels([])  # remove numbers from y axis
    plt.tight_layout()

# saves as .svg with same name as the .dat file
filename = os.path.basename(str(file))          # removes path from file
filename = os.path.splitext(filename)[0]        # removes .dat from file
fig.savefig(os.path.join(output, filename + ".svg"))  # saves as svg
