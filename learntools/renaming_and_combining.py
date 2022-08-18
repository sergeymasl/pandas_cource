# imports
from core import Tool
import pandas as pd
reviews = pd.read_csv('https://drive.google.com/uc?export=download&id=1z-1idT4mGbOvHgmEPzneqV54EJ1-w7tk', index_col = 0)


#1
name_var = 'renamed'
var = reviews.rename(columns = {'region_1' : 'region', 'region_2' : 'locale'})
what = 'df'
hint = "Используйте метод `gf`rename()`n`"
solution = "renamed = reviews.rename(columns = {'region_1' : 'region', 'region_2' : 'locale'})"
q1 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#2
name_var = 'renamed'
var = reviews.rename(columns = {'region_1' : 'region', 'region_2' : 'locale'})
what = 'df'
hint = "Используйте метод `gf`rename()`n`"
solution = "renamed = reviews.rename(columns = {'region_1' : 'region', 'region_2' : 'locale'})"
q2 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)
