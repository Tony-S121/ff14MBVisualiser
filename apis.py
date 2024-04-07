import requests as req

class APICalls:

    endPoint = 'https://universalis.app/api/v2/'
    @classmethod
    async def getWorlds(cls, session):
        worldsEndPoint = APICalls.endPoint + 'worlds'
        async with session.get(worldsEndPoint) as response:
            return response.json()


    async def getDCs(self, session):
        DCEndPoint = APICalls.endPoint + 'data-centers'
        async with session.get(DCEndPoint) as response:
            return response.json()


    async def getItemCurrData(worldDcRegion, session, itemIds, params: dict = None) -> object:
        ##'https://universalis.app/api/v2/12/1,2,3?listings=1&entries=1&hq=1&statsWithin=1&entriesWithin=1&fields=1'
        endPoint = APICalls.endPoint
        endPoint += str(worldDcRegion) + '/' + str(itemIds)
        if not params:
            endPoint += '?'
            for param in params:
                endPoint = param + '=' + str(params.get(param)) + '&'
            endPoint = endPoint[:-1]
        async with session.get(endPoint) as response:
            return await response


    async def getWorldTaxRates(self, session):
        taxRatesEndPoint = APICalls.endPoint + 'extra/stats/least-recently-updated'

        async with session.get(taxRatesEndPoint) as response:
            return await response
