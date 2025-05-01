from managers.config import *

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                remove(client)

def private_broadcast(receiver_name, message, sender_client):
    for client in clients:
        if hasattr(client, 'username') and client.username == receiver_name:
            try:
                client.send(message)
            except:
                remove(client)
            return True  
    return False  

def remove(client):
    if client in clients:
        clients.remove(client)
        client.close()