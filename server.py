import socket
from _thread import *
from models.client import Client
from managers.config import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((config['host'], config['port']))
server.listen(100)

while True:
    conn, addr = server.accept()
    client = Client(conn, addr)
    clients.append(client)
    print(f"{addr[0]} connected")
    start_new_thread(client.thread, ())

server.close()