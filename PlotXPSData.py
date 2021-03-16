#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:38:30 2021

@author: Brian Oslinker
"""

# import packages
from matplotlib import pyplot as plt


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

    # save figure
    plt.savefig("MoO3d.svg")  # save as svg

    return


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

    # save figure
    plt.savefig("MoO3d.svg")  # save as svg

    return
