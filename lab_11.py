import pandas as pd

#combine these three dataframes so that the result is a single
#dataframe with the columns "date", "place", "value1", "value2",
#with the date columns being datetime objects that run from
#1/2020 to 10/2021, without modifying any starter code

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                 '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

data3 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

df1 = df1.melt(id_vars = 'date', value_vars = None, var_name = 'place', value_name = 'value1')
df2 = df2.melt(id_vars = 'date', value_vars = None, var_name = 'place', value_name = 'value2')
df1['date'] = pd.to_datetime(df1['date'])
df2['date'] = pd.to_datetime(df2['date'])
df3['date'] = pd.to_datetime(df3['date'])
df_1and3 = pd.concat([df1, df3])
df = df_1and3.merge(df2, on=['date', 'place'], how='outer', indicator=True)
assert(all(df['_merge'] == 'both')), 'Nope!'
df = df.drop('_merge', axis=1)