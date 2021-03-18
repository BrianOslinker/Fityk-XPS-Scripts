#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:38:30 2021

@author: Brian Oslinker
"""

# import packages
from matplotlib import pyplot as plt
import pandas as pd


def ProcessData(path):
    """
    Take a fityk .dat file and return a dataframe sorted by binding energy.

    Parameters
    ----------
    path : fityk .dat file
        .dat file generated from fityk

    Returns
    -------
    df : dataframe
        returns a dataframe in the
        format [Binding Energy, Sum of Fuctions (Fit), Measured Values,
                Peak 1 (lowest BE), ..., Peak n (highest BE)]

    """
    # creates dataframe from .dat file
    df = pd.read_table(str(path), delimiter=' ')

    # find size
    col = len(df.columns)

    # create generic header
    header = range(col)
    df.columns = header

    # rename known rows
    df.rename(columns={0: 'Kenetic Energy',
                       1: 'Measured', col-1: 'Fit'}, inplace=True)

    # convert KE to BE
    if (df['Kenetic Energy'].mean()) < 60:                # check for Si2p case
        df['Kenetic Energy'] = 150 - df['Kenetic Energy']
    else:
        df['Kenetic Energy'] = 350 - df['Kenetic Energy']
    df.rename(columns={'Kenetic Energy': 'Binding Energy'}, inplace=True)

    # find binding energy of peaks
    sort = df.idxmax()               # finds index of max value for each column
    sort = sort.drop(['Binding Energy', 'Fit', 'Measured'],
                     axis='rows')    # remove unnecessary data
    sort = sort.sort_values()        # returns correct peak order

    # name peaks by binding energy (smallest to largest)
    for i in range(2, col-1):
        df.rename(
            columns={sort.index.values[i-2]: 'Peak ' + str(i-1)}, inplace=True)

    # sort columns by name
    df = df.sort_index(axis=1)

    return df


def PlotOther(df):

    color = ['black', 'orange', 'red', 'green', 'blue', 'violet']

    # set binding energy to x for convenience
    x = df['Binding Energy']

    # set fit and measured
    data_fit = df['Fit']
    data_measured = df['Measured']

    # create figure
    fig, ax1 = plt.subplots()
    ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
    plt.tight_layout()

    if len(df.columns)-3 == 6:
        # set peak pairs
        data_a1 = df['Peak 1']
        data_b1 = df['Peak 2']
        data_c1 = df['Peak 3']
        data_a2 = df['Peak 4']
        data_b2 = df['Peak 5']
        data_c2 = df['Peak 6']

        # plot peaks against binding energy
        ax1.plot(x, data_measured, 'o', color=color[0])
        ax1.plot(x, data_fit, color=color[1], linestyle='-')
        ax1.plot(x, data_a1, color=color[2], linestyle='--', label='Doublet A')
        ax1.plot(x, data_a2, color=color[2], linestyle='--')
        ax1.plot(x, data_b1, color=color[3], linestyle=':', label='Doublet B')
        ax1.plot(x, data_b2, color=color[3], linestyle=':',)
        ax1.plot(x, data_c1, color=color[4], linestyle='-.', label='Doublet C')
        ax1.plot(x, data_c2, color=color[4], linestyle='-.')
    else:
        # set peak pairs
        data_a1 = df['Peak 1']
        data_b1 = df['Peak 2']
        data_a2 = df['Peak 3']
        data_b2 = df['Peak 4']

        # plot peaks against binding energy
        ax1.plot(x, data_measured, 'o', color=color[0])
        ax1.plot(x, data_fit, color=color[1], linestyle='-')
        ax1.plot(x, data_a1, color=color[2], linestyle='--', label='Doublet A')
        ax1.plot(x, data_a2, color=color[2], linestyle='--')
        ax1.plot(x, data_b1, color=color[3], linestyle=':', label='Doublet B')
        ax1.plot(x, data_b2, color=color[3], linestyle=':',)

    # label Chart
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    ax1.set_xlabel('Binding Energy (eV)')  # global
    ax1.set_ylabel('Count (# electrons)')  # global
    plt.tight_layout()

    if df['Binding Energy'].mean() > 225:
        plt.title("MoO3d")
    else:
        plt.title("Si2p")

    return plt


def PlotC1s(df):

    # set binding energy to x for convenience
    x = df['Binding Energy']

    # set fit and measured
    data_fit = df['Fit']
    data_measured = df['Measured']

    # set peaks
    data_a = df['Peak 1']
    data_b = df['Peak 2']
    data_c = df['Peak 3']
    data_d = df['Peak 4']

    # create figure
    fig, ax1 = plt.subplots()
    ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
    plt.tight_layout()

    # plot peaks against binding energy
    ax1.plot(x, data_measured, 'o', color='black', label='Data')
    ax1.plot(x, data_fit, color='orange', linestyle='-', label='Sum')
    ax1.plot(x, data_a, color='red', linestyle='--', label='Peak A')
    ax1.plot(x, data_b, color='green', linestyle='-', label='Peak B')
    ax1.plot(x, data_c, color='blue', linestyle=':', label='Peak C')
    ax1.plot(x, data_d, color='violet', linestyle='-.', label='Peak D')

    # label Chart
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.title('C1s')
    ax1.set_xlabel('Binding Energy (eV)')  # global
    ax1.set_ylabel('Count (# electrons)')  # global
    plt.tight_layout()

    return plt
