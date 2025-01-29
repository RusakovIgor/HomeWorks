import unittest

class Employee:
    def __init__(self, names, ages, salaries):
        self.names = names
        self.ages = ages
        self.salaries = salaries

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

        return arr

    def sort_names(self):
        return self.shell_sort(self.names.copy())

    def sort_ages(self):
        return self.shell_sort(self.ages.copy())

    def sort_salaries(self):
        return self.shell_sort(self.salaries.copy())


employee = Employee(["Петров","Иванов", "Сидоров", "Яковлев", "Ли"], [34, 45, 22, 56, 18],
                    [44000, 33000, 22000, 67000, 11000])

names_result = employee.sort_names()
ages_result = employee.sort_ages()
salarie_result = employee.sort_salaries()

print(f"Сортировка фамилий - {names_result}")
print(f"Сортировка возрастов - {ages_result}")
print(f"Сортировка зарплат - {salarie_result}")

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(
            ["Петров","Иванов", "Сидоров", "Яковлев", "Ли"],
            [34, 45, 22, 56, 18],
            [44000, 33000, 22000, 67000, 11000]
        )

    def test_sort_names(self):
        expected_names = ["Иванов", "Ли", "Петров", "Сидоров", "Яковлев"]
        self.assertEqual(self.employee.sort_names(), expected_names)

    def test_sort_ages(self):
        expected_ages = [18, 22, 34, 45, 56]
        self.assertEqual(self.employee.sort_ages(), expected_ages)

    def test_sort_salaries(self):
        expected_salaries = [11000, 22000, 33000, 44000, 67000]
        self.assertEqual(self.employee.sort_salaries(), expected_salaries)

if __name__ == '__main__':
    unittest.main()