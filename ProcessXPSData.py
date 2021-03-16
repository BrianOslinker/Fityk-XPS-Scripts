#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:38:30 2021

@author: Brian Oslinker
"""

# import packages
from matplotlib import pyplot as plt


def ProcessData(df):

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

    # set binding energy to x for convenience
    x = df['Binding Energy']

    # set fit and measured
    data_fit = df['Fit']
    data_measured = df['Measured']

    # set peak pairs
    data_a1 = df['Peak 1']
    data_b1 = df['Peak 2']
    data_c1 = df['Peak 3']
    data_a2 = df['Peak 4']
    data_b2 = df['Peak 5']
    data_c2 = df['Peak 6']

    # create figure
    fig, ax1 = plt.subplots()
    ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
    plt.tight_layout()

    # plot peaks against binding energy
    ax1.scatter(x, data_measured, color='black', marker='.', label='Measured')
    ax1.plot(x, data_fit, color='orange', linestyle='-', label='Fit')
    ax1.plot(x, data_a1, color='gray', linestyle='--')
    ax1.plot(x, data_a2, color='gray', linestyle='--')
    ax1.plot(x, data_b1, color='gray', linestyle=':')
    ax1.plot(x, data_b2, color='gray', linestyle=':',)
    ax1.plot(x, data_c1, color='gray', linestyle='-.')
    ax1.plot(x, data_c2, color='gray', linestyle='-.')

    # label Chart
    plt.legend(facecolor='w')
    plt.title('MoO3d')
    ax1.set_xlabel('Binding Energy (eV)')  # global
    ax1.set_ylabel('Count (# electrons)')  # global

    return plt


def PlotC1s(df):

    # set binding energy to x for convenience
    x = df['Binding Energy']

    # set fit and measured
    data_fit = df['Fit']
    data_measured = df['Measured']

    # set peak pairs
    data_a = df['Peak 1']
    data_b = df['Peak 2']
    data_c = df['Peak 3']
    data_d = df['Peak 4']

    # create figure
    fig, ax1 = plt.subplots()
    ax1.invert_xaxis()  # invert x-axis to follow XPS plot convention
    plt.tight_layout()

    # plot peaks against binding energy
    ax1.scatter(x, data_measured, color='black', marker='.', label='Measured')
    ax1.plot(x, data_fit, color='orange', linestyle='-', label='Fit')
    ax1.plot(x, data_a, color='gray', linestyle='--')
    ax1.plot(x, data_b, color='gray', linestyle='-')
    ax1.plot(x, data_c, color='gray', linestyle=':')
    ax1.plot(x, data_d, color='gray', linestyle='-.',)

    # label Chart
    plt.legend(facecolor='w')
    plt.title('MoO3d')
    ax1.set_xlabel('Binding Energy (eV)')  # global
    ax1.set_ylabel('Count (# electrons)')  # global

    return plt
