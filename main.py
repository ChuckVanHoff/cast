import pandas as pd

import config
import collect_owm
import load

client = config.client
data = collect_owm.collect(limit=1)
load_result = load.load(data, client)
print(load_result)
