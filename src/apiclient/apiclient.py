from aiohttp import ClientSession


class Client:
    def __init__(self, api_key: str = None, base_url: str = None) -> None:
        self.apiKey = api_key
        self.base_url = base_url

    async def check_endpoint(self, endpoint):
        async with ClientSession() as session:
            async with session.get(f"{self.base_url}/{endpoint}") as response:
                return response.status

    async def fetch_data(self, endpoint):
        async with ClientSession() as session:
            async with session.get(f"{self.base_url}/{endpoint}") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Error fetching data from endpoint {endpoint}")


class APICalls:
    def __init__(self, api_client):
        self.api_client = api_client

    async def get_data(self):
        return await self.api_client.fetch_data("data")

    async def get_worlds(self):
        worlds_endpoint = "worlds"
        return await self.api_client.fetch_data(worlds_endpoint)

    async def get_dcs(self, session):
        dc_endpoint = "data-centers"
        async with session.get(dc_endpoint) as response:
            return response.json()

    async def get_item_curr_data(
        self, worldDcRegion, itemIds, params: dict = None
    ) -> object:
        ##'https://universalis.app/api/v2/12/1,2,3?listings=1&entries=1&hq=1&statsWithin=1&entriesWithin=1&fields=1'
        endpoint = str(worldDcRegion) + "/" + str(itemIds)
        if not params:
            endpoint += "?"
            for param in params:
                endpoint = param + "=" + str(params.get(param)) + "&"
            endpoint = endpoint[:-1]
        return await self.api_client.fetch_data(endpoint)

    async def get_world_tax_rates(self):
        tax_rates_endpoint = "extra/stats/least-recently-updated"
        return await self.api_client.fetch_data(tax_rates_endpoint)
