from aiohttp import ClientSession


class Client:

    def __init__(self, api_key: str = None, base_url: str = None) -> None:
        self.apiKey = api_key
        self.base_url = base_url

    async def fetch_data(self, endpoint):
        async with ClientSession() as session:
            async with session.get(f"{self.base_url}/{endpoint}") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Error fetching data from endpoint {endpoint}")
