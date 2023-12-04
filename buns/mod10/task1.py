import requests
import json
from collections import OrderedDict

ship_req = requests.get('https://swapi.dev/api/starships/10/')
ship_data = json.loads(ship_req.text, object_pairs_hook=OrderedDict)
ship_data["ship_name"] = ship_data["name"]

ship_lib = ["ship_name", "starship_class", "max_atmosphering_speed", "pilots"]
falcon = OrderedDict((key, ship_data[key]) for key in ship_lib)

pilot_lib = ["name", "height", "mass", "homeworld", "homeworld_url"]
pilots = []
for item in falcon["pilots"]:
    pilot_req = requests.get(item)
    pilot_data = json.loads(pilot_req.text, object_pairs_hook=OrderedDict)
    pilot_data["homeworld_url"] = pilot_data["homeworld"]

    home_req = requests.get(pilot_data["homeworld_url"])
    home_data = json.loads(home_req.text)

    pilot_data["homeworld"] = home_data["name"]
    pilots.append(OrderedDict((key, pilot_data[key]) for key in pilot_lib))
falcon["pilots"] = pilots

with open('falcon.json', 'w') as file:
    json.dump(falcon, file, indent=4)

print(json.dumps(falcon, indent=4))
