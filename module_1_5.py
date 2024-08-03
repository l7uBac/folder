immutable_var = 1, ',white', 2, 'bytes', 9 / 3, '9 ярдов', 5 > 2
print(immutable_var)
# immutable_var[0] = 10 - строка вызвала ошибку, сделал ее комментарием. Ошибка, потому что нет изменяемых данных.
mutable_list = ['9 с половиной', 9.5], 2024, 9 < 2, 5 - 2
print(mutable_list)
mutable_list[0][0] = str(1988)
print(mutable_list)
