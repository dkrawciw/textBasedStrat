import json

with open("gameSetup.json", 'r') as worldInformation:
    worldInfo = json.load(worldInformation)
with open("playerInformation.json", "r") as playerInformation:
    playerInfo = json.load(playerInformation)

print(f'Welcome, {playerInfo["playerName"]}!')