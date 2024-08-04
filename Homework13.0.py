import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(8 / power)
        print(f'Силач {name} поднял шар {i+1}')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Илья', 5))
    task_2 = asyncio.create_task(start_strongman('Добрыня', 4))
    task_3 = asyncio.create_task(start_strongman('Алёша', 3))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())
