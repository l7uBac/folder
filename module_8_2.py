def personal_sum(*args):
    result = 0
    incorrect_data = 0
    for i in args:
        for j in i:
            try:
                result += j
            except TypeError as e:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {j}')
    return result, incorrect_data


def calculate_average(*args):
    if isinstance(*args, int):
        print(f'В numbers записан некорректный тип данных')
        return None
    sr_arif = personal_sum(*args)
    try:
        return (sr_arif[0]/(len(*args) - sr_arif[1]))
    except ZeroDivisionError:
        return 0



print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать