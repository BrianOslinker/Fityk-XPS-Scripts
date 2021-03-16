#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:17:25 2021

@author: Brian Oslinker
"""

# import packages
from ProcessData import GetXPSData
import PlotXPSData as draw

# choose data file
df = GetXPSData()

# calculates mean of Binding Energy
mean = df['Binding Energy'].mean()

# checks what ploting function to call
if mean > 260:
    draw.PlotC1s(df)
else:
    draw.PlotOther(df)
