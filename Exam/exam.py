import asyncio
import httpx
import time

async def get_pokemon_details(client, url):
    print(f'{time.ctime()} - Getting data from {url}')
    response = await client.get(url)
    data = response.json()
    pokemon_names = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    return len(pokemon_names), pokemon_names

async def fetch_pokemon_abilities():
    async with httpx.AsyncClient() as client:
        battle_armor_url = 'https://pokeapi.co/api/v2/ability/battle-armor'
        speed_boost_url = 'https://pokeapi.co/api/v2/ability/speed-boost'
        
        battle_armor_task = asyncio.create_task(get_pokemon_details(client, battle_armor_url))
        speed_boost_task = asyncio.create_task(get_pokemon_details(client, speed_boost_url))
        
        battle_armor_count, battle_armor_names = await battle_armor_task
        speed_boost_count, speed_boost_names = await speed_boost_task
        
        print(f"\nจำนวน Pokémon ที่มีความสามารถ 'battle-armor': {battle_armor_count}")
        print(f"Pokémon เหล่านี้คือ: {', '.join(battle_armor_names)}")
        battle_armor_end_time = time.perf_counter()
        
        print(f"\nจำนวน Pokémon ที่มีความสามารถ 'speed-boost': {speed_boost_count}")
        print(f"Pokémon เหล่านี้คือ: {', '.join(speed_boost_names)}")
        speed_boost_end_time = time.perf_counter()

        return battle_armor_end_time, speed_boost_end_time

async def main():
    start_time = time.perf_counter()
    battle_armor_end_time, speed_boost_end_time = await fetch_pokemon_abilities()
    total_end_time = time.perf_counter()

    print(f"\nเวลาใช้ในการแสดงผล 'battle-armor': {battle_armor_end_time - start_time:.2f} seconds")
    print(f"เวลาใช้ในการแสดงผล 'speed-boost': {speed_boost_end_time - start_time:.2f} seconds")
    print(f"Total time taken: {total_end_time - start_time:.2f} seconds")

if __name__ == '__main__':
   asyncio.run(main())
