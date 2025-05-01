import json

with open('config.json') as f:
    config = json.load(f)

with open('MOTD.txt') as f:
    config['motd'] = f.read()

clients = []