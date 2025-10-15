class DC:
    def __init__(self, name, region_id, worlds):
        self._dc_name = name
        self._region_id = region_id
        self._worlds = worlds

    def get_name(self):
        return self._dc_name

    def get_region_id(self):
        return self._region_id

    def get_worlds(self):
        return self._worlds
