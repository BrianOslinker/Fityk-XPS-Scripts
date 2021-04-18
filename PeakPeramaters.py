#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:22:29 2021

@author: oz
"""

import tkinter as tk
from tkinter import filedialog
from pathlib2 import Path
import os
import pandas as pd

root = tk.Tk()
root.withdraw()

file = filedialog.askopenfilename()

df = pd.read_table(file)

print(df)
