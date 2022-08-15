# imports
from core import Tool
import pandas as pd
reviews = pd.read_csv('https://drive.google.com/uc?export=download&id=1z-1idT4mGbOvHgmEPzneqV54EJ1-w7tk', index_col = 0)


#1
name_var = 'dtype'
var = reviews['points'].dtype
what = 'single_value'
hint = 'Используйте метод `gf`dtype`n`'
solution = "dtype = reviews['points'].dtype"
q1 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#2
name_var = 'point_strings'
var = reviews['points'].astype('str')
what = 'series'
hint = 'Используйте метод `gf`astype`n`'
solution = "point_strings = reviews['points'].astype('str')"
q2 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#3
name_var = 'n_missing_prices'
var = reviews['price'].isnull().sum()
what = 'single_value'
hint = 'Используйте метод `gf`isnull()`n` и `gf`sum()`n`'
solution = "n_missing_prices = reviews['price'].isnull().sum()"
q3 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#4
name_var = 'reviews_per_region'
var = reviews['region_1'].fillna('Unknown').value_counts().sort_values(ascending = False)
what = 'series'
hint = 'Используйте методы `gf`fillna()`n`, `gf`value_counts()`n` и `gf`sort_values()`n`'
solution = "reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)"
q4 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)
