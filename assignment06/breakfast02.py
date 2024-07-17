import asyncio
import time

class Coffee:
    pass

class Egg:
    pass

class Bacon:
    pass

class Toast:
    pass

class Juice:
    pass

def pour_coffee():
    print(f"{time.ctime()} - Begin pour coffee...")
    time.sleep(2)
    print(f"{time.ctime()} - Finish pour coffee...")
    print(f"{time.ctime()} - >>>>>>>> Coffee is ready")
    return Coffee()

async def apply_butter():
    print(f"{time.ctime()} - Begin apply butter...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} - Finish apply butter...")

async def fry_eggs(eggs):
    print(f"{time.ctime()} - Begin fry eggs...")
    print(f"{time.ctime()} - Heat pan to fry eggs")
    await asyncio.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} - Frying", egg + 1, "eggs")
        await asyncio.sleep(1)
    print(f"{time.ctime()} - >>>>>>>> Fry eggs are ready...")
    return Egg()

async def fry_bacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    await asyncio.sleep(2)
    print(f"{time.ctime()} - Finish fry bacon...")
    print(f"{time.ctime()} - >>>>>>>> Fry bacon is ready...")
    return Bacon()

async def toast_bread(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        await asyncio.sleep(1)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        await apply_butter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    print(f"{time.ctime()} - >>>>>>>> Toast are ready")
    return Toast()

def pour_juice():
    print(f"{time.ctime()} - Begin pour juice...")
    time.sleep(1)
    print(f"{time.ctime()} - Finish pour juice...")
    return Juice()

async def main():

    bacon_task = asyncio.create_task(fry_bacon())
    toast_task = asyncio.create_task(toast_bread(2))
    egg_task = asyncio.create_task(fry_eggs(2))
   
    pour_coffee()
    print(f"{time.ctime()} >>>>>>>> Coffee is ready\n")

    await egg_task
    await bacon_task
    await toast_task

    print(f"{time.ctime()} - >>>>>>>> Nearly to finished...")
    pour_juice()

    

if __name__ == "__main__":
    start_cooking = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} - Breakfast cooked in {elapsed:.10f} seconds.")