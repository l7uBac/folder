my_dict = {'Маша': str(1988) + 'г.р.', 'Дима': str(1988) + 'г.р.', 'Анюта': str(2019) + 'г.р.',
           'Илья': str(2009) + 'г.р.'}
print('Словарь', my_dict)
print('Маша,', my_dict['Маша'])
print(my_dict.get('папа', 'Не существующее значение'))
my_dict.update({'бабушка': str(1954) + 'г.р.',
                'дедушка': str(1953) + 'г.р.'})
a = my_dict.pop('Илья')
print('Удаленное значение - Илья,', a)
print(my_dict)
my_set = {'dad', 'mam', 5 > 8, False, 1, 1, 2, 1, 2, 'dad', 'mam'}
print(my_set)
my_set.update({'Petya', 'Yasya'})
my_set.remove(False)
print(my_set)
