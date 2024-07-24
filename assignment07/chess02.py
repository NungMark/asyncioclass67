import asyncio
import time

judit_compute_time = 0.1
opponent_compute_time = 0.5
move_pairs = 30
opponents = 24

async def game(x):
    start_board_time = time.perf_counter()
    for i in range(move_pairs):
        print("Judit Turn")
        print(f"Board {x+1} {i+1} Judit made a move")
        time.sleep(judit_compute_time)
        print("Opponent Turn")
        print(f"Board {x+1} {i+1} Opponents made a move")
        await asyncio.sleep(opponent_compute_time)
    print(f'Board-{x+1}- >>>>>>>>>>> Finished - in{round(time.perf_counter()) - start_board_time} secs\n')
    return round(time.perf_counter() - start_board_time)

async def main():
    coros = [game(x) for x in range(opponents)]
    await asyncio.gather(*coros)

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f'finished in{round(time.perf_counter() - start_time)} secs')