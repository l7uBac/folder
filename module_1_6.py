my_dict = {'Маша': 1988, 'Дима': 1988, 'Анюта': 2019, 'Илья': 2009}
print(my_dict)
print(my_dict['Маша'])
print(my_dict.get('папа'))
my_dict.update({'бабушка': 1954,
                'дедушка': 1953})
a = my_dict.pop('Илья')
print(a)
print(my_dict)
my_set = {'dad', 'mam', 5 > 8, False, 1, 1, 2, 1, 2, 'dad', 'mam'}
print(my_set)
my_set.update({'Petya', 'Yasya'})
my_set.remove(False)
print(my_set)