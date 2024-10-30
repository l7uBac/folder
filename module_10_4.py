from random import randint
from time import sleep
from threading import Thread
from queue import Queue

class Table:

    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        n = randint(3, 10)

        sleep(1)


class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables


    def guest_arrival(self, *guests):
        for guest in guests:
            flag = False
            for table in self.tables:
                if table.guest is None:
                    print(f'{guest.name} сел(-а) за стол номер {table.number}.')
                    guest.start()
                    guest.join()
                    table.guest = guest
                    flag = True
                    break
            if not flag:
                print(f'{guest.name} в очереди.')
                self.queue.put(guest)

    def discuss_guests(self):
        







            

#
#     #
#     #
#     # def discuss_guests(self):
#     #     while not empty.quele():
#
#
#
# # Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
# #cafe.discuss_guests()