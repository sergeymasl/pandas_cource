# imports
from core import Tool
import pandas as pd
reviews = pd.read_csv('https://drive.google.com/uc?export=download&id=1z-1idT4mGbOvHgmEPzneqV54EJ1-w7tk', index_col = 0)
games_products = pd.read_csv('https://drive.google.com/uc?export=download&id=1Dcm3D9ZllWpgtPpkb_hh-C-pLvE9W7uV')
games_products['subreddit'] = 'r/gaming'
movies_products = pd.read_csv('https://drive.google.com/uc?export=download&id=1otcaCQ_6cmVHB0HBupsqHdyCqEfkm7Gi')
movies_products['subreddit'] = 'r/movies'


#1
name_var = 'renamed'
var = reviews.rename(columns = {'region_1' : 'region', 'region_2' : 'locale'})
what = 'df'
hint = "Используйте метод `gf`rename()`n`"
solution = "renamed = reviews.rename(columns = {'region_1' : 'region', 'region_2' : 'locale'})"
q1 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#2
name_var = 'combined_products'
var = pd.concat([games_products, movies_products])
what = 'df'
hint = "Используйте метод `gf`concat()`n`"
solution = "combined_products = pd.concat([games_products, movies_products])"
q2 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)
