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
            for table in self.tables:
                if table.guest is None:
                    print(f'{guest.name} сел(-а) за стол номер {table.number}.')
                    guest.start()
                    table.guest = guest
                    break
            else:
                print(f'{guest.name} в очереди.')
                self.queue.put(guest)

    def discuss_guests(self):
        while (not self.queue.empty() or table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен.')
                        table.guest = None
                        if not self.queue.empty() and table.guest is None:
                            table.guest = self.queue.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.')
                            table.guest.start()

# Создание столов
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
cafe.discuss_guests()