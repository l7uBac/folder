import math

class Figure():
    sides_count = 0

    def __init__(self, color, *sides, filled = False):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return [*self.__color]

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if not (0 <= i <= 255 and isinstance(i, int)):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)


    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(*new_sides):
                self.__sides = new_sides




class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side, filled = False):
        super().__init__(color, side, filled = filled)
        self.radius = self.__len__() / (2 * math.pi)

    def get_square(self):
        return self.radius ** 2 * math.pi


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a = self.get_sides()
        p = 0.5 * self.__len__()
        return (p * (p - a[0]) * (p - a[1]) * (p - a[2])) ** 0.5#round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 1)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled = False):
        super().__init__(color, sides, filled = filled)
        if len(sides) == 1:
            self.__sides = [*sides] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        a = self.get_sides()
        return a[0] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())