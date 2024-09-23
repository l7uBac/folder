class Vehicle:

    __COLOR_VARIANTS = []

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner                     # владелец транспорта
        self.__model = __model                 # модель(марка)
        self.__engine_power = __engine_power   # мощность двигателя
        self.__color = __color                 # цвет



    def get_model(self):
        return f' Модель: {self.__model}'
    # возвращает   строку: "Модель: <название модели транспорта>"

    def get_horsepower(self):
        return f' Мощность двигателя: {self.__engine_power}'
    # возвращает  строку: "Мощность двигателя: <мощность>"

    def get_color(self):
        return f' Цвет: {self.__color}'
    # возвращает    строку: "Цвет: <цвет транспорта>"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f' Владелец: {self.owner}')
    # распечатывает  результаты    методов(в    том    же    порядке): get_model, get_horsepower, get_color;
    # а    так    же    владельца    в    конце    в    формате    "Владелец: <имя>"

    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color.lower() in self.__COLOR_VARIANTS or self.new_color.upper() in self.__COLOR_VARIANTS:
            self.__color == self.new_color
        else:
            print(f' Нельзя сменить цвет на {self.new_color}')
    # принимает    аргумент    new_color(str), меняет    цвет    __color
    # на    new_color, если    он    есть    в    списке    __COLOR_VARIANTS, в    противном    случае    выводит
    # на    экран    надпись: "Нельзя сменить цвет на <новый цвет>".

class Sedan(Vehicle):
    pass

__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()