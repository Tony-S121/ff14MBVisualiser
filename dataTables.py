from client import Client
from apis import APICalls
import pandas as pd
import asyncio
import json


async def get_world_data():
    client = Client(base_url='https://universalis.app/api/v2')
    api_caller = APICalls(client)
    return await api_caller.get_worlds()


world_data = asyncio.get_event_loop().run_until_complete(get_world_data())
print(world_data)
worlds_df = pd.DataFrame(world_data)

with open('worlds.json', 'w') as f:
    json.dump(world_data, f)
