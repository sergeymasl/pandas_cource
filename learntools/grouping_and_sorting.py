# imports
from core import Tool
import pandas as pd
reviews = pd.read_csv('https://drive.google.com/uc?export=download&id=1z-1idT4mGbOvHgmEPzneqV54EJ1-w7tk', index_col = 0)

#1
name_var = 'reviews_written'
var = reviews.groupby(by = 'taster_twitter_handle')['description'].count()
what = 'series'
hint = "Используйте `gf`groupby`n` по рецензентам, а затем `gf`count()`n` для столбца с рецензиями"
solution = "reviews_written = reviews.groupby(by = 'taster_twitter_handle')['description'].count()"
q1 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#2
name_var = 'best_rating_per_price'
var = reviews.groupby('price')['points'].max().sort_index()
what = 'series'
hint = "Используйте `gf`max()`n` и `gf`sort_index()`n`. Столбец с ценой - `gf`price`n`, столбец с оценками - `gf`points`n`"
solution = "best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()"
q2 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#3
name_var = 'price_extremes'
var = reviews.groupby('variety')['price'].agg([min, max])
what = 'df'
hint = "Используйте `gf`agg()`n`"
solution = "price_extremes = reviews.groupby('variety')['price'].agg([min, max])"
q3 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#4
name_var = 'sorted_varieties'
var = reviews.groupby('variety')['price'].agg([min, max]).sort_values(by=['min', 'max'], ascending = False)
what = 'df'
hint = "Используйте `gf`sort_values()`n` и передайте в параметр `gf`by`n` список столбцов по которым нужно отсортировать DataFrame"
solution = "sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending = False)"
q4 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#5
name_var = 'reviewer_mean_ratings'
var = reviews.groupby('taster_name')['points'].mean()
what = 'series'
hint = "Используйте `gf`mean()`n`"
solution = "reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()"
q5 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)

#6
name_var = 'country_variety_counts'
var = reviews.groupby(by = ['country', 'variety']).size().sort_values(ascending = False)
what = 'series'
hint = "Используйте `gf`groupby()`n` по двум столбцам. А затем `gf`size()`n` и `gf`sort_values()`n`"
solution = "country_variety_counts = reviews.groupby(by = ['country', 'variety']).size().sort_values(ascending = False)"
q6 = Tool(name = name_var, what = what, object = var, hint = hint, solution = solution)
