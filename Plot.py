#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:21:39 2021

@author: oz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:03:42 2021

@author: oz
"""

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from ProcessData import GetXPSData


df = GetXPSData()

#graph
data_fit = df['Fit']
data_measured = df['Measured']


#col = len(df.columns)

#assign doublet peaks
#for i in range (2,col-1):
#    data[] = df['Peak ' + str(i)]

x = df['Binding Energy']

sns.set()
sns.set_context('notebook') ## 'talk', 'notebook', 'poster'

fig, ax1 = plt.subplots()
ax1.invert_xaxis() 

ax1.set_xlabel('Binding Energy (eV)') ## global
ax1.set_ylabel('Count (# electrons)') ## global


data_a1 = df['Peak 1']
data_b1 = df['Peak 2']
data_c1 = df['Peak 3']
data_a2 = df['Peak 4']
data_b2 = df['Peak 5']
data_c2 = df['Peak 6']


#im1 = ax1.plot(x, data_fit, color = 'orange', linestyle = '-')
im1 = ax1.scatter(x, data_measured, color = 'black', marker = '.', label = 'Measured')
im2 = ax1.plot(x, data_fit, color = 'orange', linestyle = '-', label = 'Fit')
im3 = ax1.plot(x, data_a1, color = 'gray', linestyle = '--')
im4 = ax1.plot(x, data_a2, color = 'gray', linestyle = '--')
im5 = ax1.plot(x, data_b1, color = 'gray', linestyle = ':')
im6 = ax1.plot(x, data_b2, color = 'gray', linestyle = ':',)
im7 = ax1.plot(x, data_c1, color = 'gray', linestyle = '-.')
im8 = ax1.plot(x, data_c2, color = 'gray', linestyle = '-.')


ax1.grid(False) #hide grid lines
ax1.set_facecolor('White') #change background color
#ax1.legend(facecolor = 'w') #change legend color

#print(np.where(data_measured == np.max(data_measured))[0])


#annotations
ax1.annotate('Mo6+', xy = (x[np.where(data_a2 == np.max(data_a2))[0]],np.max(data_a2)), xycoords = 'data',
             xytext = (x[np.where(data_a2 == np.max(data_a2))[0]+60],np.max(data_a2)+60),
            arrowprops = dict(arrowstyle = 'simple'))

ax1.annotate('Mo5+', xy = (x[np.where(data_b2 == np.max(data_b2))[0]],np.max(data_b2)), xycoords = 'data',
             xytext = (x[np.where(data_b2 == np.max(data_b2))[0]+60],np.max(data_b2)+60),
            arrowprops = dict(arrowstyle = 'simple'))

ax1.annotate('Mo4+', xy = (x[np.where(data_c2 == np.max(data_c2))[0]],np.max(data_c2)), xycoords = 'data',
             xytext = (x[np.where(data_c2 == np.max(data_c2))[0]+30],np.max(data_c2)+60),
            arrowprops = dict(arrowstyle = 'simple'))

plt.legend(facecolor = 'w')
plt.title('MoO3d')
plt.tight_layout()

#plt.rcParams["axes.edgecolor"] = "black"
#plt.rcParams["axes.linewidth"] = 1


plt.savefig("MoO3d.svg") # save as svg