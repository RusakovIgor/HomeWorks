import asyncio

counter = 0
lock = asyncio.Lock()

try:
    async def increment_counter(inc_count):
        global counter
        for _ in range(inc_count):
            async with lock:
                counter += 1


    async def main():
        tasks_num = 13
        inc_per_task = 100000

        tasks = [increment_counter(inc_per_task) for _ in range(tasks_num)]

        await asyncio.gather(*tasks)


    asyncio.run(main())

    # Проверка значения счетчика

    expected_value = 13 * 100000
    print(f"Конечное значение счетчика - {counter}, ожидаемое значение счетчика - {expected_value}")
except Exception as e:
    print(f"An Error occured: {e}")