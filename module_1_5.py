immutable_var = 1, 'Джон', 2, 'Уик', 9 / 3, '9 ярдов', 5 > 2
print(immutable_var)
# immutable_var[0] = 10 - строка вызвала ошибку, сделал ее комментарием. Ошибка, потому что в данном кортеже нет изменямых данных
mutable_list = ['9 с половиной ярдов'], 2024, 9 < 2, 5 - 2
print(mutable_list)
mutable_list[0][0] = str(1988)
print(mutable_list)
