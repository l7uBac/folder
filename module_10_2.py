from threading import Thread
import time

class Knight(Thread):
    unit = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.unit > 0:
            days += 1
            self.unit -= self.power
            time.sleep(1)
            print(f"{self.name} сражается {days}день(дня)..., осталось {self.unit} воинов")
            if self.unit <= 0:
                print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


the_1 = Knight('Sir Lancelot', 10)
the_2 = Knight("Sir Galahad", 20)

the_1.start()
the_2.start()

the_1.join()
the_2.join()
print("Все битвы закончились!")