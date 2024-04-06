import pandas as pd
import numpy as np
import APIs
import json


worlds= pd.read_json(APIs.getWorlds().text)
with open('worlds.json', 'w') as f:
    json.dump(worlds.to_json(), f)


