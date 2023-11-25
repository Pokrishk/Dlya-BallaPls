import asyncio
from random import randint
async def task1():
    i=0
    print(" ")
    while i<10:
        r = randint(1, 1000)
        print(f"{r}, ")
        i += 1
        await asyncio.sleep(2)
    await task2()
    print("Ну вот так. Это всё")
async def task2():
    print('\nВсе эти числа - ваши числа удачи')
    await asyncio.sleep(3)
    x = (int(input("Есть у вас любимая цифра? Какая? ")))
    if x<0:
        print("Алё так нельзя")
    else:
        print("Прекрасно, а теперь забудь эту цифру")
        b = x+10
        print(f"Теперь у тебя есть несчастливая цифра: {b}")
async def task3():
    i = 0
    while True:
        print(f"                                           {i} секунд",)
        await asyncio.sleep(1)
        i += 1
async def main():
    result = await asyncio.gather(task1(), task3())
    print(result)
asyncio.run(main())