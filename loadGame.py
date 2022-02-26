import json

with open("test.json", 'r') as worldInformation:
    gameInfo = json.load(worldInformation)

print(gameInfo)