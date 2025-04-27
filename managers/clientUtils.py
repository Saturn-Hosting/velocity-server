from managers.config import *

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