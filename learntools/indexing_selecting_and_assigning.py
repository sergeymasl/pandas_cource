# imports
from core import Tool
import pandas as pd
reviews = pd.read_csv('https://drive.google.com/uc?export=download&id=1z-1idT4mGbOvHgmEPzneqV54EJ1-w7tk', index_col = 0)

#1
df1 = reviews['description']
q1 = Tool(name = 'desc', what = 'series', object = df1)
del df1

#2
df2 = reviews.loc[0, 'description']
q2 = Tool(name = 'first_description', what = 'df', object = df2)
del df2

#3
df3 = reviews.iloc[0]
q3 = Tool(name = 'first_row', what = 'df', object = df3)
del df3

#4
df4 = reviews.loc[:9, 'description']
q4 = Tool(name = 'first_descriptions', what = 'df', object = df4)
del df4

#5
df5 = reviews.iloc[[1,2,3,5,8]]
q5 = Tool(name = 'sample_reviews', what = 'df', object = df5)
del df5

#6
df6 = reviews.loc[[0,1,10,100], ['country', 'province', 'region_1', 'region_2']]
q6 = Tool(name = 'df', what = 'df', object = df6)
del df6

#7
df7 = reviews.loc[:99, ['country', 'variety']]
q7 = Tool(name = 'first_rows', what = 'df', object = df7)
del df7

#8
df8 = reviews.loc[reviews['country'] == 'Italy']
q8 = Tool(name = 'italian_wines', what = 'df', object = df8)
del df8

#9
df9 = reviews.loc[(reviews['points'] >= 95) & reviews['country'].isin([]) >= 95]
q9 = Tool(name = 'top_oceania_wines', what = 'df', object = df9)
del df9
