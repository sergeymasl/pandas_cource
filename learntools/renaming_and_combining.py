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
