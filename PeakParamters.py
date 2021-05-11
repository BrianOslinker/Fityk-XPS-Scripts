#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:28:36 2021

@author: brianoslinker
"""

# import packages
import tkinter as tk
import os
import ProcessXPSData as xps
from matplotlib import pyplot as plt
from tkinter import filedialog
#from pathlib2 import Path
import pandas as pd

# import data
root = tk.Tk()
root.withdraw()                                           # hides empty window
file = filedialog.askopenfile(
    title='Select Data Folder')                           # asks user for files
# output = filedialog.asksaveasfilename(
#    title='Select Save Folder')                           # asks where to save
root.destroy()

# creates dataframe from .dat file
df = pd.read_table(file, delimiter=' ')


df = df.to_csv('output.csv')
