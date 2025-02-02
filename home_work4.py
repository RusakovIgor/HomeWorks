class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Название книги - {self.title}\nАвтор книги - {self.author}\nГод публикации - {self.year}\n'


def quick_sort(books, key):
    if len(books) <= 1:
        return books
    pivot = books[len(books) // 2]
    left = [x for x in books if getattr(x, key) < getattr(pivot, key)]
    middle = [x for x in books if getattr(x, key) == getattr(pivot, key)]
    right = [x for x in books if getattr(x, key) > getattr(pivot, key)]
    return quick_sort(left, key) + middle + quick_sort(right, key)


def merge_sort(books, key):
    if len(books) <= 1:
        return books
    mid = len(books) // 2
    left_half = merge_sort(books[:mid], key)
    right_half = merge_sort(books[mid:], key)
    return merge(left_half, right_half, key)


def merge(left, right, key):
    result = []
    while left and right:
        if getattr(left[0], key) <= getattr(right[0], key):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def heapify(books, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and getattr(books[left], key) > getattr(books[largest], key):
        largest = left
    if right < n and getattr(books[right], key) > getattr(books[largest], key):
        largest = right
    if largest != i:
        books[i], books[largest] = books[largest], books[i]
        heapify(books, n, largest, key)


def heap_sort(books, key):
    n = len(books)
    for i in range(n // 2 - 1, -1, -1):
        heapify(books, n, i, key)
    for i in range(n - 1, 0, -1):
        books[i], books[0] = books[0], books[i]
        heapify(books, i, 0, key)
    return books


def find_books(books, search_key):
    return [book for book in books if search_key.lower() in book.title.lower() or search_key.lower() in book.author.lower()]


library = [
    Book("1984", "Джордж Оруэл", 1949),
    Book("История двух городов", "Чарльз Диккенс", 1859),
    Book("Великий Гэтсби", "Ф. Скотт Фицжеральд", 1925),
    Book("Убить Пересмешника", "Харпер Ли", 1960),
    Book("Гордость и предубеждение", "Джейн Остин", 1813),
    Book("Над пропастью во ржи", "Дж. Селлинджер", 1951),
    Book("Хоббит", "Дж.Р.Р. Толкиен", 1937),
    Book("451 градус по Фаренгейту", "Рей Бредбери", 1953),
    Book("Трудно быть Богом", "Братья Стругацкие", 1964),
    Book("Братья Карамазовы", "Федор Достоевский", 1880)
]

while True:
    print("\nДобро пожаловать в систему управления библиотекой!\n")
    print("Выберите действие:")
    print("1. Показать все книги")
    print("2. Сортировать книги по названию")
    print("3. Сортировать книги по автору")
    print("4. Сортировать книги по году издания")
    print("5. Найти книгу по названию")
    print("6. Найти книгу по автору")
    print("7. Добавить книгу")
    print("8. Удалить книгу")
    print("9. Выйти")

    try:
        action = int(input("Введите номер действия: "))
        if action < 1 or action > 9:
            print("Пожалуйста, выберите номер от 1 до 9.")
            continue

        if action == 1:
            print("Список всех книг:")
            for book in library:
                print(book)

        elif action == 2:
            sorted_books = quick_sort(library, 'title')
            print("Книги отсортированы по названию:")
            for book in sorted_books:
                print(book)

        elif action == 3:
            sorted_books = merge_sort(library, 'author')
            print("Книги отсортированы по автору:")
            for book in sorted_books:
                print(book)

        elif action == 4:
            sorted_books = heap_sort(library[:], 'year')  # Используем срез, чтобы сохранить оригинальный список
            print("Книги отсортированы по году издания:")
            for book in sorted_books:
                print(book)

        elif action == 5:
            title = input("Введите часть названия книги: ")
            found_books = find_books(library, title)
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(book)
            else:
                print("Книги не найдены.")

        elif action == 6:
            author = input("Введите имя автора: ")
            found_books = find_books(library, author)
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(book)
            else:
                print("Книги не найдены.")

        elif action == 7:
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.append(Book(title, author, year))
            print("Книга добавлена.")

        elif action == 8:
            title = input("Введите название книги для удаления: ")
            for book in library:
                if book.title.lower() == title.lower():
                    library.remove(book)
                    print("Книга удалена.")
                    break
            else:
                print("Книга не найдена.")

        elif action == 9:
            print("Выход из программы.")
            break

    except ValueError:
        print("Ошибка: введите числовое значение.")