import aiohttp
import aiofiles
import asyncio
import re
import time

URLS = [
    'https://www.example.com',
    'https://www.python.org',
]

MAX_RETRIES = 3
CONCURRENT_REQUESTS = 5

async def fetch(session, url):
    for attempt in range(MAX_RETRIES):
        try:
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                return await response.text()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f'Ошибка при загрузке {url}: {e}. Попытка {attempt + 1} из {MAX_RETRIES}')
            await asyncio.sleep(2)
        return None

def parse_html(html):
    titles = re.findall(r'<h1>(.*?)</h1>', html)
    dates = re.findall(r'<time datetime="(.*?)">', html)
    return titles, dates

async def save_to_file(data, filename):
    async with aiofiles.open(filename, 'w') as f:
        for item in data:
            await f.write(f"{item}\n")

async def scrape(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        if html:
            titles, dates = parse_html(html)
            await save_to_file(titles, 'titles.txt')
            await save_to_file(dates, 'dates.txt')

async def main():
    tasks = []
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    async def bounded_scrape(url):
        async with semaphore:
            await scrape(url)

    for url in URLS:
        tasks.append(bounded_scrape(url))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Скрейпинг завершен за {time.time() - start_time:.2f} секунд")