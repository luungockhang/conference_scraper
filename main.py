import asyncio
import combiner
import random
import time
from crawlers import crawler
from crawlers import crawler2

# Set interval here:
interval = 25
random_interval_a = interval - 4
random_interval_b = interval + 5

async def main():
    while True:
        random_interval = random.randrange(random_interval_a,random_interval_b)
        task1 = asyncio.create_task(crawler.run())
        task2 = asyncio.create_task(crawler2.run())
        await asyncio.gather(task1,task2)
        await combiner.combine()
        print('Processed CSV. Next interval: {0}'.format(random_interval))
        time.sleep(random_interval)

asyncio.run(main())