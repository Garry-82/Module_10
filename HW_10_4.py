import threading
import time
from threading import Thread
import queue
from time import sleep

class Table():  #  -  класс для столов
    def __init__(self, number):
        self.number = number
        self.is_bussy = True
class Cafe():  #  -  класс для кафе
    def __init__(self, tables):
        self.tables = tables
        self.list_customer = queue.Queue()  #  - очередь входящих посетителей!
        self.waiter = queue.Queue()  #  - очередь ожидающих обслуживание
    def Table_free(self):
        tb_free = []
        for i in self.tables:
            tb_free.append(i.is_bussy)
        if True in tb_free:
            tb_free.clear()
            return True
        if not True in tb_free:
            tb_free.clear()
            return False
    def customer_arrival(self):  #  - формирование очереди Посетителей!!!! (НЕ очередь ожидания!!!)
        c = 0
        while c < 20:
            c += 1
            guest = ("Посетитель № " + str(c))
            self.list_customer.put(guest)
            print(guest + " прибыл")
            time.sleep(1)
    def serve_customer(self, customer):
        j = 0
        while self.tables[j].is_bussy != True:
            j += 1
        else:
            self.tables[j].is_bussy = False
            print(f"{customer} сел за стол № {self.tables[j].number}")
            sv = Customer(customer, j)
            sv.start()
            sv.join()
class Customer(Thread):  #  -  класс (поток) для Посетителя
    def __init__(self, customer, index):
        super().__init__()
        self.customer = customer
        self.index = index
    def run(self):  #  -  функция обслуживания клиента (запуск потока!)
        time.sleep(5)
        print(f"{self.customer} покушал и ушел.")
        cafe.tables[self.index].is_bussy = True

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)

customer_arrival_thread.start()
time.sleep(0.001)  #  -  небольшая пауза между приходом первого посетителя и началом обслуживания! (выводом на экран

while not cafe.list_customer.empty() or not cafe.waiter.empty():
    if cafe.Table_free() == True and cafe.waiter.empty():
        sv1 = threading.Thread(target=cafe.serve_customer, args=(cafe.list_customer.get(), ))
        sv1.start()
        time.sleep(1)
        continue
    elif cafe.Table_free() == True and not cafe.waiter.empty():
        cafe.serve_customer(cafe.waiter.get())
        sv1 = threading.Thread(target=cafe.serve_customer, args=(cafe.waiter.get(), ))
        sv1.start()
        sv1.join()

    elif cafe.Table_free() == False:
        guest = cafe.list_customer.get()
        cafe.waiter.put(guest)
        print(f"{guest} ожидает свободный стол")
        time.sleep(1)

else:
    print("Обслуживание посетителей закончилось, кафе закрыто!!")

customer_arrival_thread.join()
sv1.join()

