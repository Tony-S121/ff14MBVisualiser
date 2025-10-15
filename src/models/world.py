from pydantic import BaseModel


class World(BaseModel):

    world_id: int
    name: str
    
    def __init__(self, world_id, name):
        self.world_id = world_id
        self.name = name

    def getWorldId(self):
        return self.worldId

    def getName(self):
        return self.name
