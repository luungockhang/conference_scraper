# Created by 22880068, 22880179
# May 25 2024
# v0.1
# Run the program from here. Manages asynchronous execution.

# For user interface, change the 

import asyncio
import combiner
import random
import time
import hh
from crawlers import crawler
from crawlers import crawler2

# Set interval here:
interval = 60
random_interval_a = interval - 4
random_interval_b = interval + 5

#
# UPDATE: June 16 2024, LIX.POLYTECHNIQUE.FR IS STILL OFFLINE, THEREFORE REMOVE TASK1 AND ONLY RUN TASK2 
# -- 22880068
#

async def main():
    while True:
        random_interval = random.randrange(random_interval_a,random_interval_b)
        task1 = asyncio.create_task(crawler.run())   # Remove this task because website is offline.
        task2 = asyncio.create_task(crawler2.run())
        await asyncio.gather(task1,task2)   # Run these tasks concurrently
        await combiner.combine()
        await hh.import_to_db()
        print('Database updated. Next interval: {0}'.format(random_interval))
        time.sleep(random_interval)

asyncio.run(main())