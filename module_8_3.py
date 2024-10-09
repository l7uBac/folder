
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        # 'Некорректный тип vin номер'
        # 'Неверный диапазон для vin номера'

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
    # 'Некорректный тип данных для номеров'
    # 'Неверная длина номера'

class Car():

    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self.__is_valid_numbers(__numbers):
            self.__numbers = __numbers


    def __is_valid_vin(self, vin_number):
        if vin_number not in range(1000000, 9999999+1):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        else:
            return True



    def __is_valid_numbers(self, __numbers):
        __numbers = __numbers
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')