import psycopg2

# Конфигурация подключения к базе данных
DB_NAME = "students_db"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "5432"

def create_table():
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    course_number INT,
                    age INT
                )
            ''')
            conn.commit()

def add_student(first_name, last_name, course_number, age):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO students (first_name, last_name, course_number, age)
                VALUES (%s, %s, %s, %s)
            ''', (first_name, last_name, course_number, age))
            conn.commit()

def update_student(student_id, first_name, last_name, course_number, age):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        with conn.cursor() as cur:
            cur.execute('''
                UPDATE students
                SET first_name=%s, last_name=%s, course_number=%s, age=%s
                WHERE id=%s
            ''', (first_name, last_name, course_number, age, student_id))
            conn.commit()

def delete_student(student_id):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM students WHERE id=%s', (student_id,))
            conn.commit()

def list_students():
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM students')
            students = cur.fetchall()
            for student in students:
                print(student)

def main():
    create_table()
    while True:
        print("\nМеню:")
        print("1. Добавить студента")
        print("2. Обновить данные студента")
        print("3. Удалить студента")
        print("4. Показать список студентов")
        print("5. Выход")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            first_name = input("Имя: ")
            last_name = input("Фамилия: ")
            course_number = int(input("Номер курса: "))
            age = int(input("Возраст: "))
            add_student(first_name, last_name, course_number, age)
        elif choice == "2":
            student_id = int(input("ID студента: "))
            first_name = input("Имя: ")
            last_name = input("Фамилия: ")
            course_number = int(input("Номер курса: "))
            age = int(input("Возраст: "))
            update_student(student_id, first_name, last_name, course_number, age)
        elif choice == "3":
            student_id = int(input("ID студента: "))
            delete_student(student_id)
        elif choice == "4":
            list_students()
        elif choice == "5":
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
