import math

class Figure():
    sides_count = 0

    def __init__(self, color, *sides, filled = False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        # for i in (r, g, b):
        #     if 0 <= i <= 255 and isinstance(i, int):
        #         return True
        # return False
        range = 0<=r<=255 and 0<=g<=255 and 0<=b<=255
        type = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return range and type


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)


    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides




class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side, filled = False):
        super().__init__(color, side, filled=filled)
        self.radius = side / (2 * math.pi)

    def get_square(self):
        return self.radius ** 2 * math.pi


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        # #a, b, c == self.get_sides()
        p = 0.5 * self.__len__()
        return (p * (p - self.get_sides[0]) * (p - self.get_sides[1]) * (p - self.get_sides[2])) ** 0.5 #(p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    pass




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
print(circle1.get_color())
#cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
#cube1.set_color(300, 70, 15) # Не изменится
#print(cube1.get_color())

# Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
#print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
#print(cube1.get_volume())
triangle1 = Triangle((0, 0, 0), 3, 3, 3)
triangle1.get_square()