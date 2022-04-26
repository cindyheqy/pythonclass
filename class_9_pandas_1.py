# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:03:52 2022

@author: Cindy
"""

import pandas
import pandas as pd
from pandas import DataFrame

pandas.DataFrame
pd.DataFrame
DataFrame

data = {'month':[1, 2, 3], 
       'unemp_il': [5.6, 5.7, 5.8], 
       'unemp_wi': [6.1, 6.8, 6.1], 
       'gdp_il': [6, 6, 7], 
       'gdp_wi': [4, 5, 4]
       }
df = pd.DataFrame(data)

print(df)
print(df['month'])
print(df[['unemp_il', 'gdp_il']])
# Selecting one column takes a string, but selecting multiple is done with a list. 
cols = ['unemp_wi', 'gdp_wi']
print(df[cols])
# DataFrame instances have a 'columns' value that we can iterate over
print(df.columns)
print(df[[c for c in df.columns if c.endswith('wi')]])
# calculate mean
# 1) use function
import numpy as np
np.mean(df['unemp_il'])
# 2) Dataframes have their own methods
df['unemp_il'].mean()
df['unemp_il'].mean()

# slicing rows
df[1:]
df.index = ['a', 'b', 'c']

# '.loc' method for row names; '.iloc' method for row positions, first row then column
df.loc['a']
df.loc[['a', 'c']]
df.iloc[0]
df.iloc[[0, 2]]
df.loc[['a', 'c'], ['unemp_il', 'gdp_il']]
df.iloc[[0, 2], [1, 3]]

# selecting by columns
df1 = df[['unemp_il', 'gdp_il']] # just creating a view
df2 = df.loc[:, ['unemp_il', 'gdp_il']] # copy the data

# selct the data for wisconson for row 2
#df.loc[[1], ['unemp_wi']]

# operation 
df1['il_rescaled'] = df1['unemp_il'] * .01 # will raise warning
df2['il_rescaled'] = df2['unemp_il'] * .01