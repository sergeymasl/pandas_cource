class Tool:
  '''
  Касс для проверки ответов на упражнения
  '''

  def __init__(self, name, df = None, series = None, file = False):
    '''
    При инициализация передаем датафрейм или серию, в зависимости от проверяемого объекта
    
    name - имя переменной которую проверяем
    df - датафрейм если проверяем датафрейм
    series - если проверяем серию
    file - если проверяем сохранение файла
    '''
    self.name = name
    self.df = df
    self.series = series
    self.file = False

  def check(self):
    '''
    Проверка задания
    '''
    # сначала наименование переменной
    if self.series.all():
      
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
      
      # 3 проверяе название series
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
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, индексы в вашей Series'))          
          correct = False
      
      # 5 проверяем на соответсвие сами Series
      if correct:
        if not self.series.equals(globals()[self.name]):
          print('\033[1;31m{} \033[0m{}'.format('Промах :', 'проверьте, пожалуйста, значения в вашей Series'))
          correct = False
      
      # и НАКОНЕЦ если все проверки пройдены говорим о том что все отлично
      if correct:
        print('\033[1;32m{}'.format('Отлично, все верно'))
