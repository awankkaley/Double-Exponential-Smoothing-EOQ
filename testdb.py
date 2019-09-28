
import requests
import pandas as pd
import json
from pandas.io.json import json_normalize

data = []
response = requests.get("http://api.open-notify.org/astros.json")
parse = response.json()["people"]
for d in parse:
  nama = d['name']
  data.append(nama)

print(data)
