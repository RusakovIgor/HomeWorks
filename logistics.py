import pytest

class Delivery:
    def __init__(self, number, departure_point, destination_point, weight, time):
        self.number = number
        self.departure_point = departure_point
        self.destination_point = destination_point
        self.weight = weight
        self.time = time

    def __str__(self):
        return f"Номер доставки: {self.number}, Откуда: {self.departure_point}, Куда: {self.destination_point}, Вес: {self.weight}, Время: {self.time}"

#Сортировка по весу груза
def merge_sort(deliveries):
    if len(deliveries) > 1:
        mid = len(deliveries) // 2
        left_half = deliveries[:mid]
        right_half = deliveries[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].weight < right_half[j].weight:
                deliveries[k] = left_half[i]
                i += 1
            else:
                deliveries[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            deliveries[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            deliveries[k] = right_half[j]
            j += 1
            k += 1

#Сортировка по времени доставки
def quick_sort(deliveries):
    if len(deliveries) <= 1:
        return deliveries
    pivot = deliveries[len(deliveries) // 2]
    left = [x for x in deliveries if x.time < pivot.time]
    middle = [x for x in deliveries if x.time == pivot.time]
    right = [x for x in deliveries if x.time > pivot.time]
    return quick_sort(left) + middle + quick_sort(right)

#Сортировка по номеру доставки
def heapify(deliveries, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and deliveries[left].number > deliveries[largest].number:
        largest = left

    if right < n and deliveries[right].number > deliveries[largest].number:
        largest = right

    if largest != i:
        deliveries[i], deliveries[largest] = deliveries[largest], deliveries[i]
        heapify(deliveries, n, largest)

def heap_sort(deliveries):
    n = len(deliveries)
    for i in range(n // 2 - 1, -1, -1):
        heapify(deliveries, n, i)
    for i in range(n - 1, 0, -1):
        deliveries[i], deliveries[0] = deliveries[0], deliveries[i]
        heapify(deliveries, i, 0)

#Стек для срочной доставки
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

#Очередь для обработки заявок
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

#Поиск
def linear_search(deliveries, number):
    for delivery in deliveries:
        if delivery.number == number:
            return delivery
    return None

def binary_search(deliveries, time):
    low = 0
    high = len(deliveries) - 1

    while low <= high:
        mid = (low + high) // 2
        if deliveries[mid].time == time:
            return deliveries[mid]
        elif deliveries[mid].time < time:
            low = mid + 1
        else:
            high = mid - 1
    return None

#Управление доставками
class DeliveryManagementSystem:
    def __init__(self):
        self.deliveries = []

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)

    def remove_delivery(self, number):
        self.deliveries = [d for d in self.deliveries if d.number != number]

    def update_delivery(self, number, **kwargs):
        for delivery in self.deliveries:
            if delivery.number == number:
                for key, value in kwargs.items():
                    setattr(delivery, key, value)

    def sort_deliveries_by_weight(self):
        merge_sort(self.deliveries)

    def sort_deliveries_by_time(self):
        self.deliveries = quick_sort(self.deliveries)

    def sort_deliveries_by_number(self):
        heap_sort(self.deliveries)

    def search_delivery_by_number(self, number):
        return linear_search(self.deliveries, number)

    def search_delivery_by_time(self, time):
        # Сначала сортируем по времени
        self.sort_deliveries_by_time()
        return binary_search(self.deliveries, time)


delivery1 = Delivery(1, "Москва", "Санкт-Петербург", 30, "2024-10-12 10:00")
delivery2 = Delivery(2, "Казань", "Челябинск", 20, "2024-10-13 09:00")
delivery3 = Delivery(3, "Нижний Новгород", "Самара", 25, "2024-10-11 11:00")
delivery4 = Delivery(4, "Волгоград", "Оренбург", 15, "2024-10-14 08:00")
delivery5 = Delivery(5, "Екатеринбург", "Тюмень", 50, "2024-10-15 07:30")

# Создаем систему управления поставками
dms = DeliveryManagementSystem()

# Добавляем доставки в систему
dms.add_delivery(delivery1)
dms.add_delivery(delivery2)
dms.add_delivery(delivery3)
dms.add_delivery(delivery4)
dms.add_delivery(delivery5)


def main():
    while True:
        print("\nВыберите действие:")
        print("0. Список всех поставок")
        print("1. Добавить доставку")
        print("2. Сортировать доставки по весу")
        print("3. Сортировать доставки по времени")
        print("4. Сортировать доставки по номеру")
        print("5. Найти доставку по номеру")
        print("6. Найти доставку по времени")
        print("7. Использовать стек")
        print("8. Использовать очередь")
        print("9. Выход")

        choice = input("Введите номер действия: ")

        if choice == "0":
            print("Список поставок:")
            for delivery in dms.deliveries:
                print(delivery)

        elif choice == "1":
            number = int(input("Введите номер доставки: "))
            starting_location = input("Введите начальную локацию: ")
            destination = input("Введите конечную локацию: ")
            weight = int(input("Введите вес доставки: "))
            time = input("Введите время доставки (ГГГГ-MM-ДД ЧЧ:MM): ")
            delivery = Delivery(number, starting_location, destination, weight, time)
            dms.add_delivery(delivery)
            print("Доставка добавлена!")

        elif choice == "2":
            print("\nСортировка по весу:")
            dms.sort_deliveries_by_weight()
            for delivery in dms.deliveries:
                print(delivery)
            print("Доставки отсортированы по весу.")

        elif choice == "3":
            print("\nСортировка по времени:")
            dms.sort_deliveries_by_time()
            for delivery in dms.deliveries:
                print(delivery)
            print("Доставки отсортированы по времени.")

        elif choice == "4":
            print("\nСортировка по номеру:")
            dms.sort_deliveries_by_number()
            for delivery in dms.deliveries:
                print(delivery)
            print("Доставки отсортированы по номеру.")

        elif choice == "5":
            number = int(input("Введите номер доставки для поиска: "))
            found_delivery = dms.search_delivery_by_number(number)
            print(f"\nПоиск по номеру доставки {number}:")
            print(found_delivery)

        elif choice == "6":
            time = input("Введите время доставки для поиска (ГГГГ-MM-ДД ЧЧ:MM): ")
            found_delivery = dms.search_delivery_by_time(time)
            print(f"\nПоиск по времени доставки {time}:")
            print(found_delivery)

        elif choice == "7":
            stack = Stack()
            stack.push(delivery1)
            stack.push(delivery2)
            stack.push(delivery3)

            print("\nСтек срочных доставок (последние поступившие - первыми):")
            while not stack.is_empty():
                print(stack.pop())

        elif choice == "8":
            queue = Queue()
            queue.enqueue(delivery4)
            queue.enqueue(delivery5)

            print("\nОчередь доставок (первым пришел - первым обслужен):")
            while not queue.is_empty():
                print(queue.dequeue())

        elif choice == "9":
            print("Выход из программы.")
            break

        else:
            print("Недопустимый ввод. Пожалуйста, выберите номер действия от 0 до 9.")

#Тестирование


@pytest.fixture
def delivery_management_system():
    dms = DeliveryManagementSystem()
    dms.add_delivery(Delivery(1, "Москва", "Санкт-Петербург", 10.5, "2023-10-01 10:00"))
    dms.add_delivery(Delivery(2, "Казань", "Москва", 5.0, "2023-10-02 12:00"))
    dms.add_delivery(Delivery(3, "Екатеринбург", "Казань", 7.0, "2023-10-01 09:00"))
    return dms

def test_add_delivery(delivery_management_system):
    initial_count = len(delivery_management_system.deliveries)
    delivery_management_system.add_delivery(Delivery(4, "Новосибирск", "Калуга", 15.0, "2023-10-03 14:00"))
    assert len(delivery_management_system.deliveries) == initial_count + 1

def test_sort_deliveries_by_weight(delivery_management_system):
    delivery_management_system.sort_deliveries_by_weight()
    assert delivery_management_system.deliveries[0].weight == 5.0  # Доставка с наименьшим весом
    assert delivery_management_system.deliveries[1].weight == 7.0
    assert delivery_management_system.deliveries[2].weight == 10.5

def test_sort_deliveries_by_time(delivery_management_system):
    delivery_management_system.sort_deliveries_by_time()
    assert delivery_management_system.deliveries[0].time == "2023-10-01 09:00"  # Самая ранняя доставка

def test_search_delivery_by_number(delivery_management_system):
    delivery = delivery_management_system.search_delivery_by_number(2)
    assert delivery is not None
    assert delivery.number == 2

def test_search_delivery_not_found(delivery_management_system):
    delivery = delivery_management_system.search_delivery_by_number(99)
    assert delivery is None

def test_stack():
    stack = Stack()
    stack.push("item1")
    assert not stack.is_empty()
    assert stack.pop() == "item1"
    assert stack.is_empty()

def test_queue():
    queue = Queue()
    queue.enqueue("item1")
    assert not queue.is_empty()
    assert queue.dequeue() == "item1"
    assert queue.is_empty()

if __name__ == "__main__":
    main()