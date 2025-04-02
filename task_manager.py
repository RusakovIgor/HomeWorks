import asyncio
from datetime import datetime

class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def sort_tasks(self):
        n = len(self.tasks)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.tasks[j].created_at > self.tasks[j+1].created_at:
                    self.tasks[j], self.tasks[j+1] = self.tasks[j+1], self.tasks[j]

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

class Task:
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.created_at = datetime.now()

    async def execute(self):
        print(f"Запуск задачи {self.id}: {self.description}")
        await asyncio.sleep(3) 
        print(f"Задача {self.id} завершена.")

async def run_tasks():
    manager = TaskManager()
    await asyncio.gather(*(task.execute() for task in manager.tasks))

async def main():
    manager = TaskManager()
    task_id_counter = 1

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Удалить задачу по ID")
        print("3. Запустить все задачи")
        print("4. Просмотреть список задач")
        print("5. Найти задачу по ID")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            task = Task(task_id_counter, description)
            manager.add_task(task)
            task_id_counter += 1
            print(f"Задача добавлена с ID {task.id}.")

        elif choice == '2':
            task_id = int(input("Введите ID задачи для удаления: "))
            manager.remove_task(task_id)
            print(f"Задача с ID {task_id} удалена.")

        elif choice == '3':
            print("Запуск всех задач...")
            await run_tasks()

        elif choice == '4':
            manager.sort_tasks()
            print("Список задач:")
            for task in manager.tasks:
                print(f"ID: {task.id}, Описание: {task.description}, Время создания: {task.created_at}")

        elif choice == '5':
            task_id = int(input("Введите ID задачи для поиска: "))
            task = manager.find_task(task_id)
            if task:
                print(f"Задача найдена: ID: {task.id}, Описание: {task.description}")
            else:
                print("Задача не найдена.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    asyncio.run(main())