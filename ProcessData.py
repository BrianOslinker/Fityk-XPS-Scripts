#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:00:10 2021

@author: Brian Oslinker
"""

def GetXPSData():

    #import packages
    import tkinter as tk
    from tkinter import filedialog    
    import pandas as pd

    #import data
    root = tk.Tk()
    root.withdraw()                     #hides empty window
    df = filedialog.askopenfilename()   #gets file from user
    
    #creates data frame with file
    df = pd.read_table(df, sep="\s+")
    
    #find size
    col = len(df.columns)
    
    #create generic header
    header = range(col)
    df.columns = header
       
    #rename known rows
    df.rename(columns={0:'Binding Energy',1:'Measured',col-1:'Fit'}, inplace=True)
    
    #convert KE to BE
    df['Binding Energy'] = 350 - df['Binding Energy']
    
    #find binding energy of peaks
    sort = df.idxmax()                                                      #finds index of max value for each column
    sort = sort.drop(['Binding Energy', 'Fit', 'Measured'], axis='rows')    #remove unnessacary data
    sort = sort.sort_values()                                               #returns correct peak order
    
    #name peaks by binding energy (smallest to largest)
    for i in range (2,col-1):
        df.rename(columns={sort.index.values[i-2]:'Peak ' + str(i-1)}, inplace=True)
        
    #sort columns by name   
    df = df.sort_index(axis=1)
    
    return df
