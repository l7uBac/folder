from random import randint
from time import sleep
import threading

class Bank(threading.Thread):
    lock = threading.Lock()
    balance = 0

    def __init__(self):
        super().__init__()

    def deposit(self):
        count = 0
        if self.lock.locked():
            if self.balance >= 500:
                self.lock.release()
        else:
            for i in range(100):

                n = randint(50, 500)
                self.balance += n
                count += 1
                print(f'{count} - Пополнение: {n}. Баланс: {self.balance}.')
                sleep(0.001)

    def take(self):
        for i in range(100):
            n = randint(50, 500)
            if n <= self.balance:
                print(f"Запрос на {n}")
                self.balance -= n
                print(f"Снятие: {n}. Баланс: {self.balance}")
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')