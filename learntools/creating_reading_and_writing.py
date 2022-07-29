class Tool:
  '''
  Касс для проверки ответов на упражнения
  '''

  def __init__(self, name, what, object):
    '''
    При инициализация передаем датафрейм или серию, в зависимости от проверяемого объекта
    
    name - имя переменной которую проверяем
    df - датафрейм если проверяем датафрейм
    object - датафрейм или серия которая соответствует правильному ответу
    what - что проверяем ['df', 'series', 'file']
    '''
    self.name = name
    self.what = what

    if what == 'series':
      self.series = object 
    
    if what == 'df' or what == 'file':
      self.df = object


  def check(self):
    '''
    Проверка задания
    '''
    # series
    if self.what == 'series':
      
      correct = True

      # 1 проверяем есть ли переменная
      if not self.name in globals():
        # сообщаем об ошибке
        print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вам необходимо создать переменную', self.name))
        correct = False
      
      # 2 проверяем тип переменной
      if correct:
        if not isinstance(globals()[self.name], type(self.series)):
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'ваша переменная имеет формат', type(globals()[self.name]), 'а должна быть', type(self.series)))
          correct = False
      
      # 3 проверяем название series
      if correct:
        # сначала смотрим есть ли вообще название
        if self.series.name:
          # проверяем соответсвие имени
          if globals()[self.name].name:
            if globals()[self.name].name != self.series.name:
              print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {}\033[48;5;252m{}'.format('Промах :', 'вы не верно задали name для Series, ваш name -', globals()[self.name].name, 'необходимое name - ', self.series.name))
              correct = False
          # если у проверяемой серии нет имени
          else:
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вы не задали name для Series, вам необходимо задать name:', self.series.name))
            correct = False
      
      # 4 проверим индексы
      if correct:
        if not self.series.index.equals(globals()[self.name].index):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, индексы в вашей Series, они отличаются от требуемых'))          
          correct = False
      
      # 5 проверяем на соответсвие сами Series
      if correct:
        if not self.series.equals(globals()[self.name]):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, значения в вашей Series, они отличаются от требуемых'))
          correct = False
      
      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))
      
    # dataframe
    elif self.what == 'df':

      correct = True

      # 1 проверяем есть ли переменная
      if not self.name in globals():
        print('Ушел в проверку переменной')
        print(globals())
        # сообщаем об ошибке
        print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вам необходимо создать переменную', self.name))
        correct = False
      
      # 2 проверяем тип переменной
      if correct:
        if not isinstance(globals()[self.name], type(self.df)):
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'ваша переменная имеет формат', type(globals()[self.name]), 'а должна быть', type(self.df)))
          correct = False
      
      # 3 проверяем столбцы
      if correct:
        if not self.df.columns.equals(globals()[self.name].columns):
          
          # если столбцов в проверяемой больше
          if len(self.df.columns) < len(globals()[self.name].columns):
            # список столбцов который есть в проверяемом массиве, но нет в эталонном
            list_of_columns = list(set(self.df.columns) ^ set(globals()[self.name].columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вы имеете больше столбцов чем необходимо, неизвестные столбцы:', list_of_columns))
          
          # если столбцов меньше
          elif len(self.df.columns) > len(globals()[self.name].columns):
            list_of_columns = list(set(self.df.columns) ^ set(globals()[self.name].columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вы имеете меньше столбцов чем необходимо, недостющие столбцы:', list_of_columns))
          
          # если одинаковое количество столбцов, но различаются названия
          else:
            print('\033[1;31m{} \033[0m{}'.format('Промах :', 'названия столбцов различаются, пожалуйста, проверьте названия столбцов'))
          correct = False
      
      # 4 проверяем индексы
      if correct:
        if not self.df.index.equals(globals()[self.name].index):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, индексы в вашем DataFrame, они отличаются от требуемых'))          
          correct = False
      
      # 5 проверяем сами значения в датафрейме
      if correct:
        if not self.df.equals(globals()[self.name]):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, значения в вашем DataFrame, они отличаются от требуемых'))
          correct = False
      
      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))
    
    # file
    if self.what == 'file':

      from glob import glob
      import pandas as pd
      
      correct = True

      # 1 проверяем наличие файла
      if not self.name in glob('*'):
        print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {}'.format('Промах :', 'файл c именем', self.name, 'не найден'))
        correct = False

      if correct:
        # считываем сам датафрейм для проверки
        check_df = pd.read_csv(self.name, index_col = 0)
        print()

      # 2 проверяем столбцы
      if correct:
        if not self.df.columns.equals(check_df.columns):
          
          # если столбцов в проверяемой больше
          if len(self.df.columns) < len(check_df.columns):
            # список столбцов который есть в проверяемом массиве, но нет в эталонном
            list_of_columns = list(set(self.df.columns) ^ set(check_df.columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'в датафрейме загруженном из', self.name, 'столбцов больше, чем необходимо, неизвестные столбцы:', list_of_columns))
          
          # если столбцов меньше
          elif len(self.df.columns) > len(check_df.columns):
            list_of_columns = list(set(self.df.columns) ^ set(check_df.columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'в датафрейме загруженном из', self.name, 'столбцов меньше, чем необходимо, недостающие столбцы:', list_of_columns))
          
          # если одинаковое количество столбцов, но различаются названия
          else:
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {}'.format('Промах :', 'в датафрейме загруженном из', self.name, 'названия столбцов различаются, пожалуйста, проверьте названия столбцов'))
          correct = False
      
      # 3 проверяем сами значения в датафрейме
      if correct:
        if not self.df.equals(check_df):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, значения в вашем DataFrame, они отличаются от требуемых'))
          correct = False

      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))

        
        
import pandas as pd
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
