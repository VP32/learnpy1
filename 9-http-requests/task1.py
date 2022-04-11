from pprint import pprint

import requests

superheroes = [{"name": "Hulk"}, {"name": "Captain America"}, {"name": "Thanos"}]
token = "2619421814940190"
host = " https://superheroapi.com/api/" + token + "/"

for hero in superheroes:
    resp = requests.get(host + "search/" + hero["name"])
    resp.raise_for_status()
    id = resp.json()["results"][0]["id"]
    hero["id"] = id
    resp1 = requests.get(host + id + "/powerstats")
    resp1.raise_for_status()
    intelligence = resp1.json()["intelligence"]
    hero["intelligence"] = int(intelligence)

superheroes.sort(key=lambda d: d['intelligence'], reverse=True)
print(f"Самый умный супергерой: {superheroes[0]['name']}")
