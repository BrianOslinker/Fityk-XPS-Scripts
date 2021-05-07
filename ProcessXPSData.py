#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:38:30 2021

@author: Brian Oslinker
"""

# import packages
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


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


def Plot(df):

    # color = ['black', 'orange', 'red', 'green', 'blue', 'violet']
    with plt.style.context(['seaborn-colorblind']):
        # set binding energy to x for convenience
        x = df['Binding Energy']

        color = sns.color_palette("colorblind", 6)

        # print(color[:])

        # set fit and measured
        data_fit = df['Fit']
        data_measured = df['Measured']

        # create figure
        fig, ax1 = plt.subplots()
        ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
        plt.tight_layout()

        if len(df.columns)-3 == 6:
            # set peak pairs
            if df['Binding Energy'].mean() > 110:
                # set peak pairs
                data_a1 = df['Peak 1']
                data_b1 = df['Peak 2']
                data_c1 = df['Peak 3']
                data_a2 = df['Peak 4']
                data_b2 = df['Peak 5']
                data_c2 = df['Peak 6']

                doublet_a = 'Doublet A'
                doublet_b = 'Doublet B'
                doublet_c = 'Doublet C'

                color_a = color[1]
                color_b = color[2]
                color_c = color[3]

            else:
                # set Peak Pairs
                data_a1 = df['Peak 1']
                data_a2 = df['Peak 2']
                data_b1 = df['Peak 3']
                data_b2 = df['Peak 4']
                data_c1 = df['Peak 5']
                data_c2 = df['Peak 6']

                axis_size = [105, 99]

                doublet_a = 'Si3'
                doublet_b = 'Si2'
                doublet_c = 'Si1'

                color_a = color[3]
                color_b = color[1]
                color_c = color[2]

            # plot peaks against binding energy
            ax1.plot(x, data_measured, '.', color='black')
            ax1.plot(x, data_fit, color=color[0], linestyle='-')
            ax1.plot(x, data_a1, color=color_a,
                     linestyle='--', label=doublet_a)
            ax1.plot(x, data_a2, color=color_a, linestyle='--')
            ax1.plot(x, data_b1, color=color_b,
                     linestyle=':', label=doublet_b)
            ax1.plot(x, data_b2, color=color_b, linestyle=':',)
            ax1.plot(x, data_c1, color=color_c,
                     linestyle='-.', label=doublet_c)
            ax1.plot(x, data_c2, color=color_c, linestyle='-.')
        elif df['Binding Energy'].mean() > 200:
            data_a = df['Peak 1']
            data_b = df['Peak 2']
            data_c = df['Peak 3']
            data_d = df['Peak 4']

            axis_size = [287, 281]

            ax1.plot(x, data_measured, '.', color='black')
            ax1.plot(x, data_fit, linestyle='-', color=color[0])
            ax1.plot(x, data_a, linestyle='--', color=color[1], label='B*')
            ax1.plot(x, data_b, linestyle=':', color=color[2], label='Bulk')
            ax1.plot(x, data_c, linestyle='-.', color=color[3], label='B1')
            ax1.plot(x, data_d, linestyle='-', color=color[4], label='B2')

        elif 99 < df['Binding Energy'].mean() < 102:
            # set peak pairs
            data_a1 = df['Peak 1']
            data_a2 = df['Peak 2']
            data_b1 = df['Peak 3']
            data_b2 = df['Peak 4']

            axis_size = [104, 95]

            # plot peaks against binding energy
            ax1.plot(x, data_measured, '.', color='black')
            ax1.plot(x, data_fit, color=color[0], linestyle='-')
            ax1.plot(x, data_a1, color=color[1],
                     linestyle='--', label='Si1')
            ax1.plot(x, data_a2, color=color[1], linestyle='--')
            ax1.plot(x, data_b1, color=color[2],
                     linestyle=':', label='Si2')
            ax1.plot(x, data_b2, color=color[2], linestyle=':',)
        else:
            # set peak pairs
            data_a1 = df['Peak 1']
            data_b1 = df['Peak 2']
            data_a2 = df['Peak 3']
            data_b2 = df['Peak 4']

            # plot peaks against binding energy
            ax1.plot(x, data_measured, '.', color='black')
            ax1.plot(x, data_fit, color=color[0], linestyle='-')
            ax1.plot(x, data_a1, color=color[1],
                     linestyle='--', label='Doublet A')
            ax1.plot(x, data_a2, color=color[1], linestyle='--')
            ax1.plot(x, data_b1, color=color[2],
                     linestyle=':', label='Doublet B')
            ax1.plot(x, data_b2, color=color[2], linestyle=':',)

        # label Chart
        plt.legend(loc="upper right")
        ax1.set_xlabel('Binding Energy (eV)')  # global
        ax1.set_ylabel('Count (# electrons)')  # global
        ax1.set_yticklabels([])

        # if axis_size is not None:
        # set the xlim to left, right
        plt.xlim(axis_size[0], axis_size[1])
#        plt.xlim(287, 281)

    return plt
