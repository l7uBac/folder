from random import randint
from time import sleep
import threading

class Bank(threading.Thread):
    lock = threading.Lock()
    balance = 0

    def __init__(self):
        super().__init__()

    def deposit(self):
        for i in range(100):
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            n = randint(50, 500)
            self.balance += n
            print(f'Пополнение: {n}. Баланс: {self.balance}.')
            sleep(0.001)

    def take(self):
        for i in range(100):
            m = randint(50, 500)
            print(f"Запрос на {m}")
            if m <= self.balance:
                self.balance -= m
                print(f"Снятие: {m}. Баланс: {self.balance}")
            if m > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')