from threading import Thread
import time
from datetime import datetime

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.enemys = 100  # общее, начальное кол-во врагов
        self.name = name
        self.power = power


    def run(self):
        day = 0
        print(f"{self.name}, на нас напали!")
        while self.enemys > 0:
            self.enemys -= self.power
            time.sleep(1)
            day += 1
            print(f"{self.name} сражается {day} день(дня)..., осталось {self.enemys} воинов.")
        return print(f"{self.name} одержал победу спустя {day} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
