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
    
    if what == 'df':
      self.df = df


  def check(self):
    '''
    Проверка задания
    '''
    # series
    if self.what == 'series':
      
      correct = True

      # 1 проверяем есть ли переменная
      if self.name not in globals():
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
      if self.name not in globals():
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
