#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:38:30 2021

@author: Brian Oslinker
"""

# import packages
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


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


def ImprovedPlot(df):
    """Now short enough to be incorperated into scripts."""
    with plt.style.context(['seaborn-colorblind']):

        color = sns.color_palette("colorblind", 6)

        x = df['Binding Energy']    # set binding energy to x for convenience

        # set fit and measured
        data_fit = df['Fit']
        data_measured = df['Measured']

        # create figure
        fig, ax1 = plt.subplots()
        ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
        # plt.tight_layout()

        col = len(df.columns)  # Size

        line = ['--', ':', '-.', '-']

        label = ['Mo$^{6}$', 'Mo$^{5}$', 'Mo$^{4}$']

        '"PLOT"'
        # axis_size = [287, 281]
        ax1.plot(x, data_measured, '.', color='black', label='Data')
        ax1.plot(x, data_fit, linestyle='-', color=color[0], label='Sum')

        for i in range(1, col-2):
            ax1.plot(x, df['Peak ' + str(i)], linestyle=line[i-1],
                     color=color[i], label=label[i-1])  # label

        ax1.set_yticks([])
        ax1.set_xlim([241, 227])
        ax1.legend(loc='upper left')
        ax1.set_xlabel("Binding Energy (eV)")
    return plt


def DeprecatedPlot(df):
    """Create graph for C1s, Si2p, and Mo3d XPS measurements."""
    # color = ['black', 'orange', 'red', 'green', 'blue', 'violet']
    with plt.style.context(['seaborn-colorblind']):
        # set binding energy to x for convenience
        x = df['Binding Energy']

        'DEFINE COLOR PALETTE'
        color = sns.color_palette("colorblind", 6)

        # print(color[:]) 'debug only'

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

                doublet_a = 'Mo$^{6+}$'
                doublet_b = 'Mo$^{5+}$'
                doublet_c = 'Mo$^{4+}$'

                axis_size = [241, 227]

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

                axis_size = [106, 98]

                doublet_a = 'Si$^{3+}$'
                doublet_b = 'Si$^{2+}$'
                doublet_c = 'Si$^{1+}$'

                color_a = color[1]
                color_b = color[2]
                color_c = color[3]

            # plot peaks against binding energy
            ax1.plot(x, data_measured, '.', color='black', label='Data')
            ax1.plot(x, data_fit, color=color[0], linestyle='-', label='Sum')
            ax1.plot(x, data_a1, color=color_a,
                     linestyle='--', label=doublet_a)
            ax1.plot(x, data_a2, color=color_a, linestyle='--')
            ax1.plot(x, data_b1, color=color_b,
                     linestyle=':', label=doublet_b)
            ax1.plot(x, data_b2, color=color_b, linestyle=':',)
            ax1.plot(x, data_c1, color=color_c,
                     linestyle='-.', label=doublet_c)
            ax1.plot(x, data_c2, color=color_c, linestyle='-.')
        elif df['Binding Energy'].mean() > 240:
            data_a = df['Peak 1']
            data_b = df['Peak 2']
            data_c = df['Peak 3']
            data_d = df['Peak 4']

            axis_size = [287, 281]

            ax1.plot(x, data_measured, '.', color='black', label='Data')
            ax1.plot(x, data_fit, linestyle='-', color=color[0], label='Sum')
            ax1.plot(x, data_a, linestyle='--',
                     color=color[1], label='B$_{(2x1)}$')
            ax1.plot(x, data_b, linestyle=':', color=color[2], label='Bulk')
            ax1.plot(x, data_c, linestyle='-.',
                     color=color[3], label='C$_{Si1}$')
            ax1.plot(x, data_d, linestyle='-',
                     color=color[4], label='C$_{Si2}$')

        elif 99 < df['Binding Energy'].mean() < 102:
            # set peak pairs
            data_a1 = df['Peak 1']
            data_a2 = df['Peak 2']
            data_b1 = df['Peak 3']
            data_b2 = df['Peak 4']

            axis_size = [106, 98]

            # plot peaks against binding energy
            ax1.plot(x, data_measured, '.', color='black', label='Data')
            ax1.plot(x, data_fit, color=color[0], linestyle='-', label='Sum')
            ax1.plot(x, data_a1, color=color[2],
                     linestyle=':', label='Si$^{2+}$')
            ax1.plot(x, data_a2, color=color[2], linestyle=':')
            ax1.plot(x, data_b1, color=color[3],
                     linestyle='-.', label='Si$^{1+}$')
            ax1.plot(x, data_b2, color=color[3], linestyle='-.',)
        else:
            # set peak pairs
            data_a1 = df['Peak 1']
            data_b1 = df['Peak 2']
            data_a2 = df['Peak 3']
            data_b2 = df['Peak 4']

            axis_size = [241, 227]

            # plot peaks against binding energy
            ax1.plot(x, data_measured, '.', color='black', label='Data')
            ax1.plot(x, data_fit, color=color[0], linestyle='-', label='Sum')
            ax1.plot(x, data_a1, color=color[2],
                     linestyle='--', label='Mo$^{5+}$')
            ax1.plot(x, data_a2, color=color[2], linestyle='--')
            ax1.plot(x, data_b1, color=color[3],
                     linestyle=':', label='Mo$^{4+}$')
            ax1.plot(x, data_b2, color=color[3], linestyle=':',)

        """" label Chart"""
        plt.legend(loc="upper right")
        ax1.set_xlabel('Binding Energy (eV)')  # global
        ax1.set_ylabel('Arbitrary Units')  # global
        ax1.set_yticklabels([])
        plt.yticks([])                                  # remove y tick marks

        # if axis_size is not None:
        # set the xlim to left, right
        plt.xlim(axis_size[0], axis_size[1])

    return plt
