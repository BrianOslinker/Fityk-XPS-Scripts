#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:17:25 2021

@author: Brian Oslinker
"""

# import packages
import tkinter as tk
from tkinter import filedialog
from pathlib2 import Path
import pandas as pd
import ProcessXPSData as xps
import os

# import data
root = tk.Tk()
root.withdraw()                                            # hides empty window
directory = filedialog.askdirectory(
    title='Select Data Folder')                            # asks user for file
output = filedialog.askdirectory(title='Save As Folder')   # asks where to save
root.destroy()                                             # removes window
# %%
pathlist = Path(directory).rglob('*.dat')
# %%
for path in pathlist:
    # %%
    # creates data frame with file
    df = pd.read_table(str(path), delimiter=' ')
# %%
    # choose data file
    df = xps.ProcessData(df)
# %%
    # checks what ploting function to call
    if df['Binding Energy'].mean() > 260:
        fig = xps.PlotC1s(df)
    else:
        fig = xps.PlotOther(df)
# %%
    # saves as .svg
    fig.savefig(os.path.join(
        output, os.path.splitext(str(path))[0]+".svg"))
