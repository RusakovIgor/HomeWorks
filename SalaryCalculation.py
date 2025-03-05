from functools import partial
import pytest

def hours_per_day(hours):
    return lambda days: hours * days

def bonus_percentage(percentage):
    return lambda salary: (percentage / 100) * salary

def net_salary(gross_salary, tax_rate):
    return gross_salary - (gross_salary * tax_rate)

tax_20 = partial(net_salary, tax_rate=0.20)

def final_salary(base_salary, bonus):
    return base_salary + bonus

bonus_500 = partial(final_salary, bonus=500)

def calculate_hours(hours_per_day, days):
    return hours_per_day * days

def calculate_gross_salary(hours, hourly_rate):
    return hours * hourly_rate

def composed_salary_function(hours_per_day, days, hourly_rate):
    hours = calculate_hours(hours_per_day, days)
    return calculate_gross_salary(hours, hourly_rate)

def calculate_net_salary(gross_salary):
    return gross_salary - (gross_salary * 0.20)

def apply_bonus(salary, bonus):
    return salary + bonus

def final_salary_composition(gross_salary, bonus):
    salary_with_bonus = apply_bonus(gross_salary, bonus)
    return calculate_net_salary(salary_with_bonus)

result = hours_per_day(8)(20)
print(result)

result = bonus_percentage(10)(3000)
print(result)

result = tax_20(5000)
print(result)

result = bonus_500(3000)
print(result)

result = composed_salary_function(8, 20, 25)
print(result)

result = final_salary_composition(4000, 300)
print(f"Финальная зарплата - {result}")

def test_hours_per_day():
    assert hours_per_day(8)(5) == 40
    assert hours_per_day(0)(10) == 0

def test_bonus_percentage():
    assert bonus_percentage(10)(1000) == 100
    assert bonus_percentage(0)(1000) == 0

def test_net_salary():
    assert net_salary(1000, 0.20) == 800
    assert net_salary(1000, 0.25) == 750

def test_final_salary():
    assert final_salary(1000, 500) == 1500
    assert final_salary(200, 300) == 500

def test_calculate_hours():
    assert calculate_hours(8, 5) == 40
    assert calculate_hours(0, 10) == 0

def test_calculate_gross_salary():
    assert calculate_gross_salary(40, 15) == 600
    assert calculate_gross_salary(0, 10) == 0

def test_composed_salary_function():
    assert composed_salary_function(8, 5, 15) == 600
    assert composed_salary_function(0, 10, 20) == 0

def test_calculate_net_salary():
    assert calculate_net_salary(1000) == 800
    assert calculate_net_salary(600) == 480

def test_apply_bonus():
    assert apply_bonus(5000, 500) == 5500
    assert apply_bonus(900, 300) == 1200

def test_final_salary_composition():
    assert final_salary_composition(1000, 500) == 1200
    assert final_salary_composition(600, 200) == 640

if __name__ == '__main__':
    pytest.main()