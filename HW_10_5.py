import multiprocessing
class WarehouseManager():
    data = {}
#    def __init__(self):
#        super().__init__()

    def run(self, requests):
        with multiprocessing.Pool(4) as pool:
             self.data = pool.map(self.process_request, requests)
    def process_request(self, request):
        if request[1] == "receipt":  #  -  пополнение товара на склад
            if request[0] in self.data:
                self.data[request[0]] += request[2]
            if request[0] not in self.data:
                self.data[request[0]] = request[2]
            return self.data

        elif request[1] == "shipment":  #  -  отгрузка товара со склада
            if request[0] in self.data:
                self.data[request[0]] -= request[2]
            if request[0] not in self.data:
                print(f"Товар {request[0]} отсутстует на складе!! Его отгрузка невозможна!!")
            return self.data

if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()


    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)



