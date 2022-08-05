# imports
from core import Tool
import pandas as pd
reviews = pd.read_csv('https://drive.google.com/uc?export=download&id=1z-1idT4mGbOvHgmEPzneqV54EJ1-w7tk', index_col = 0)
        

#1
df1 = pd.DataFrame({'Apples' : [30], 'Bananas' : [21]})
q1 = Tool(name = 'fruits', what = 'df', object = df1)
del df1

#2
df2 = pd.DataFrame({'Apples' : [35, 41], 'Bananas' : [21, 34]}, index = ['2017 Sales', '2018 Sales'])
q2 = Tool(name = 'fruit_sales', what = 'df', object = df2)
del df2

#3
s3 = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index = ['Flour', 'Milk', 'Eggs', 'Spam'], name = 'Dinner')
q3 = Tool(name = 'ingredients', what = 'series', object = s3)
del s3

#4
df4 = pd.read_csv('https://drive.google.com/uc?export=download&id=1a1R6dr1Y1oq7f-1pvEI3x3jUdyL89qBO', index_col = 0)
q4 = Tool(name = 'fruit_sales', what = 'df', object = df4)
del df4

#5
df5 = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
q5 = Tool(name = 'cows_and_goats.csv', what = 'file', object = df5)
del df5
