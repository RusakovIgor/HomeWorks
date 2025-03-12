class OldService:
    def fetch_data(self):
        return "Данные в старом формате"

# Интерфейс NewService, предоставляющий метод для получения данных в новом формате
class NewService:
    def get_data(self):
        return "Данные в новом формате"

# Адаптер ServiceAdapter, который адаптирует OldService к NewService
class ServiceAdapter(NewService):
    def __init__(self, old_service):
        self.old_service = old_service

    # Метод get_data() адаптирует старый формат данных к новому
    def get_data(self):
        old_data = self.old_service.fetch_data()  # Получаем данные из OldService
        # Преобразуем данные в новый формат (например, добавляем префикс)
        return f"Конвертировано: {old_data}"

# Использование адаптера с объектом OldService
old_service = OldService()         # Создаем объект старого сервиса
adapter = ServiceAdapter(old_service)  # Создаем адаптер
print(adapter.get_data())          # Вызываем метод get_data для получения адаптированных данных

import pytest

def test_service_adapter():
    #Создаем объект старого сервиса
    old_service = OldService()
    #Создаем адаптер
    adapter = ServiceAdapter(old_service)
    #Вызываем метод get_data для получения адаптированных данных
    result = adapter.get_data()
    #Проверка на соответствие ожидаемым результатам
    expected_result = "Конвертировано: Данные в старом формате"
    assert result == expected_result