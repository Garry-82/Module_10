from threading import Thread, Lock

lock = Lock()
class BankAccount():

    def __init__(self, count):
        self.count = count  #  -  изначальный, текущий баланс счета
    def run(self,func):
        return func
    def deposit_task(self, bank_accaunt, amount):
        for i in range(10):
            with lock:
                bank_accaunt.count += amount
                print(bank_accaunt.count)
    def withdraw_task(self, bank_accaunt, amount):
        for i in range(10):
            with lock:
                bank_accaunt.count -= amount
                print(bank_accaunt.count)

account = BankAccount(1000)  #  - объект класса с заданным, изначальным балансом на счете

deposit_thread = Thread(target=account.deposit_task, args=(account, 100))
withdraw_thread = Thread(target=account.withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()