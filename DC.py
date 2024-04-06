class DC:
    def __init__(self, name, regionId, worlds):
        self.name = name
        self.regionId = regionId
        self.worlds = worlds

    def getName(self):
        return self.name

    def getRegionId(self):
        return self.regionId

    def getWorlds(self):
        return self.worlds
