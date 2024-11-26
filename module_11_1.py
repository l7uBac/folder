import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time

# !pandas!
# В библиотеке pandas определены два класса объектов для работы с данными:
# Series — одномерный массив, который может хранить значения любого типа данных;
# DataFrame — двумерный массив (таблица), в котором столбцами являются объекты класса Series.

"""students_marks_dict = {"Студент": ["Иван", "Алена", "Алексей", "Константин", "Георгий", "Дмитрий", "Анатолий", "Светлана"],
                       "Возраст" : [15, 20, 22, 32, 16, 21, 21, 15],
                       "Пол": ["мужской", "женский", "мужской", "мужской", "мужской", "мужской", "мужской", "женский"],
                       "Тест_Алгебра": [5, 3, 4, 5, 4.5, 5, 3, 4],
                       "Тест_Физика": [4, 5, 10/2, 5, 3.5, 4.5, 3, 5]}
students = pd.DataFrame(students_marks_dict) # Создаем объект класса DataFrame состоящий из столбцов (класс Series).
print()
print(students)
print()
print(type(students)) # Проверяем тип объекта DataFrame.
print(type(students["Студент"])) # Проверяем тип объекта Series.
print()
# У объекта класса DataFrame есть индексы по строкам (index) и столбцам (columns):
print(students.index) # Индекс по строкам.
print(students.columns) # Индекс по столбцам.
print()
students.index = [1,2,3,4,5,6,7,8] # задаем порядок индексов - не с "0" а с "1" (также можно использовать "А","В","С"...)
print(students[2:4]) # Получаем срез

students.to_csv('students_marks_dict.csv', index=False) # Создание файла.
students = pd.read_csv('students_marks_dict.csv')  # Чтение файла.
print()
sort = students[students["Пол"] == "мужской"]
print(sort[["Студент", "Возраст"]].head()) # Отсортировали мужской пол и вывели их возраст
print()
scores = students.assign(Средний_бал=lambda x: (x["Тест_Алгебра"] + x["Тест_Физика"])/2) # Добавил столбец "Средний бал" в таблицу,
                                                                                         # в процессе добавления столбца создается новая таблица,
                                                                                         # а не изменяется старая.
scores.to_csv("scores.csv", index=False)
print(scores)
"""
#
# # !numpy!
# # Программы на Python могут быть такими же быстрыми, как и программы, созданные на компилируемых языках.
# # Существенную прибавку в скорости обеспечивает библиотека numpy (Numerical Python, читается как «нампАй»).
# # Библиотека numpy частично написана на языках С и «Фортран», благодаря чему и работает быстро.
# # Таким образом, numpy сочетает в себе вычислительную мощность языков С и «Фортран» и простоту синтаксиса Python.
#
# print()
# a = np.array([1, 2, 3])  # создание массива из списка
# print(f'Массив a: \n{a}\n')
#
# b = np.zeros((4, 3), dtype="int8")  # создание массива заполненное нулями ((строки, столбцы))
# print(f'Массив b: \n{b}\n')
#
# # Массивы numpy являются объектами класса ndarray. Наиболее важными атрибутами класса ndarray являются:
# # ndarray.ndim — размерность (количество осей) массива;
# # ndarray.shape — кортеж, значения которого содержат количество элементов по каждой из осей массива;
# # ndarray.size — общее количество элементов массива;
# # ndarray.dtype — объект, описывающий тип данных элементов массива;
# print(f"a.ndim = {a.ndim}, a.shape = {a.shape}, a.size = {a.size}, a.dtype = {a.dtype}")
# print(f"b.ndim = {b.ndim}, b.shape = {b.shape}, b.size = {b.size}, b.dtype = {b.dtype}\n")
#
# t = time()
# print(f"Результат итератора: {sum(x ** 0.5 for x in range(10 ** 7))}.")
# print(f"{time() - t} с.") # Скорость подсчета итератора суммы квадратных корней
# t = time()
# print(f"Результат numpy: {np.sqrt(np.arange(10 ** 7)).sum()}.")
# print(f"{time() - t} с.") # Скорость подсчета "нампАй" суммы квадратных корней
#
#
# !Matplotlib! это библиотека для рисования графиков и диаграмм на языке Python. Она помогает визуализировать данные,
# что бы их было легче понять. Например, если у вас есть данные о росте и весе людей, вы можете построить график,
# что бы увидеть, как они связаны.
df = pd.read_csv('scores.csv')                                #считываем файл
df["Возраст"].value_counts().plot(kind='bar', ylabel='Кол-во')# сортируем студентов по возрасту
plt.show()                                                    # выводим график
v1 = df.groupby("Пол")["Возраст"].value_counts()              # сохраняем в новую переменную отсортированные данные таблицы по студентам
v1.unstack(0).plot(kind='bar', ylabel='Кол-во')               # создаем график
plt.show()                                                    # визуализируем график
# Линейный график
x = [1, 2, 3, 4, 5]        # координаты по осям х и у
y = [25, 32, 34, 20, 25]
plt.plot(x, y)       # передаем координаты точек на график
plt.xlabel('Ось х')        # Подпись для оси х
plt.ylabel('Ось y')        # Подпись для оси y
plt.title('Первый график') #Название
plt.show()                 # визуализируем наш график


# Круговая диаграмма
vals = df["Возраст"]   # записываем в переменную возраст студентов
labels = df["Студент"] # Записываем имена

plt.pie(vals, labels=labels) # создаем круговую диаграмму на основе переданных данных записанных в переменную.
                             # (autopct='%1.1f%%') - в процентном соотношении показывает
plt.title("Возраст студентов")
plt.show()