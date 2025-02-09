import heapq
import pytest

class Task:
    def __init__(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority
        self.status = "Pending"

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f'{self.name} - {self.duration} сек., Приоритет: {self.priority}, Статус: {self.status}'

class TaskScheduler:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        heapq.heappush(self.queue, (task.priority, task))

    def execute_tasks(self):
        while not self.is_empty():
            task = self.execute_task()
            task.status = "In Progress"
            print(f'Выполняется: {task}')
            task.status = 'Completed'
            print(f'Завершено: {task}')

    def execute_task(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        raise IndexError('deque from empty queue')

    def is_empty(self):
        return len(self.queue) == 0

    def task_count(self):
        return len(self.queue)

task1 = Task("Установление TCP-соединения", 1, 2)
task2 = Task("Обработка HTTP-запроса", 1, 1)
task3 = Task("Ожидание ответа от базы данных", 1, 3)
task4 = Task("Отправка ответа клиенту", 1, 1)

scheduler = TaskScheduler()
scheduler.add_task(task1)
scheduler.add_task(task2)
scheduler.add_task(task3)
scheduler.add_task(task4)

print(f'Пустой: {scheduler.is_empty()}')
print(f'Количество задач: {scheduler.task_count()}')
scheduler.execute_tasks()


def test_task_creation():
    task = Task('Тестовая задача', 5, 1)
    assert task.name == 'Тестовая задача'
    assert task.duration == 5
    assert task.priority == 1
    assert task.status == 'Pending'

def test_task_scheduler_add_and_count():
    scheduler = TaskScheduler()
    task1 = Task('Задача1', 1, 1)
    task2 = Task('Задача2', 2, 2)

    scheduler.add_task(task1)
    scheduler.add_task(task2)

    assert scheduler.task_count() == 2
    assert not scheduler.is_empty()

def test_execute_tasks():
    scheduler = TaskScheduler()
    task1 = Task('Задача1', 1, 1)
    task2 = Task('Задача2', 1, 2)

    scheduler.add_task(task1)
    scheduler.add_task(task2)

    scheduler.execute_tasks()

    assert task1.status == 'Completed'
    assert task2.status == 'Completed'

def test_execute_empty_scheduler():
    scheduler = TaskScheduler()
    with pytest.raises(IndexError):
        scheduler.execute_task()

if __name__ == "__main__":
    pytest.main()