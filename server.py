import socket
from _thread import *
import json
from models.client import Client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

with open('config.json') as f:
    config = json.load(f)

server.bind((config['host'], config['port']))
server.listen(100)

clients = []
credentials = {}

def clientthread(client):
    client.send(f"{config['motd']}\n")
    
    while not client.logged_in:
        try:
            message = client.receive()
            if not message:
                break
            if message.startswith("REGISTER"):
                parts = message.split()
                if len(parts) == 3:
                    username, password = parts[1], parts[2]
                    if username in credentials:
                        client.send("ERR_ALREADYREGISTRED\n")
                    else:
                        credentials[username] = password
                        client.send("CONFIRM_REGISTER\n")
                        client.logged_in = True
                else:
                    client.send("ERR_TOOMANYPARAMS\n")
            else:
                client.send("ERR_INVALIDCMD\n")
        except Exception as e:
            print(f"Error: {e}")
            break

    client.send("MOTD hello world\n")

    while True:
        try:
            message = client.receive()
            if message:
                print(f"<{client.addr[0]}> {message}")
                broadcast(message, client)
            else:
                remove(client)
                break
        except Exception as e:
            print(f"Error: {e}")
            break

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                remove(client)

def remove(client):
    if client in clients:
        clients.remove(client)
        client.close()

while True:
    conn, addr = server.accept()
    client = Client(conn, addr)
    clients.append(client)
    print(f"{addr[0]} connected")
    start_new_thread(clientthread, (client,))

server.close()