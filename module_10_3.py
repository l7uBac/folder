from random import randint
from time import sleep
import threading

class Bank:
    lock = threading.Lock()
    balance = 0

    def __init__(self):
        super().__init__()

    def deposit(self):
        n = randint(50, 500)
        if self.balance <= 500 and self.lock.locked():
            self.lock.release()
            for i in range(100):
                self.balance += n
                print(f'Пополнение: {n}. Баланс: {self.balance}.')

    def take(self):
        pass

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
#th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
#th2.start()
th1.join()
#th2.join()

print(f'Итоговый баланс: {bk.balance}')