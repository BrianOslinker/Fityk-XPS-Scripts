#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:17:25 2021

@author: Brian Oslinker
"""

# import packages
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import ProcessXPSData as xps

# import data
root = tk.Tk()
root.withdraw()                                            # hides empty window
df = filedialog.askopenfilename(title='Select Data')       # asks user for file
output = filedialog.asksaveasfile(title='Save As')         # asks where to save
root.destroy()                                             # removes window

# creates data frame with file
df = pd.read_table(df, delimiter=' ')

# choose data file
df = xps.ProcessData(df)

# checks what ploting function to call
if df['Binding Energy'].mean() > 260:
    xps.PlotC1s(df, output)
else:
    xps.PlotOther(df, output)
