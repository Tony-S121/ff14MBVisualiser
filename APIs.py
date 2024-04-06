import requests as req
import asyncio

def getWorlds():
    return req.get('https://universalis.app/api/v2/worlds')


def getDCs():
    return req.get('https://universalis.app/api/v2/data-centers')


def getItemCurrData(worldDcRegion, itemIds, params: dict = None) -> object:
    ##'https://universalis.app/api/v2/12/1,2,3?listings=1&entries=1&hq=1&statsWithin=1&entriesWithin=1&fields=1'
    endPoint = 'https://universalis.app/api/v2/'
    endPoint += str(worldDcRegion) + '/' + str(itemIds)
    if not params:
        endPoint += '?'
        for param in params:
            endPoint = param + '=' + str(params.get(param)) + '&'
        endPoint = endPoint[:-1]
    return req.get(endPoint)


def getWorldTaxRates():
    return req.get('https://universalis.app/api/v2/extra/stats/least-recently-updated')


def getWorlds():
    return req.get('https://universalis.app/api/v2/worlds')


def getWorlds():
    return req.get('https://universalis.app/api/v2/worlds')



