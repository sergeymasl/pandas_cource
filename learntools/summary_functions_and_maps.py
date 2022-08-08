# imports
from core import Tool
import pandas as pd
reviews = pd.read_csv('https://drive.google.com/uc?export=download&id=1z-1idT4mGbOvHgmEPzneqV54EJ1-w7tk', index_col = 0)

#1
name_var = 'median_points'
var = reviews['points'].median()
what = 'single_value'
hint = None
solution = None
q1 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#2
name_var = 'countries'
var = reviews['country'].unique()
what = 'array'
hint = None
solution = None
q2 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#3
name_var = 'reviews_per_country'
var = reviews['country'].value_counts()
what = 'series'
hint = None
solution = None
q3 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#4
name_var = 'centered_price'
price_mean = reviews['price'].mean()
var = reviews['price'].map(lambda x: x - price_mean)
what = 'series'
hint = None
solution = None
q4 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#5
name_var = 'centered_price'
bargain_idx = (reviews.points / reviews.price).idxmax()
var = reviews.loc[bargain_idx, 'title']
what = 'single_value'
hint = None
solution = '''
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
'''
q5 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#6
name_var = 'descriptor_counts'
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
var = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
what = 'series'
hint = 'Используйте метод `gf`map`n` для проверки нахождения слова `gf`tropical`n` затем сложите все `gf`True`n`, повторите это для `gf`fruity`n`. Затем соедините эти выражения в `gf`Series' 
solution = '''
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
'''
q6 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)


#7
name_var = 'descriptor_counts'

def stars(row):
    if row['country'] == 'Canada':
        return 3
    elif row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1
var = reviews.apply(stars, axis='columns')
what = 'series'
hint = 'Напишите собственную функцию затрагивающую два столбца и возвращяющую количество звезд. Затем используйте `gf`DataFrame.apply`n` для обработки каждой строки' 
solution = '''
def stars(row):
    if row['country'] == 'Canada':
        return 3
    elif row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
'''
q6 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)
