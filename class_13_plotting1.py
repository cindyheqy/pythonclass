# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:51:06 2022

@author: Cindy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# random walk
x = range(300)
y = np.random.choice([-1, 0, 1], 300) # randomly choose from -1, 0 and 1, 300 times
y = np.cumsum(y) # random walk: add all values of y

fig, ax1 = plt.subplots()
ax1.plot(x, y)

# colors and lines
fig, ax2 = plt.subplots()
ax2.plot(x, y, color='red', linestyle='dashed', marker='o', linewidth=2, 
         markersize=5, markerfacecolor='red', markeredgecolor='black')

fig, ax3 = plt.subplots()
ax3.plot(x, y, 'r-', label='A red line')
ax3.plot(x, y[::-1], 'b-', label='Ablue line')
ax3.legend(loc='best')

fig, ax4 = plt.subplots()
ax4.plot(x, y, 'b-')

ax4.set_ylabel('Hello Y axis')
ax4.set_xlabel('X Axis is here')
ax4.set_title('The plot title says hi')

ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

ax4.axvline(150, color='k', linestyle=':')
ax4.axhline(5, color='k', linestyle=':')

df = pd.DataFrame({'values_x': x, 'values_y': y}) # use pandas to create dataframe
ax = df.plot(x='values_x', y='values_y') # df.plot method is on pandas dataframe and will return matplotlib object, so that we can then pass it into ax and use matplotlib function
ax.axvline(150, color='k', linestyle=':') # add vertical line by using matplotlib