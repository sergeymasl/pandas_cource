class Tool:
  '''
  Касс для проверки ответов на упражнения
  Методы:
  check - проверка упражнения
  hint - вывод подсказки для упражнения если она есть, доступен после 3 проверок
  soluthion - решение, доступно после 5 проверок
  '''

  def __init__(self, name, what, object, hint = None, solution = None):
    '''
    При инициализация передаем датафрейм или серию, в зависимости от проверяемого объекта
    
    name - имя переменной которую проверяем
    object - переменная которая соответсвует правильному ответу
    what - что проверяем ['df', 'series', 'file', 'single_value']
    hint - текст подсказки для упражнеия (текст в формате `r`- красный и т.д.)
    solution - текст решения упражнения (текст в формате `r`- красный и т.д.)
    '''
    
    # присвоение атрибутов
    self.name = name
    self.what = what
    self._hint = hint
    self._solution = solution
    
    if what == 'series':
      self.series = object 
    
    if what in ['df', 'file']:
      self.df = object
    
    if what in ['single_value']:
      self.var = object
     
    # обявляем счетчик попыток проверок
    self.counter_check = 0
  
  def color_text(text):
  '''
  Функция для легкого изменения цвета и заливки текста.

  Параметры в text:
  `n` - с этого момента начинается нормальный текст
  `r` - с этого момента начинается красный текст
  `g` - с этого момента начинается зеленый цвет
  `b` - с этого момента начинается голубой цвет
  `gf` - c этого момента начинается серая заливка

  Ссылка на параметры изменения цвета: https://habr.com/ru/company/macloud/blog/558316/
  '''
  var = text
  var = var.replace('`n`' , '\033[0m')
  var = var.replace('`r`' , '\033[1;31m')
  var = var.replace('`g`' , '\033[1;32m')
  var = var.replace('`b`' , '\033[1;34m')
  var = var.replace('`gf`' , '\033[48;5;252m')
  return var

  def check(self, check_obj = None):
    '''
    Проверка задания
    '''
    # при активации увеличиваем счетчик
    self.counter_check +=1
    
    # =====================================================series==========================================================
    if self.what == 'series':
      
      correct = True

      # 1 проверяем есть ли переменная
      #if not self.name in globals():
      #  # сообщаем об ошибке
      #  print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вам необходимо создать переменную', self.name))
      #  print()
      #  correct = False
      
      # 2 проверяем тип переменной
      if correct:
        if not isinstance(check_obj, type(self.series)):
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'ваша переменная имеет формат', type(check_obj), 'а должна быть', type(self.series)))
          print()
          correct = False
      
      # 3 проверяем название series
      if correct:
        # сначала смотрим есть ли вообще название
        if self.series.name:
          # проверяем соответсвие имени
          if check_obj.name:
            if check_obj.name != self.series.name:
              print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {}\033[48;5;252m{}'.format('Промах :', 'вы не верно задали name для Series, ваш name -', check_obj.name, 'необходимое name - ', self.series.name))
              print()
              correct = False
          # если у проверяемой серии нет имени
          else:
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вы не задали name для Series, вам необходимо задать name:', self.series.name))
            print()
            correct = False
      
      # 4 проверим количество строк
      if correct:
        if self.series.shape[0] != check_obj.shape[0]:
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'не соответствует количество строк. Требуемое количество строк:', self.series.shape[0], 'Обнаружено:', check_obj.shape[0]))
          print()
          correct = False
      
      # 5 проверим индексы
      if correct:
        if not self.series.index.equals(check_obj.index):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, индексы в вашей Series, они отличаются от требуемых'))
          print()
          correct = False
      
      # 6 проверяем на соответсвие сами Series
      if correct:
        if not self.series.equals(check_obj):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, значения в вашей Series, они отличаются от требуемых'))
          print()
          correct = False
      
      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))
        print()
      
    # =====================================================dataframe==========================================================
    elif self.what == 'df':

      correct = True

      # 1 проверяем есть ли переменная
      #if not self.name in globals():
      #  # сообщаем об ошибке
      #  print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вам необходимо создать переменную', self.name))
      #  print()
      #  correct = False
      
      # 2 проверяем тип переменной
      if correct:
        if not isinstance(check_obj, type(self.df)):
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'ваша переменная имеет формат', type(check_obj), 'а должна быть', type(self.df)))
          print()
          correct = False
      
      # 3 проверяем столбцы
      if correct:
        if not self.df.columns.equals(check_obj.columns):
          
          # если столбцов в проверяемой больше
          if len(self.df.columns) < len(check_obj.columns):
            # список столбцов который есть в проверяемом массиве, но нет в эталонном
            list_of_columns = list(set(self.df.columns) ^ set(check_obj.columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вы имеете больше столбцов чем необходимо, неизвестные столбцы:', list_of_columns))
            print()
          
          # если столбцов меньше
          elif len(self.df.columns) > len(check_obj.columns):
            list_of_columns = list(set(self.df.columns) ^ set(check_obj.columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}'.format('Промах :', 'вы имеете меньше столбцов чем необходимо, недостющие столбцы:', list_of_columns))
            print()
          
          # если одинаковое количество столбцов, но различаются названия
          else:
            print('\033[1;31m{} \033[0m{}'.format('Промах :', 'названия столбцов или их порядок различаются, пожалуйста, проверьте названия или порядок столбцов'))
            print()
          correct = False

      # 4 проверим количество строк
      if correct:
        if self.df.shape[0] != check_obj.shape[0]:
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'не соответствует количество строк. Требуемое количество строк:', self.df.shape[0], 'Обнаружено:', check_obj.shape[0]))
          print()
          correct = False

      # 5 проверяем индексы
      if correct:
        if not self.df.index.equals(check_obj.index):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, индексы в вашем DataFrame, они отличаются от требуемых'))
          print()
          correct = False
      
      # 6 проверяем сами значения в датафрейме
      if correct:
        if not self.df.equals(check_obj):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, значения в вашем DataFrame, они отличаются от требуемых'))
          print()
          correct = False
      
      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))
        print()
    
    # =====================================================file==========================================================
    if self.what == 'file':

      from glob import glob
      import pandas as pd
      
      correct = True

      # 1 проверяем наличие файла
      if not self.name in glob('*'):
        print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {}'.format('Промах :', 'файл c именем', self.name, 'не найден'))
        print()
        correct = False

      if correct:
        # считываем сам датафрейм для проверки
        check_df = pd.read_csv(self.name, index_col = 0)

      # 2 проверяем столбцы
      if correct:
        if not self.df.columns.equals(check_df.columns):
          
          # если столбцов в проверяемой больше
          if len(self.df.columns) < len(check_df.columns):
            # список столбцов который есть в проверяемом массиве, но нет в эталонном
            list_of_columns = list(set(self.df.columns) ^ set(check_df.columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'в датафрейме загруженном из', self.name, 'столбцов больше, чем необходимо, неизвестные столбцы:', list_of_columns))
            print()
          
          # если столбцов меньше
          elif len(self.df.columns) > len(check_df.columns):
            list_of_columns = list(set(self.df.columns) ^ set(check_df.columns))
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'в датафрейме загруженном из', self.name, 'столбцов меньше, чем необходимо, недостающие столбцы:', list_of_columns))
            print()
          
          # если одинаковое количество столбцов, но различаются названия
          else:
            print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {}'.format('Промах :', 'в датафрейме загруженном из', self.name, 'названия столбцов или их порядок различаются, пожалуйста, проверьте названия или порядок столбцов'))
            print()
          correct = False
        
      # 3 проверим количество строк
      if correct:
        if self.df.shape[0] != check_obj.shape[0]:
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'не соответствует количество строк. Требуемое количество строк:', self.df.shape[0], 'Обнаружено:', check_obj.shape[0]))
          print()
          correct = False
      
      # 4 проверяем сами значения в датафрейме
      if correct:
        if not self.df.equals(check_df):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, значения в вашем DataFrame, они отличаются от требуемых'))
          print()
          correct = False

      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))
        print()
    
    # =====================================================single_value==========================================================

    if self.what == 'single_value':

      correct = True

      # 1 проверяем тип переменной
      if correct:
        if not isinstance(check_obj, type(self.var)):
          print('\033[1;31m{} \033[0m{} \033[48;5;252m{}\033[0m {} \033[48;5;252m{}'.format('Промах :', 'ваша переменная имеет формат', type(check_obj), 'а должна быть', type(self.var)))
          print()
          correct = False
      
      # 2 проверяем сами значения
      if correct:
        if self.var != check_obj:
          print('\033[1;31m{} \033[0m{}\033[48;5;252m{}\033[0m {}'.format('Промах :', 'проверьте, пожалуйста, значения в переменной ', self.name, ', они отличаются от требуемых'))
          print()
          correct = False
      
      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))
        print()
  
  def hint(self):
    '''Подсказка, которая откроется через 3 попытки проверки ответа'''
    # проверяем предусмотрена ли подсказка
    if self._hint:
      # смотрим на счетчик, печатаем подсказку только после 3 попытки
      if self.counter_check < 3:
        print(color_text('`b`Подсказка:`n` подсказка будет доступна после 3 попыток проверки ответа (пробуйте решить самостоятельно)'))
      else:
        print(color_text(f'`b`Подсказка:`n` {self._hint}'))
    else:
      print(color_text('`b`Подсказка:`n` автор не предусмотрел подсказки для этого упражнения'))
  
  def solution(self):
    '''Решение, которое откроется через 5 попыток проверки ответа'''
    if self._solution:
      # смотрим на счетчик, печатаем подсказку только после 5 попытки
      if self.counter_check < 5:
        print(color_text('`b`Решение:`n` решение будет доступно после 5 попыток проверки ответа (пробуйте решить самостоятельно)'))
      else:
        print(color_text(f'''`b`Решение:`n` 
        {self._solution}'''))
    else:
      print(color_text('`b`Решение: `n` автор не предусмотрел решение для этого упражнения'))
