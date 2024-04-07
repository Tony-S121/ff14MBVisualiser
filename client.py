from typing import Optional

import pandas as pd
import numpy as np
from apis import APICalls
import json
import asyncio
from aiohttp import ClientSession


class Client:

    def __init__(self, apiKey: str, session: Optional[ClientSession] = None) -> None:
        self.apiKey = apiKey
        self._session = session

    @property
    def session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            self._session = ClientSession()
        return self._session

async def main():
    c = Client('test', None)
    async with c.session as client:
        res = await APICalls.getWorlds(client)
        worlds = pd.read_json(res)
        with open('worlds.json', 'w') as f:
            json.dump(worlds.to_json(), f)

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())

asyncio.run(main())

#worlds = pd.read_json(res)
#worlds = pd.read_json(APICalls.getWorlds(c.getSession()).text)
#with open('worlds.json', 'w') as f:
 #  json.dump(worlds.to_json(), f)


