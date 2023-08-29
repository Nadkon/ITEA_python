import asyncio


async def timer(interval):
    while True:
        await asyncio.sleep(interval)
        print (f'The timer complete in {interval} s.')

async def main():
    timers = [2, 3, 5]
    tasks = []

    for i in timers:
       tasks.append(asyncio.create_task(timer(i)))

    await asyncio.gather(*tasks)

asyncio.run(main())
